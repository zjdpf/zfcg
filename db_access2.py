# --*-- coding: utf-8 --*--
from model2 import *
from sqlalchemy import func

session = DBSession()

#公告列表保存到数据库
def Save_to_mysql(zfcglists):
    try:
        result=session.query(Zfcglists).filter_by(id=zfcglists.id).first()
        if result:
            print(result)
            result.updatatime=func.now()
            result.keywords=zfcglists.keywords
            session.flush()
            print("update success!!!")
        else:
            print(zfcglists)
            session.add(zfcglists)
            session.flush()
            print("insert success!!!")
    except Exception as e:
        print(str(e))

#根据公告id查询公告详细信息，更新发布时间、正文信息，下载保存附件

