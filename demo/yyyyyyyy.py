# -*- coding: utf-8 -*-
"""
@file: yyyyyyyy.py
@time: 18-4-4 下午4:00
@Author  : Ubuntu
@Software: PyCharm Community Edition
"""

import os
import sys

import numpy as np

# 获取项目路径下的目录
os.chdir('E:\\operating')
# 将项目路径保存
sys.path.append('E:\\operating')
# import HTMLTestReportCN

# 获取当前文件所在目录
CUR_PATH = os.path.dirname(os.path.realpath(__file__))

from tools.RewriteThread import InheritThread
from tools.browser_establish import browser_confirm
from tools.configs import readModel
from tools.openpyxlExcel import OpenExcelPandas
from tools.operation.selenium_click import action_click
from tools.operation.selenium_input import action_input
from tools.Logger import Log

file_path = 'F:\\desktop\\'
file_name = '执行完毕'
read_name = "10倒叙用户"
read = OpenExcelPandas(file_path + ('%s.csv' % read_name), sheet=',')
df_excelData = read.internal_read_csv(title='买家ID')
df_excelData.loc[:, '验证码'] = np.array([5] * len(df_excelData))
logs = Log("Ubuntu")
logs.functionName("AotuLoginStop")


class AotuLoginStop():
    aci = action_input()
    acc = action_click()

    def liulanqi(cls, link_value):
        logs.info("程序开始执行")
        # 1.创建浏览器所在函数的对象
        try:
            cls.bc = browser_confirm.__new__(browser_confirm)

            conf = readModel.establish_con(model="model")  # 获取账号密码
            cls.url = conf.get("wap", "buyer_url")

            cls.driver = cls.bc.url_opens(cls.url, link_value)
        except Exception as e:
            print(e)

    def auto_auto(self, acc_number):
        logs.info("开始执行登陆")

        try:
            # 2.调用已经规划好的浏览器函数
            self.driver.get(self.url)
            # 账号密码登陆
            self.aci.id_input(self.driver, 'J_tel', acc_number)
            self.aci.id_input(self.driver, 'J_code', '123456')
            # 登陆按钮
            self.acc.id_click(self.driver, 'J_login')

            self.acc.css_click(self.driver, '.am-dialog-button.cancel')  # 提示设置密码
            # self.acc.css_click(self.driver, '.am-dialog-button')  # 公告



        except:
            print("提示密码设置框  或者   城市公告提示框  没有出现")
        logs.info("登陆执行完毕")
        pass

    def auto_stop(self):
        try:
            import time
            if self.is_home:
                logs.info("红包领取完毕")
            else:
                logs.info("红包提示语一直存在呢")
                time.sleep(3)

            logs.info("执行退出")
            self.acc.css_click(self.driver, '.nav-user')

            self.acc.css_click(self.driver, '.sysMsg.slide')  # 遮盖层
            self.acc.css_click(self.driver, '.setting')
            self.acc.css_click(self.driver, '.J_logout.tab-list.center')
            self.acc.css_click(self.driver, 'div.am-dialog-footer > button:nth-child(2)')
            logs.info("退出完成")
            self.driver.close()
        except:
            logs.info("这里什么")

    def auto_home(self):
        logs.info("首页领取红包")
        self.acc.css_click(self.driver, '.nav-index')
        try:
            # 吐司
            ele = self.aci.is_visible_css_selectop(self.driver, '.toast-cont')
            if ele:
                ele_toast = ele.text
                self.is_home = False
            else:
                # 红包弹窗
                bunus_ele = self.acc.css_click(self.driver, '.close-bonus-btn')
                if bunus_ele:
                    ele_toast = "红包领取成功"
                    self.is_home = True
                else:
                    ele_toast = "什么鬼?"
                    self.is_home = False
        except:
            logs.info("红包弹窗 或者 红包提示语 地方")
        logs.info("提示信息获取完毕: %s" % ele_toast)
        return ele_toast

    def test_auto_bunus(self, link_range_len):
        logs.info("------------------")
        logs.info(link_range_len)
        logs.info(link_range_len.items())
        for link_key, link_value in link_range_len.items():
            pass
        for start in range(link_value[0], link_value[1]):
            start_iloc = dict(df_excelData.iloc[start])
            logs.info("浏览器为 %s 正在执行第 %s 的数据, %s" % (link_key, str(start), start_iloc))
            if start_iloc['认证手机'] != 0:
                self.liulanqi(link_key)
                logs.info('+++++++++++++++++++++')
                self.auto_auto(str(start_iloc['认证手机']))

                ele_toast = self.auto_home()

                self.auto_stop()

            else:
                ele_toast = '用户没有手机号'

            start_iloc['验证码'] = ele_toast
            df_excelData.iloc[start] = start_iloc.values()
        # self.driver.quit()
        # if link_key == 'firefox':
        #     self.driver.close()


if __name__ == '__main__':
    # link_range_len = [{'firefox': (0, 100)}, {'chrome': (101, 200)}]
    link_range_len = [{'firefox': (900, 1000)}]  # 整数是我的
    link_list = []
    for linkk in range(len(link_range_len)):
        qidong = InheritThread(AotuLoginStop().test_auto_bunus, link_range_len[linkk])
        qidong.start()
        link_list.append(qidong)
    for qidong in link_list:
        qidong.join()
    firefox_start = link_range_len[0]['firefox'][0]
    firefox_stop = link_range_len[0]['firefox'][1]
    names_path = 'firefox-%s-chrome-%s.csv' % \
                 (str(firefox_start), str(firefox_stop))
    # 只读取运行的数据
    logs.info("%s-----------------%s" % (type(firefox_start), type(firefox_stop)))
    df_excelData = df_excelData.iloc[firefox_start:firefox_stop]
    css_file = os.path.join(file_path, names_path)
    df_excelData.to_csv(css_file, index=False, encoding="gbk")
    print(css_file)
