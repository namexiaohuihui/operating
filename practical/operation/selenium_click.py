# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_click
@time: 2017/6/20 22:07
"""
import os
# 这是元素点击类，传入相应的id，name，text，xpath，css就可以执行的点击事件
from time import sleep

from practical.Exception_error.DefinitionError import definition_error

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
def id_click(browser,id):
    try:
        browser.find_element_by_id(id).click()
        sleep(2)
    except:
        writeLog(browser)


def name_click(browser,name):
    try:
        browser.find_element_by_name(name).click()
        sleep(2)
    except:
        writeLog(browser)

def text_click(browser,text):
    try:
        browser.find_element_by_link_text(text).click()
        sleep(2)
    except:
        writeLog(browser)


def xpath_click(browser,xpath):
    try:
        browser.find_element_by_xpath(xpath).click()
        sleep(2)
    except:
        writeLog(browser)

def css_click(browser,css):
    try:
        browser.find_element_by_css_selector(css).click()
        sleep(2)
    except:
        writeLog(browser)


def writeLog(browser):
    basename = os.path.splitext(os.path.basename(__file__))[0]
    # 组合日志文件名（当前文件名 + 当前时间）.比如：case_login_success_20150817192533
    de_error = definition_error()
    de_error.erroe_get(basename, browser)
    #raise
