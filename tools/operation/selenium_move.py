# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_move.py
@time: 2017/6/21 21:00
@项目名称:operating_call
"""
import os
import time

#这是鼠标移动类，传入相应的id，name，text，xpath，css就可以执行鼠标移动的指令
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

def id_move(browser,id):
    try:
        #   找到需要转移的元素
        ele = browser.find_element_by_id(id)
        #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
        auto_move(browser,ele)
    except:
        writeLog()

def name_move(browser,name):
    try:
        #   找到需要转移的元素
        ele = browser.find_element_by_name(name)
        #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
        auto_move(browser,ele)
    except:
        writeLog()

def text_move(browser,text):
    try:
        #   找到需要转移的元素
        ele = browser.find_element_by_link_text(text)
        #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
        auto_move(browser,ele)
    except:
        writeLog()

def xpath_move(browser,xpath):
    try:
        #   找到需要转移的元素
        ele = browser.find_element_by_xpath(xpath)
        #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
        auto_move(browser,ele)
    except:
        writeLog()

def css_move(browser,css):
    try:
        #   找到需要转移的元素
        ele = browser.find_element_by_css_selector(css)
        #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
        auto_move(browser,ele)
    except:
        writeLog()

def auto_move(browser,br_ele):
    from selenium.webdriver import ActionChains
    ActionChains(browser).move_to_element(br_ele).perform()
    time.sleep(2)

def writeLog():
    basename = os.path.splitext(os.path.basename(__file__))[0]
    print("selenium_move,名为名=%s"% \
          basename,)
