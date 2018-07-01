import unittest

import numpy as np

from tools.browser_establish import browser_confirm
from tools.openpyxlExcel import OpenExcelPandas
from tools.operation.selenium_click import action_click
from tools.operation.selenium_input import action_input

file_path = 'C:\\Users\\70486\\Desktop\\'


class AotuLoginStop(unittest.TestCase):
    aci = action_input()
    acc = action_click()

    @classmethod
    def setUpClass(cls):
        print("程序开始执行")
        # 1.创建浏览器所在函数的对象
        cls.bc = browser_confirm.__new__(browser_confirm)

        cls.url = 'http://wechat5.t-lianni.com/login?f=/user'

        cls.driver = cls.bc.url_opens(cls.url)

    @classmethod
    def tearDownClass(cls):
        print("程序结束")

    def auto_auto(self, acc_number='18778036030'):
        print("开始执行登陆")

        try:
            # 2.调用已经规划好的浏览器函数
            # self.driver = bc.dingdong_mobile_opens(url)
            self.driver.get(self.url)
            # self.bc.browser.get(self.url)
            # 账号密码登陆
            self.aci.id_input(self.driver, 'J_tel', acc_number)
            self.aci.id_input(self.driver, 'J_code', '123456')
            # 登陆按钮
            self.acc.id_click(self.driver, 'J_login')

            self.acc.css_click(self.driver, '.am-dialog-button.cancel')  # 提示设置密码

        except:
            print("提示密码设置框  或者   城市公告提示框  没有出现")
        print("登陆执行完毕")
        # time.sleep(1)
        pass

    def auto_stop(self):
        try:
            import time
            # ele = self.aci.is_not_visible_css_selectop(self.driver, '.toast-cont')
            if self.is_home:
                print("红包领取完毕")
            else:
                print("红包提示语一直存在呢?")
                time.sleep(4)

            print("执行退出")
            self.acc.css_click(self.driver, '.nav-user')

            self.acc.css_click(self.driver, '.sysMsg.slide')  # 遮盖层
            self.acc.css_click(self.driver, '.setting')
            self.acc.css_click(self.driver, '.J_logout.tab-list.center')
            self.acc.css_click(self.driver, 'div.am-dialog-footer > button:nth-child(2)')
            print("退出完成")
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

    def test_auto_bunus(self):
        read = OpenExcelPandas(file_path + '买家记录300.xlsx', sheet='名字')
        df_excelData = read.internal_read_excel(title='买家ID')
        # print(df_excelData)
        df_excelData.loc[:, '验证码'] = np.array([5] * len(df_excelData))
        print("------------------")
        try:
            for start in range(len(df_excelData)):
                print('+++++++++++++++++++++')
                start_iloc = dict(df_excelData.iloc[start])
                print("正在执行第 %s 的数据, %s" % (str(start), start_iloc))
                self.auto_auto(str(start_iloc['认证手机']))
                ele_toast = self.auto_home()
                self.auto_stop()
                start_iloc['验证码'] = ele_toast
                df_excelData.iloc[start] = start_iloc.values()
            self.driver.close()
        except Exception as  e:
            print(e)
        finally:
            print("*************************")
            print(df_excelData)
            df_excelData.to_csv(file_path + '执行完毕.xlsx', index=False, encoding="gbk")
            print("*************************")


if __name__ == '__main__':
    unittest.main(verbosity=2)
