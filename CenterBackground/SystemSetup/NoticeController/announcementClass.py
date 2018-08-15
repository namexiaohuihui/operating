# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: announcementClass.py
@time: 2018/5/22 11:13
"""

from CenterBackground.SystemSetup.NoticeController import popupWindows
from CenterBackground.SystemSetup.NoticeController.dailyLabelNames import DailyLabelNames
from CenterBackground.SystemSetup.NoticeController.dailyOperationSteps import DailyOperationSteps

dn = DailyLabelNames()


class AnnouncementClass(DailyOperationSteps):
    '''
    页面公告的父类。
    将两个不同的公告，内容一致的合并到一起。
    方便一起调用
    '''

    # -----------------------------------------用例直接使用：日常和维护都可以调用--------------------------
    def getAllTitle(self):
        '''
        获取标题显示数据中，标签为th的数据信息.
        通过","进行切割然后判断数据信息是否一致
        :return:
        '''
        # 爬取界面标题数据
        EBS_DF = self.getLableExtend("th").iloc[0]
        # 将爬取的数据转换成list数据类型
        EBS_DF = list(EBS_DF)

        # 读取excle文档标题为【结果】的数据信息
        OVE_DF = self.overall[dn.whole_result()]
        # 将读取到的数据进行切割
        OVE_DF = OVE_DF.split(",")

        # 比较界面爬取的数据以及excle界面读取的数据是否一致
        self.verify_operator(EBS_DF, OVE_DF)
        pass

    # -----------------------------------------用例直接使用只用于日常调用--------------------------

    def getAllContent(self) -> "选择转换查询数据":
        # 执行点击按钮之后执行查询语句
        self.setButtonMysql()

        # 对sql查询之后的数据信息进行二次调整
        self.defaultModifyTime()

        # 下拉筛选的选择
        self.getOperaSelect()
        '''
        # 获取页面数据:获取页面数据必须在执行sql语句之后。
        # 页面上翻页按钮个数的判断是根据读取数据库之后量来进行的
        '''
        self.extendSoup()
        # 　比较操作
        self.judgeAllContent()

    def getAllCity(self) -> "获取城市内容":
        '''
        进入页面，读取数据并进行比对
        :return:
        '''
        # 执行城市和状态下拉筛选框的操作
        self.getOperaSelect()
        # 界面数据获取及比较
        self.getAllContent()
        pass

    def getAllRelease(self) -> "只获取页面数据然后跟数据库比较":
        # 下拉筛选的选择
        self.getOperaSelect()
        # 剩下的数据获取和比较操作
        self.getAllScreening()

    def getStopRelease(self, bl_button=True) -> "点击停止和发布按钮,弹出二次确认框":
        '''
        点击操作按钮，并对弹窗二次对话框的处理
        :param bl_button:  公告操作里面有两个按钮时。需要通过bl_button来判断点击哪一个
        为真时：点击操作里面第一个按钮
        为假时：点击操作里面第二个按钮
        :return:
        '''
        # 下拉筛选的选择
        self.getOperaSelect()
        # 获取当前页面上所展示的全部数据。
        attribute = self.get_window_data()

        # 获取二次弹窗的数据
        self.popup_title_content(bl_button) if attribute is not None else self.log.info("页面数据为空")
        pass

    def get_overdue_modify(self, bl_button=True) -> "点击按钮弹出编辑框":
        '''
        点击操作按钮，并对编辑弹窗进行数据输入以及数据校验
        :param bl_button:公告操作里面有两个按钮时。需要通过bl_button来判断点击哪一个
        为真时：点击操作里面第一个按钮
        为假时：点击操作里面第二个按钮
        :return:
        '''
        self.driver.refresh()
        # 下拉筛选的选择
        self.getOperaSelect()

        # 获取当前页面上所展示的全部数据。
        attribute = self.get_window_data()
        # 获取编辑框的数据
        self.get_popup_data(bl_button) if attribute is not None else self.log.info("页面数据为空")
        pass

    def get_announcement_release(self) -> "用于公告发布的操作":
        self.driver.refresh()
        # 点击添加按钮
        self._visible_css_selectop(dn.operation)
        # 信息输入
        popupWindows.release_popup_all(self, dn)
        # 判断是否为提交按钮
        bl_cond = self.conditions_operation(dn.dailyOperation())
        if bl_cond:
            # 点击提交按钮
            self._visible_css_selectop(dn.operation_primary)
            # 提交之后，前端提示框的信息比较
            self.poput_to_confirm()
            # 提示框中的OK按钮。
            self._visible_css_selectop(dn.error_button)
        else:
            self._visible_css_selectop(dn.operation_default)

    def status_judge_time(self):
        '''
        用于判断公告的有效时间。用例设置的时间符合要求才进行数据编辑
        :param expect_value:  修改时间之后，期望该公告的状态
        :return:
        '''
        self.case_time_assert(dn.announDeadline(), dn.whole_output())
        self.get_overdue_modify()

    def release_judge_time(self):
        '''
        用于判断公告的有效时间。用例设置的时间符合要求才进行数据编辑
        :param expect_value:  修改时间之后，期望该公告的状态
        :return:
        '''
        self.driver.refresh()
        # 检验excle上的时间参数是否符合要求
        self.judge_time_click_button()
        # 信息输入
        popupWindows.release_popup_all(self, dn)
        # 判断是点击添加弹窗上的提交按钮还是取消按钮
        self.judge_conditions_operation()

    def prepare_judge_time(self):
        '''
        用于判断公告的有效时间。用例设置的时间符合要求才进行数据编辑
        :param expect_value:  修改时间之后，期望该公告的状态
        :return:
        '''
        # 检验excle上的时间参数是否符合要求
        self.judge_time_click_button()

        # 添加弹窗里面的信息输入
        popupWindows.no_release_popup_city(self, dn)
        # 判断是点击添加弹窗上的提交按钮还是取消按钮
        self.judge_conditions_operation()

    # -----------------------------------------用例直接使用只用于维护调用--------------------------
    def notice_all_content(self) -> "选择转换查询数据,不需要下拉操作":
        # 执行点击按钮之后执行查询语句
        self.setButtonMysql()
        # 修改时间和操作
        self.defaultModifyTime()
        # 获取页面数据:获取页面数据必须在执行sql语句之后。不然有个判断会出错
        self.extendSoup()
        # 　比较操作
        self.judgeAllContent()
