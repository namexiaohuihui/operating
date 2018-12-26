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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file:  dispatch_work.py
@time: 2018/12/26 20:57
@Software: PyCharm
@Site    : 
@desc:
"""
from time import sleep
from SimpleProcess.openbrowser import OpenBrowper
from tools.screeningdrop import ScreeningDrop
from tools.configs import readModel


class DispatchWork(object):
    def __init__(self, muen_i, user_pass=True):
        self.op_br = OpenBrowper()
        self.op_br.open_driver('dispatch_url')

        self.warehousing_login(user_pass)
        self.access_muen_module(muen_i)
        pass

    def get_object_work(self):
        return self.op_br

    def close_quit_driver(self):
        self.op_br.driver.quit()

    def get_option_text(self, label_path):
        screen = ScreeningDrop(self.op_br.driver, label_path, attr='css')
        option_text = screen.getSelectedOptions()
        del screen
        return option_text
        pass

    def warehousing_login(self, user_pass):
        """
        登录操作
        :param user_pass: 区分登录者类型
        :return:
        """
        conf = readModel.establish_con(model="model")  # 获取账号密码
        if user_pass:
            account = conf.get("username", "admin_dispatch_account")
            password = conf.get("username", "admin_dispatch_password")
        else:
            account = conf.get("username", "level_dispatch_account")
            password = conf.get("username", "level_dispatch_password")
        # 账号
        self.op_br.is_visible_inputs(locator='phone', way='id', parameter=account)
        # 密码
        self.op_br.is_visible_inputs(locator='password', way='id', parameter=password)
        # 点击登录
        self.op_br.is_visible_clicks(locator='loginBtn', way='id')

        del conf
        sleep(1)
        pass

    def access_muen_module(self, muen_int):
        # 进入菜单
        muen_int = '.nav.nav-list>li:nth-child(%s)' % muen_int
        self.op_br.is_visible_clicks(locator=muen_int, way='css')
        pass

    def seller_info_number(self):
        # 读取info的数据并把int数据切割
        info_text = self.op_br.is_visible_singles("div.dataTables_info", 'css')

        if info_text:
            info_text = str.split(info_text.text, '，')[-1]
            searchObj = re.search("\d+", info_text)
            info_text = int(searchObj.group() if searchObj else searchObj)
            if (info_text % 6) > 0:
                number = 1
            else:
                number = 0
            info_text = int((info_text / 6)) + number
        return info_text

    def searchlist_verify(self, subs_int):
        # 进入指定的tab
        self.op_br.is_visible_clicks('div.subsearch>a:nth-child(%s)' % subs_int, 'css')
        # 1.判断是否有数据
        show_data = self.op_br.is_visible_singles("div.shownodata", "css")
        assert not show_data, "该页面没有数据需人工手动点击:%s" % show_data
        pass

    def subscribe_jump(self, subs_int):
        # 进入指定的tab并判断页面是否有数据
        self.searchlist_verify(subs_int)

        # 判断翻页的数据长度
        info_text = self.seller_info_number()
        for info in range(info_text):
            # 获取全部数据
            search_list = self.op_br.is_visible_all_drivers("div.searchlist", "css")
            # 遍历获取数据
            for search in search_list:
                # 读取该数据中转预约按钮
                search_attr = search.find_element_by_css_selector("div.row>div:nth-child(2)>span", "css")
                # 获取转预约按钮的属性值
                search_attr_text = search_attr.get_attribute('class')
                # 判断转预约按钮的状态
                if 'delivery-make' == search_attr_text:
                    # 点击转预约按钮
                    search_attr.click()
                    # 获取弹窗标题文字
                    label_title = self.op_br.get_ele_text_vlue("myModalLabel", "id")
                    # 点击关闭弹窗
                    self.op_br.is_visible_clicks("div.modal-header > button > span", 'css')
                    # 比较弹窗标题文字是否正确
                    assert "转预约" == label_title, "点击转预约按钮之后,弹窗标题显示有误:%s" % label_title
                    break

            # 没有点击转预约进行跳转时,进入下一个页面
            li_active = self.op_br.is_visible_singles("ul.pagination>li:nth-child(-1)", "css")
            li_active_text = li_active.get_attribute('class')
            if 'active' in li_active_text:
                break
            else:
                li_active.click()
        pass

    def single_jump(self, subs_int):
        # 进入指定的tab并判断页面是否有数据
        self.searchlist_verify(subs_int)

        # 读取该数据中派单按钮
        self.op_br.is_visible_clicks("div.row>div:nth-child(3)>span", "css")
        # 获取弹窗标题文字
        label_title = self.op_br.get_ele_text_vlue("myModalLabel", "id")
        assert label_title, "该区域没有可派单的人员,点击派单没有弹窗:%s" % label_title

        # 点击关闭弹窗
        self.op_br.is_visible_clicks("close", 'id')

        # 比较弹窗标题文字是否正确
        assert "派单" == label_title, "点击派单按钮之后,弹窗标题显示有误:%s" % label_title
        pass

    def even_more_jump(self, subs_int):
        # 进入指定的tab并判断页面是否有数据
        self.searchlist_verify(subs_int)

        # 读取该数据中更多按钮
        self.op_br.is_visible_clicks("div.row>div:nth-child(4)>a", "css")

        # 获取当前句柄
        current_handles = self.op_br.driver.current_window_handle

        # 获取全部句柄
        all_handles = self.op_br.driver.window_handles

        # 进入新的句柄
        for handles in all_handles:
            if current_handles == handles:
                pass
            else:
                self.op_br.driver.switch_to.window(handles)

        bread_text = self.op_br.get_ele_text_vlue("#breadcrumbs > ul > li", "css")

        # 关闭新打开的浏览器窗口
        self.op_br.driver.close()

        # 进入之前的窗口
        self.op_br.driver.switch_to.window(current_handles)

        # 执行其他任务
        assert '配送明细' == bread_text, "点击更多跳转到新页面之后标题判断有误:%s" % bread_text
        pass
