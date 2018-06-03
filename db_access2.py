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

#取出所有id，供循环处理
def Querey_zfcglists_id():
    try:
        result1=session.query(Zfcglists.id).all()
        result2=session.query(Zfcg_deatil.id).all()
        result=list(set(result1).difference(set(result2)))
        return  result
    except:
        return ""

def Save_zfcg_deatil(zfcg_deatil):
    try:
        result=session.query(Zfcg_deatil).filter_by(id=zfcg_deatil.id).first()
        if result:
            print("Data is exist in mysql!!!")
        else:
            print(zfcg_deatil)
            session.add(zfcg_deatil)
            session.flush()
            print("insert success!!!")
    except Exception as e:
        print(str(e))

def Query_zfcg_deatil():
    try:
        result=session.query(Zfcg_deatil).filter_by(fjbool='0')
        pass
    except:
        pass

