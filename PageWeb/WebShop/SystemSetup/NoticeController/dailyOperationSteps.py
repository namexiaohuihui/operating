# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: dailyOperationSteps.py
@time: 2018/4/16 10:25
"""
import inspect

from pandas import DataFrame

from PageWeb.WebShop.SystemSetup.NoticeController import popupWindows
from PageWeb.WebShop.SystemSetup.NoticeController.dailyLabelNames import DailyLabelNames
from PageWeb.WebShop.judgmentVerification import JudgmentVerification
from tools.extendBeantifulSoup import ExtendBeantifulSoup
from tools.openpyxlExcel import PANDASDATA
from tools.operationSelector import OperationSelector
from utils.timeFromat import TimeFromat


class DailyOperationSteps(JudgmentVerification):
    # 修改已停止的公告之后，状态值
    STOP_RELEASE_STATUS = 2
    # 记录提交修改公告的时间
    ANNOUN_SHE_TIME = ''
    global dn
    dn = DailyLabelNames()

    # ----------------------------------文件配置函数-----------------------------------
    def setDailyTitle(self):
        """
        pandas标题的设置
        :return:
        """
        daily = ("type", "city", "title", "content", "time", "status", "default")
        return daily

    def setDailyBulletin(self, basename, case_position):
        """
            定义文件名以及工作薄，方便统一进行修改
        """
        EXCLE_FILE = dn.getDailyBulletin(case_position)
        self.openingProgram(basename, EXCLE_FILE)
        pass

    def _rou_fun(self):
        self._visible_css_selectop(dn.sidebar)
        self._visible_css_selectop(dn.treew)

    def _rou_DailyFun(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self._rou_fun()
        self._visible_css_selectop(dn.tabs_dail)
        pass

    def _rou_MaintenanceFun(self):
        """
        进入维护页面
        :return:  暂时没有返回值
        """
        self._rou_fun()
        self._visible_css_selectop(dn.tabs_maintenance)
        pass

    def _rou_HelpFun(self):
        """
        进入帮助页面
        :return:  暂时没有返回值
        """
        self._rou_fun()
        self._visible_css_selectop(dn.tabs_help)
        pass

    # ---------------------------------数据库模块--------------------------

    def _verify_content(self):
        my_sql = self.overall[dn.wholeQueryStatement()]  # 获取sql语句
        match = self._verify_match(my_sql)  # 返回查询之后的数据信息
        return match

    def setButtonMysql(self):
        # 根据sql查询数据内容
        # 执行第一个sql之后所得到的数据集
        storage = self._verify_content()
        self.pan = PANDASDATA(storage)
        self.MYSQL_DF = self.pan.dataFrame(columns=self.setDailyTitle())

    # ---------------------------------用例/页面数据处理--------------------------
    def getOperaSelect(self):
        # 找到城市下拉框
        dl = OperationSelector(self.driver, dn.dail_city)
        # 设置数据
        weizhi = self.overall[dn.dailyCity()]
        dl.setSelectorText(weizhi)
        self.log.info("下拉选择的数据为 %s " % weizhi)

        # 找到状态下拉框
        dl.setSelectData(dn.dail_status)
        # 设置数据
        weizhi = self.overall[dn.dailyTitle()]
        dl.setSelectorText(weizhi)
        self.log.info("下拉选择的数据为 %s " % weizhi)

        # 搜索按钮
        self._visible_css_selectop(dn.dail_button)

    def getLableExtend(self, load, td="td"):
        '''
        定义获取页面数据对象
        :param load:
        :param td:
        :return:
        '''
        ebs = ExtendBeantifulSoup(self.driver, load, self.setDailyTitle())
        EBS_DF = ebs.lableParsingList(td).interfaceToPandas()
        return EBS_DF

    def getAllTitle(self):
        '''
        获取标签为th的数据信息.
        通过","进行切割然后判断数据信息是否一致
        :return:
        '''
        EBS_DF = self.getLableExtend(dn.lable_thead, "th").iloc[0]
        EBS_DF = list(EBS_DF)
        OVE_DF = self.overall[dn.whole_result()]
        OVE_DF = OVE_DF.split(",")
        # 比较两个数据是否一致
        self._verify_operator_dataframe(EBS_DF, OVE_DF)
        pass

    def judgeAllContent(self):
        if type(self.LABLE_DF) is DataFrame:
            # 比较两个数据是否一致
            dfop = self._verify_operator_dataframe(self.MYSQL_DF, self.LABLE_DF)

        else:
            self.log.info("公告页面的tbody不存在 ----> %s" % inspect.stack()[0][3])

    def getAllScreening(self) -> "不需要转换查询数据":
        # 执行点击按钮之后执行查询语句
        self.setButtonMysql()
        # 获取页面数据
        self.getLableTbodyPage()
        # 数据比较
        self.judgeAllContent()

    def getLableTbodyPage(self):
        '''
        获取标签为lable_tbody的全部数据并进行转换操作
        :return:
        '''
        # 获取页面数据
        self.LABLE_DF = self._visible_css_selectop_text(dn.lable_tbody)
        if self.LABLE_DF is not '':  # 判断是否出现
            # 读取页面数据
            ebs = ExtendBeantifulSoup(self.driver, dn.lable_tbody, self.setDailyTitle())
            # 判断是否需要翻页读取数据
            self.sizeLen(ebs, len(self.MYSQL_DF.values))
            self.LABLE_DF = ebs.interfaceToPandas()

    def submit_data_judgment(self) -> "提交完成之后数据信息判断":
        # 修改时间和操作
        self.default_modify_time()
        # 提交之后的数据跟用例的数据比较情况
        self._verify_operator_dataframe(self.MYSQL_DF.iloc[0], self.LABLE_DF.iloc[0])

    def time_to_list(self):
        print("转换前的数据{}".format(self.LABLE_DF.iloc[0]))
        status_time, status_end = self.ti.cutting_time_current(self.LABLE_DF.iloc[0]['time'])
        # status_time = self.list_add_number(status_time)
        # status_end = self.list_add_number(status_end)
        self.LABLE_DF.iloc[0]["time"] = status_time
        self.LABLE_DF.iloc[0]["default"] = status_end
        print("转换后的数据{}".format(self.LABLE_DF.iloc[0]))

    def submit_conditions(self, operation: "提交按钮", attribute: "公告id") -> "执行提交操作之后根据id查询数据库":
        # 3.1 执行点击操作
        self._visible_css_selectop(operation)
        # 3.2点击之后的返回信息
        _title = self._visible_css_selectop_text(dn.dail_title)
        # 3.3判断信息跟规定中的是否一致
        self._verify_operator(_title, self.overall[dn.whole_verification()])
        # 3.4点击提交按钮
        self._visible_css_selectop(dn.dail_determine)
        # 记录提交的时间
        self.ANNOUN_SHE_TIME = self.ti.currentToStamp()

        # 3.5提交按钮之后，进行数据库查询。将查询的结果返回
        self.sleep_time(2)
        statements_content = " n.id = '%s' " % (self.number_cutting(attribute))
        # 拼接sql
        self.overall[dn.wholeQueryStatement()] = self.overall[dn.wholeQueryStatement()] + statements_content
        # 3.6查询数据库
        self.setButtonMysql()

    def popup_conditions_button(self, operation: "提交按钮", default: "取消按钮", attribute):
        if self.interface_conditions(operation, default, attribute):
            # 数据处理，将界面数据的时间进行修改
            self.time_to_list()
            # 比较数据库的数据
            self.submit_data_judgment()

    def submit_conditions_button(self, operation: "提交按钮", default: "取消按钮", attribute):
        if self.interface_conditions(operation, default, attribute):
            # 比较数据库的数据
            self.submit_data_judgment()

    def interface_conditions(self, operation: "提交按钮", default: "取消按钮", attribute) -> "操作提交之后,提示语的比较":
        """
        判断二次弹窗的操作按钮:两个情况
        1.点击停止或者发布之后出现的弹窗
        2.点击编辑或者点击添加公告出现的弹窗
        :param operation:
        :param default:
        :param attribute:
        :return:
        """
        bl_cond = self.conditions_operation(dn.dailyOperation())
        if bl_cond:
            # 如果为确定按钮，那么就比较二次弹窗的信息
            self.submit_conditions(operation=operation, attribute=attribute)
        else:
            self._visible_css_selectop(default)
        return bl_cond

    def popup_data_obtain(self):
        # 获取公告编辑框中的数据信息
        popupWindows.get_popup_data_obtain(self, dn)

    def lable_button_click(self, bl_button):
        # 用户检查是点击第一个按钮还是第二个
        print("用户检查是点击第一个按钮还是第二个 ---> {}".format(bl_button))
        bl_button = dn.button_one if bl_button else dn.button_two
        # 如果数据存在就先找到需要操作的公告id
        attribute = self._visible_css_selectop_attribute(bl_button, attr="data-url")
        # 并点击该公告
        self._visible_css_selectop(bl_button)
        print("{}------->公告的id数据 ".format(attribute))
        return attribute

    def get_window_data(self):
        # 获取页面数据
        self.LABLE_DF = self._visible_css_selectop_text(dn.lable_tbody)
        if self.LABLE_DF is not '':  # 判断是否出现
            # 读取页面数据对象
            ebs = ExtendBeantifulSoup(self.driver, dn.lable_tbody, self.setDailyTitle())
            # 获取当页的数据信息
            ebs.lableParsingList()
            self.LABLE_DF = ebs.interfaceToPandas()

            return True
        else:
            return None

    def extendSoup(self):
        '''
        将转换的数据进行切割重组
        :param df:
        :return:
        '''
        dfebs = self.getLableTbodyPage()
        if type(dfebs) is DataFrame:  # 判断是否出现
            default = dfebs["default"]
            df_dault = []
            for deff in default:
                df_dault.append(deff.replace("\n\n\n", ""))
            dfebs["default"] = df_dault
        else:
            self.log.info("%s  公告页面的tbody不存在" % inspect.stack()[0][3])

    def sizeLen(self, ebs, size):
        """
        判断是否有翻页数据
        :param ebs:
        :param size:
        :return:
        """
        lenn = int(size / 10)
        ebs.lableParsingList()
        for nnn in range(lenn):
            self._visible_css_selectop(".paginate_button.next > a")
            ebs.lableParsingList()

    # ---------------------------------df数据集修改--------------------------
    def status_time_modify(self, status_time, status_end):
        print(type(status_time), type(status_end))
        status = []
        # 存储状态以及操作按钮
        if self.ANNOUN_SHE_TIME < status_end and self.ANNOUN_SHE_TIME > status_time:  # 大于开始时间小于结束时间
            status.append("发布中")
        if self.ANNOUN_SHE_TIME < status_time:  # 小于开始时间
            status.append("未开始")
        if self.ANNOUN_SHE_TIME > status_end:  # 大于结束时间
            status.append("已过期")
        print("status -------> %s " % status)
        return status

    def default_modify(self, modify):
        status_time = int(modify["time"])
        status_end = int(modify["default"])
        return self.status_time_modify(status_time, status_end)

    def default_modify_time(self):
        # 判断时间给出数据
        status = self.default_modify(self.MYSQL_DF.iloc[0])
        # 赋值
        self.MYSQL_DF["status"] = status

        # 判断时间给出数据
        status = self.default_modify(self.LABLE_DF.iloc[0])
        # 赋值
        self.LABLE_DF.iloc[0]["status"] = status

    def defaultModifyTime(self):
        tf = TimeFromat()
        now = tf.currentToStamp()  # 获取当前时间戳
        status = []  # 存状态
        defaults = []  # 存操作
        times = []  # 存时间
        for code in range(len(self.MYSQL_DF.values)):
            # 获取时间
            statusda = self.MYSQL_DF.iloc[code]
            status_time = statusda["time"]  # 开始时间
            status_end = statusda["default"]  # 结束时间

            # 存储状态以及操作按钮
            if statusda["status"] == 1:
                if now < status_end and now > status_time:  # 大于开始时间小于结束时间
                    status.append("发布中")
                    defaults.append("停止")
                if now < status_time:  # 小于开始时间
                    status.append("未开始")
                    defaults.append("""编辑 停止""")
                if now > status_end:  # 大于结束时间
                    status.append("已过期")
                    defaults.append("编辑")
            else:
                status.append("已停止")
                defaults.append("编辑 发布")

            # 存储时间
            status_time = tf.stampToTime(status_time)
            status_end = tf.stampToTime(status_end)
            times.append(status_time + "-" + status_end)
        # 赋值
        self.MYSQL_DF["status"] = status
        self.MYSQL_DF["default"] = defaults
        self.MYSQL_DF["time"] = times

    # ------------------------------用例多次调用的方法统一起来------------
    def getAllContent(self) -> "选择转换查询数据":
        # 执行点击按钮之后执行查询语句
        self.setButtonMysql()
        # 修改时间和操作
        self.defaultModifyTime()
        # 下拉筛选的选择
        self.getOperaSelect()
        # 获取页面数据:获取页面数据必须在执行sql语句之后。不然有个判断会出错
        self.extendSoup()
        # 　比较操作
        self.judgeAllContent()

    def getAllRelease(self) -> "只获取页面数据然后跟数据库比较":
        # 下拉筛选的选择
        self.getOperaSelect()
        # 剩下的数据获取和比较操作
        self.getAllScreening()

    def poput_to_confirm(self):
        # 2.获取二次确认弹窗的标题和内容
        _title = self._visible_css_selectop_text(dn.dail_title)
        _content = self._visible_css_selectop_text(dn.dail_content)
        title_content = {"title": _title, "content": _content}

        # 2.1获取用例上弹窗的数据信息，并转换成json数据格式
        content = self.strTodict(self.overall[dn.whole_result()])

        # 2.22判断是否一致
        self._verify_operator(title_content, content)

    def popup_title_content(self, bl_button=True) -> "二次确认弹窗的信息比较":
        # 点击停止/发布按钮，弹出二次确认弹窗
        attribute = self.lable_button_click(bl_button)

        # 二次弹窗的标题以及提示消息的判断
        self.poput_to_confirm()

        # 3.获取用户执行的动作,判断是取消提交还是确定提交
        self.popup_conditions_button(dn.dail_determine, dn.dail_cancel, attribute)

    def get_popup_data(self, bl_button):
        # 点击按钮，开始执行 下一步的操作
        attribute = self.lable_button_click(bl_button)

        # 弹窗数据获取以及判断
        self.popup_data_obtain()

        # 对弹窗输入框进行数据输入
        popupWindows.set_popup_all_data(self, dn)

        # 获取用户执行的动作,判断是取消提交还是确定提交
        self.submit_conditions_button(dn.operation_primary, dn.operation_default, attribute)

    # -----------------------------------------用例直接使用--------------------------

    def getAllCity(self) -> "获取城市内容":
        '''
        进入页面，读取数据并进行比对
        :return:
        '''
        # 筛选数据的函数
        self.getOperaSelect()
        # 获取数据的函数
        self.getAllContent()
        pass

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
        # 下拉筛选的选择
        self.getOperaSelect()

        # 获取当前页面上所展示的全部数据。
        attribute = self.get_window_data()
        # 获取编辑框的数据
        self.get_popup_data(bl_button) if attribute is not None else self.log.info("页面数据为空")
        pass

    def get_announcement_release(self) -> "用于公告发布的操作":
        # 点击添加按钮
        self._visible_css_selectop(dn.operation)
        # 信息输入
        popupWindows.release_popup_data(self, dn)
        bl_cond = self.conditions_operation(dn.dailyOperation())
        if bl_cond:
            # 点击提交按钮
            self._visible_css_selectop(dn.operation_primary)
            # 错误提示框的信息比较
            self.poput_to_confirm()
            self.vac.sleep_Rest(3)
            # 弹窗上的确认按钮点击
            self._visible_css_selectop(dn.error_button)
        else:
            self._visible_css_selectop(dn.operation_default)

    def get_time_status(self, expect_value) -> "目前没有使用到这个函数":
        '''
        根据修改时间然后判断状态是否正常
        程序运行完毕之后，根据修改后的状态来判断状态值是否跟期望的一直
        :param expect_value:  修改时间之后，期望该公告的状态
        :return:
        '''
        self.get_overdue_modify()
        assert expect_value == self.MYSQL_DF.iloc[0]['status'], "时间设置不严谨，导致公告期望状态判断出错.用例出现False"
