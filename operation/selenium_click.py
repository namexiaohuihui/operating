# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_click
@time: 2017/6/20 22:07
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

def id_click(browser,id):
    try:
        # global browser
        browser.find_element_by_id(id).click()
    except:
        writeLog()


def name_click(browser,name):
    try:
        # global browser
        browser.find_element_by_name(name).click()
    except:
        writeLog()


def xpath_click(browser,xpath):
    try:
        # global browser
        browser.find_element_by_xpath(xpath).click()
    except:
        writeLog()


def css_click(browser,css):
    try:
        # global browser
        browser.find_element_by_css_selector(css).click()
    except:
        writeLog()

def writeLog():
    basename = os.path.splitext(os.path.basename(__file__))[0]
    print("文件名为", basename, "出现了错误")
    raise