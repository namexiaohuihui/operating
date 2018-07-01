# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: dalao
@time: 2017/6/20 21:53
"""
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

from multiprocessing import cpu_count, Process, Queue

from tomorrow import threads
import numpy as np
from tools.RewriteThread import InheritThread, InheritProcess
from tools.browser_establish import browser_confirm
from tools.openpyxlExcel import OpenExcelPandas
from tools.operation.selenium_click import action_click
from tools.operation.selenium_input import action_input

file_path = 'C:\\Users\\70486\\Desktop\\'
read = OpenExcelPandas(file_path + '买家记录300.xlsx', sheet='名字')
df_excelData = read.internal_read_excel(title='买家ID')
df_excelData.loc[:, '验证码'] = np.array([5] * len(df_excelData))


class AotuLoginStop():
    aci = action_input()
    acc = action_click()

    def liulanqi(cls, link_value):
        print("程序开始执行")
        # 1.创建浏览器所在函数的对象
        cls.bc = browser_confirm.__new__(browser_confirm)

        cls.url = 'http://wechat5.t-lianni.com/login?f=/user'

        cls.driver = cls.bc.url_opens(cls.url, link_value)

    def auto_auto(self, acc_number='18778036030'):
        print("开始执行登陆")

        try:
            # 2.调用已经规划好的浏览器函数
            self.driver.get(self.url)
            # 账号密码登陆
            self.aci.id_input(self.driver, 'J_tel', acc_number)
            self.aci.id_input(self.driver, 'J_code', '123456')
            # 登陆按钮
            self.acc.id_click(self.driver, 'J_login')

            self.acc.css_click(self.driver, '.am-dialog-button.cancel')  # 提示设置密码

        except:
            print("提示密码设置框  或者   城市公告提示框  没有出现")
        print("登陆执行完毕")
        pass

    def auto_stop(self):
        try:
            import time
            if self.is_home:
                print("红包领取完毕")
            else:
                print("红包提示语一直存在呢?")
                time.sleep(3)

            print("执行退出")
            self.acc.css_click(self.driver, '.nav-user')

            self.acc.css_click(self.driver, '.sysMsg.slide')  # 遮盖层
            self.acc.css_click(self.driver, '.setting')
            self.acc.css_click(self.driver, '.J_logout.tab-list.center')
            self.acc.css_click(self.driver, 'div.am-dialog-footer > button:nth-child(2)')
            print("退出完成")
            self.driver.quit()
        except:
            print("这里什么")

    def auto_home(self):
        print("首页领取红包")
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
            print("红包弹窗 或者 红包提示语 地方")
        print("提示信息获取完毕: %s" % ele_toast)
        return ele_toast

    def test_auto_bunus(self, link_key,link_value):
        print("------------------")
        self.liulanqi(link_key)
        print('+++++++++++++++++++++')
        start_iloc = dict(link_value.get(timeout=2))
        print("正在执行第 %s 的数据, %s" % (str(start), start_iloc))
        self.auto_auto(str(start_iloc['认证手机']))
        ele_toast = self.auto_home()
        self.auto_stop()
        start_iloc['验证码'] = ele_toast
        link_value = start_iloc.values()
        if link_key == 'firefox':
            self.driver.close()
        # print("*************************")
        # print(df_excelData)
        # df_excelData.to_csv(file_path + 'multiprocessing执行完毕.csv', index=False, encoding="gbk")
        # print("*************************")


if __name__ == '__main__':
    link_range_len = [{'chrome': (0, 2)}, {'firefox': (4, 6)}]
    link_list = []
    # workqueue = Queue(1000)
    print("开始正价")
    for key, values in link_range_len[0].items():
        value = link_range_len[0][key]
        workqueue = Queue(value[1])
        for neirong in range(value[0],value[1]):
            workqueue.put(df_excelData.iloc[neirong])
        link_range_len[0][key] = workqueue
    print("还在家？")
    # for linkk in range(len(link_range_len)):
    #     print(link_range_len[linkk])
    #     qidong = AotuLoginStop()
    #     qidong.test_auto_bunus(link_range_len[linkk])
    for linkk in range(0, 4):
        qidong = InheritProcess(AotuLoginStop().test_auto_bunus, link_range_len)
        qidong.daemon = True
        qidong.start()
        link_list.append(qidong)
        # qidong.join()
    for qidong in link_list:
        qidong.join()
    df_excelData.to_csv(file_path + 'multiprocessing执行完毕.csv', index=False, encoding="gbk")
