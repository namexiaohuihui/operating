# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: hello.py
@time: 2017/11/29 22:15
@项目名称:operating
"""
import requests

# 接口的url
url = "http://fanyi.baidu.com/v2transapi"

# 接口的参数
params = {
    "from":"en",
    "to":"zh",
    "query": "study"
}

r = requests.request("post", url, params=params)

# 打印返回结果
#　print(r.text)

# 为了让结果看的更加清楚一点，我取来翻译的字段
import json
d = json.loads(r.text)
print(d['liju_result']['tag'])