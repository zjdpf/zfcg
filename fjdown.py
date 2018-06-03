# # -*- coding:utf-8 -*-
import requests
from db_access2 import *
from bs4 import BeautifulSoup
import  re
import json

def gen(each):
    url = "http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?noticeId=%s"%each+"&url=http%3A%2F%2Fnotice.zcy.gov.cn%2Fnew%2FnoticeDetail"
    html=getHtmltext(url)
    fjxx=getFjxx(html)
    #保存附件信息表
    zfcg_deatil=Zfcg_deatil(
        id=each,
        url=url,
        detailtext=html,
        fbdate=fjxx[0],
        fjurl=fjxx[1],
        fjurlname=fjxx[2],
        createtime=func.now(),
        updatatime=func.now(),
        )
    Save_zfcg_deatil(zfcg_deatil)

def getHtmltext(url):
    try:
        req=requests.get(url,timeout=30)
        req.encoding=req.apparent_encoding
        req.raise_for_status()
        return req.text
    except:
        return ""

def getFjxx(html):
    fbsj=json.loads(html)["noticePubDate"]      #获取发布时间
    print(fbsj)
    data = json.loads(html)["noticeContent"]    #获取正文内容
    #从正文中搜索附件url
    soup = BeautifulSoup(data, "lxml")
    href=soup.find_all("a",href=re.compile("aliyuncs"))
    if href:
        for link in href:
            fhref=link.get("href")
            fname=link.contents[0]
            fjurl=[fbsj,fhref,fname] #发布时间、附件url链接、附件名称
        return  fjurl
    else:
        fhref=" "
        fname=" "
        fjurl=[fbsj,fhref,fname]
        return fjurl

def gen_info():
    for each in Querey_zfcglists_id():
        gen(each)
    # gen('294712')

if __name__ == '__main__':
    gen_info()




#
# import json
#
# data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
# print('DATA:', repr(data))
# print(type(data))
#
# data_string = json.dumps(data)
# print ('JSON:', data_string)
# print(type(data_string))

#
# try:
#     import cPickle as pickle
# except ImportError:
#     import pickle

# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))


#
# f = open('c:/dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# import json
# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d))

# import  json
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))
#
# import json
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
# s = Student('Bob', 20, 88)
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))