# -*- coding:utf-8 -*-
import json
from celery import Celery
from db_access2 import *
from sqlalchemy import func
celery_app3=Celery('celery_zfcg2',broker='redis://172.17.173.196:6379/1')

@celery_app3.task
def gen(i):
    types = ['10', '20', '30', '40', '50']  # 5种类型
    for type in types:
        pathname=r'C:/zfcg1/%djson%s'%(i,str(type))
        with open(pathname,'r',encoding='utf-8') as f:
            zjfc_dict=json.load(f)
            for each in zjfc_dict.get('articles'):
                zfcglists=Zfcglists(
                    id=each['id'],
                    mainBidMenuName=each['mainBidMenuName'],
                    title=each['title'],
                    projectCode=each['projectCode'],
                    pubDate=each['pubDate'],
                    districtName=each['districtName'],
                    type=each['type'],
                    typeName=each['typeName'],
                    keywords=each['keywords'],
                    url=each['url'],
                    createtime=func.now(),
                    updatatime=func.now(),
                    ggtype=str(type)
                    )
                Save_to_mysql(zfcglists)
        print("The Json of Number %s is dealing over ！！！" %i)

def gen_info():
    for i in range(1,101):
        gen.delay(i)

if __name__ == '__main__':
    gen_info()
