# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_input.py
@time: 2017/6/21 0:01
"""
import os
# 这是元素输入类，传入相应的id，name，text，xpath，css以及内容就可以执行输入的指令
import sys
from time import sleep

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

def id_input(browser,id, data):
    try:
        ele = browser.find_element_by_id(id)
        ele_clear_keys(ele, data)
    except:
        writeLog()


def name_input(browser,name, data):
    try:
        ele = browser.find_element_by_name(name)
        ele_clear_keys(ele, data)
    except:
        writeLog()


def css_input(browser,css, data):
    try:
        ele = browser.find_element_by_css_selector(css)
        ele_clear_keys(ele, data)
    except:
        writeLog()


def xpath_input(browser,xpath, data):
    try:
        ele = browser.find_element_by_xpath(xpath)
        ele_clear_keys(ele,data)
    except:
        writeLog()

def ele_clear_keys(ele,data):
    ele.clear()
    ele.send_keys(data)
    sleep(1)

def writeLog():
    basename = os.path.splitext(os.path.basename(__file__))[0]
    print("自己定义的_文件出现错误,名为名=%s"% \
          basename,)
    sys.exit(0)
    raise
