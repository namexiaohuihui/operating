# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: domoTaothereTwo.py
@time: 2018/5/13 21:24
@Entry Name:operating
"""

import requests
from bs4 import BeautifulSoup
link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
r = requests.get(link,headers)
# soup = BeautifulSoup(r.text,"lxml")
soup = BeautifulSoup(r.text,"html.parser")
title = soup.find("h1",class_="post-title")
print(title)
tstra = title.a.text.strip()
print(tstra)


