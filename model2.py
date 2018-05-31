# -*- coding:utf-8 -*-
from  sqlalchemy import create_engine,Column,String,Text,DateTime
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from config2 import *

# （1）初始化数据库连接（连接参数从DB模块引入）
engine = create_engine('mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset=utf8'.format(
    USERNAME=DB['USER'],
    PASSWORD=DB['PASSWORD'],
    HOST=DB['HOST'],
    PORT=DB['PORT'],
    DB_NAME=DB['DB_NAME'],
), convert_unicode=True, echo=False)  #echo = True 是为了方便 控制台 logging 输出一些sql信息，默认是False

#（2）声明ORM映射基类
Base=declarative_base()

#（3）政府采购信息表
class Zfcglists(Base):
    __tablename__ = 'zfcglists'
    id=Column(String(7),primary_key=True) #编码
    mainBidMenuName=Column(String(100)) #行业类型
    title=Column(String(200)) #标题
    projectCode=Column(String(100)) #项目代码
    pubDate=Column(String(20)) #发布时间
    districtName=Column(String(20)) #所在地区
    type=Column(String(5)) #公告类型代码
    typeName=Column(String(50)) #公告类型名称
    keywords=Column(Text) #关键词
    url=Column(String(200)) #url地址
    createtime=Column(DateTime(timezone=True), default=func.now()) #创建时间
    updatatime=Column(DateTime(timezone=True), default=func.now()) #更新时间
    ggtype=Column(String(2))#公告大类：[0:全部公告]  [10:采购公告] [2同公告]','40 [其他标讯]','50 [采购公示]','20 [结果公告]'
    def __repr__(self):
        return "<Zfcglists(id='%s')>" % self.id


#（4）政府采购，公告详细信息表
class Zfcg_deatil(Base):
    __tablename__ = 'zfcg_deatil'
    id=Column(String(7),primary_key=True) #编码
    url=Column(String(200)) #公告url连接
    fjbool=Column(String(1)) #公告是否存在附件
    downflag=Column(String(1)) #附件是否已经下载保存
    detailtext=Column(Text) #公告详细正文信息
    fbdate=Column(DateTime(timezone=True)) #公告发布时间
    fjurl=Column(String(200)) #附件url
    createtime=Column(DateTime(timezone=True), default=func.now()) #创建时间
    updatatime=Column(DateTime(timezone=True), default=func.now()) #更新时间
    def __repr__(self):
        return "<zfcg_deatil(id='%s')>" % self.id


#声明会话类
Session=sessionmaker(bind=engine)
DBSession = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))

def init_db(db_engine):
  Base.metadata.create_all(bind=db_engine)

if __name__ == '__main__':
    init_db(engine)
