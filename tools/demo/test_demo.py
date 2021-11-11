# -*- coding: utf-8 -*-
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
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: test_demo.py
@time: 2018/7/27 20:44
@desc:
'''
import os

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r'E:\drivers\Drivers'

print("开始爬取")
# 创建chrome参数对象
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
# options.add_argument('--window-size=1920,1080')  # 指定浏览器窗口大小
options.add_argument('--start-maximized')  # 浏览器窗口最大化
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
# options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片,加快访问速度
# options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
options.add_argument('test-type')
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors",
                                                    "enable-automation"])
# options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度


browser = webdriver.Chrome(options=options, executable_path=os.path.join(driver_path, 'chromedriver.exe'))
browser.maximize_window()
browser.get('https://kfadmin.atats.shop/')
browser.implicitly_wait(15)

baidu_img = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#regForm > fieldset > label:nth-child(4) > span > img'))
)
browser.save_screenshot("screenshot.png")  # 对整个浏览器页面进行截图
left = baidu_img.location['x']
top = baidu_img.location['y']
right = baidu_img.location['x'] + baidu_img.size['width']
bottom = baidu_img.location['y'] + baidu_img.size['height']
# 输出元素
print(baidu_img.location)
print(baidu_img.size)
# 加个延迟
import time
time.sleep(1)
im = Image.open('screenshot.png')
# 值都加100
im = im.crop((left+100, top+100, right+100, bottom+100))  # 对浏览器截图进行裁剪
im.save('baidu.png')
print("爬取完成")
