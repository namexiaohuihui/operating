# -*- coding: utf-8 -*-
"""
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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      goods_shuju.py
@time:      2018/12/18 21:58
@desc:
"""
import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from tools.openpyxlExcel import OpenExcelPandas
from tools.Logger import Log
from selenium.webdriver.support.select import Select

log_s = Log()
url = "---"

driver_path = 'E:\drivers\Drivers'
browser = webdriver.Chrome(executable_path=os.path.join(driver_path, 'chromedriver239-68.exe'))
browser.maximize_window()
# 输入网址
browser.get(url)
# 等待网页加载，加载时间为10s，加载完就跳过
# 隐形等待时间和显性等待时间不同时，默认使用两者之间最大的那个
browser.implicitly_wait(15)

# denglu
browser.find_element_by_name("username").send_keys("admin")
browser.find_element_by_name("password").send_keys("123456")
browser.find_element_by_id("loginBtn").click()
read = OpenExcelPandas(r"C:\Users\DingDonf\Desktop\完蛋还是蛋完.xlsx", sheet='完蛋还是蛋完')
df_excelData = read.readCaseExcel("buyer_id")
time.sleep(3)
browser.get(url + "/goods/barrel_deposit")
time.sleep(2)
works_se = browser.find_element_by_css_selector(".form-control.workstatus")
select = Select(works_se)
select.select_by_visible_text("用户ID")

for ex in range(len(df_excelData)):
    buy_input = browser.find_element_by_css_selector("input[type='search']")
    buy_input.clear()
    ex_data =df_excelData.iloc[ex]
    in_data = str(ex_data.loc["buyer_id"]).replace(" ", "")
    buy_input.send_keys(in_data)
    action_type = browser.find_elements_by_css_selector(".btn.btn-default.btn-flat.btn-action.J_ipt")[0]
    action_type.click()
    time.sleep(2)
    datatleThead = browser.page_source
    soup = BeautifulSoup(datatleThead, "lxml")

    # 找数据
    thead_td = soup.find("tbody").find('tr').find_all('td')

    if '暂无数据' in thead_td[0].text.replace(" ", ""):
        log_s.debug("该用户没有找到:---%s" % ex_data)
    else:
        si_text = int(thead_td[4].text.replace("\n", "").replace(" ", ""))
        wu_text = int(thead_td[5].text.replace("\n", "").replace(" ", ""))
        if si_text > wu_text:
            text_thead = [str.strip(th.text).replace("\n", "") for th in thead_td]
            log_s.error("该用户数据不对:(%s---%s)" % (ex_data, text_thead))
