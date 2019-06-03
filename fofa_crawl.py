# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:cike
# datetime:2019-05-30 17:04

import requests
import base64, time


EMAIL = 'email'
API_KEY = 'api'
filed = "host,ip,port"
search_key = '"influxdb" && port=8086'
page_to = 10  # 需要翻到多少页，默认每页返回1000条


def crawl(search_content, page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)', }
    url = "https://fofa.so/api/v1/search/all?email=%s&key=%s&qbase64=%s&fields=%s&size=1000&page=%s" % (
        EMAIL, API_KEY, search_content, filed, page)
    try:
        req = requests.get(url=url, timeout=16, headers=headers)
        content = req.json()
        result = content['results']
        print(len(result))
        return result
    except:
        return 'cike'


if __name__ == '__main__':
    f = open('ok.txt', 'w+')
    base64_str = base64.b64encode(search_key.encode('utf-8'))
    base64_str2 = str(base64_str, 'utf-8')
    for num in range(1, page_to):
        time.sleep(2)
        result_list = crawl(base64_str2, str(num))
        if result_list == "cike":
            pass
        else:
            for i in result_list:
                m = i[0] + "###" + i[1] + "###" + i[2] + '\n'
                f.write(m)
    f.close()
