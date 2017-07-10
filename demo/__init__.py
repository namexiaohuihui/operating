# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/6/20 21:43
"""
import os
import time


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

from constant.browser.browser_establish import browser_confirm
from constant.url_website.url_data import url_content
from operation import selenium_click
from operation import selenium_input
from constant.parameter.parameter_data import parameter_content

try:
    bc = browser_confirm.__new__(browser_confirm)
    _browser_ = bc.call_browser()
    url = url_content.__new__(url_content)
    _browser_.get(url.return_account())
    _browser_.implicitly_wait(30)
    # 新增一个窗口打开url
    newwindow = 'window.open(\'url.return_account()\');'
    _browser_.execute_script(newwindow)

except Exception as msg:
    now = time.strftime("%Y%m%d.%H.%M.%S")
    t = _browser_.get_screenshot_as_file("%s.png" % now)
    print(u"截图返回值:%s" % t)
    print(u"报错信息%s" % msg)
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
