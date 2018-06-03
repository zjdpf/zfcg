# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

import  bs4
from bs4 import  BeautifulSoup
import  requests,json
import  time
from celery import Celery
# app3=Celery('download',broker='redis://172.17.173.196:6379/1')
app3=Celery('download',broker='redis://127.0.0.1:6379/1')

@app3.task
def zfcg(i):
    types=['10','20','30','40','50']#5种类型  [0:全部公告]  [10:采购公告] [20:结果公告] [30:合同公告] [40:其他标讯] [50:采购公示]
    for type in types:
        url = "http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?pageSize=%d&pageNo=%d&noticeType=%s" % (100,i,type) + "&url=http%3A%2F%2Fnotice.zcy.gov.cn%2Fnew%2FnoticeSearch"
        req=requests.get(url,timeout=30)
        req.encoding=req.apparent_encoding
        print(req.status_code)
        filename="c:/zfcg1/"+str(i)+"json"+str(type)
        with open(filename,'w',encoding='utf-8') as f:
            f.write(req.text)
        print("%s类型的第%s 个文件创建成功 " % (str(type),str(i)))


def craw():
    start = time.time()
    # for i in range(1,101):
    for i in range(1,7):
        zfcg.delay(i)
    print("it tooks", time.time() - start, "seconds")

if __name__ == '__main__':
    craw()