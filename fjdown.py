# # -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import  re
import json

url="http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?noticeId=1834900&url=http%3A%2F%2Fnotice.zcy.gov.cn%2Fnew%2FnoticeDetail"


def getHtmltext(url):
    try:
        req=requests.get(url,timeout=30)
        req.encoding=req.apparent_encoding
        req.raise_for_status()
        return req.text
    except:
        return ""

def getFjxx(html):
    soup=BeautifulSoup(html,"lxml")
    href=soup.find_all("a",href=re.compile("zcy"))
    for link in href:
        print(link.get("href"),link.contents[0])

if __name__ == '__main__':
    data=getHtmltext(url)
    html=json.loads(data)["noticeContent"]
    getFjxx(html)


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