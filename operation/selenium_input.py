# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_input.py
@time: 2017/6/21 0:01
@项目名称:operating
"""
import os

'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
'''
from parameter import browser_establish
'''
global browser
browser = browser_establish.browser_confirm().call_browser()
'''

def id_input(browser,id,data):
    try:
        # global browser
        ele = browser.find_element_by_id(id)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()

def name_input(browser,name,data):
    try:
        # global browser
        ele = browser.find_element_by_name(name)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()

def css_input(browser,css,data):
    try:
        # global browser
        ele = browser.find_element_by_css_selector(css)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()

def xpath_input(browser,xpath,data):
    try:
        # global browser
        ele = browser.find_element_by_xpath(xpath)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()


def writeLog():
    basename = os.path.splitext(os.path.basename(__file__))[0]
    print("文件名为", basename, "出现了错误")
    raise