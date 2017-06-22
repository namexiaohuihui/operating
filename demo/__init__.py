# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/6/20 21:43
"""
import os
import time

import logging

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

from parameter.browser import browser_establish
from operation import selenium_move_child

try:
    one = browser_establish.browser_using()
    _browser_ = one.call_browser()
    _browser_.get("https://www.baidu.com")
    _browser_.implicitly_wait(30)
    _browser_.find_element_by_id("weqw")
    # selenium_move_child.xpath_move_text_click("//*[@id=\"u1\"]/a[8]","搜索设置")
except Exception as msg:
    now = time.strftime("%Y%m%d.%H.%M.%S")
    t = _browser_.get_screenshot_as_file("%s.png" % now)
    print(u"棘突%s" % t)

'''
if __name__ == "__main__":

    name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename="./" +name,
                        filemode='w')
    logging.error(name)
    print(name)

'''
