# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: dailyOperationSteps.py
@time: 2018/4/16 10:25
"""
import inspect

from pandas import DataFrame

from CenterBackground.SystemSetup import SystemCoexistence
from CenterBackground.SystemSetup.NoticeController import popupWindows
from CenterBackground.SystemSetup.NoticeController.dailyLabelNames import DailyLabelNames
from tools.extendBeantifulSoup import ExtendBeantifulSoup
from tools.openpyxlExcel import PANDASDATA
from tools.operationSelector import OperationSelector


dn = DailyLabelNames()
class DailyOperationSteps(SystemCoexistence):
    # 记录提交修改公告的时间
    ANNOUN_SHE_TIME = ''

    # 当前子目录的所在位置
    FATHER_TAGS_LOCATION = "2"

    # 该目录下的用例在modei文件中所属的key值
    MODEI_CASE_POSITION = "dailybulletin"

    # ----------------------------------文件配置函数-----------------------------------

    # BOOL_TITLE_KEY :设置一个参数用于判断当前程序是运行日常还是维护的代码
    def _modify_boolean_key(self, bl_key):
        self.BOOL_TITLE_KEY = bl_key

    def _achieve_boolean_key(self):
        return self.BOOL_TITLE_KEY

    modify_key = property(_achieve_boolean_key, _modify_boolean_key,
                          doc='Notice the setting of the header parameter.')

    def setDailyTitle(self):
        '''
        pandas标题的设置
        modify_key参数是子类里面的一个参数值.
        :return:
        '''
        print("----->%s" % self.modify_key)
        if self.modify_key:
            daily = ("type", "city", "title", "content", "time", "status", "default")
        else:
            daily = ("type", "title", "content", "time", "status", "default")
        return daily


    def _rou_daily_opera(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self._rou_system()
        self._visible_css_selectop(dn.tabs_dail)
        pass

    def _rou_MaintenanceFun(self):
        """
        进入维护页面
        :return:  暂时没有返回值
        """
        self._rou_system()
        self._visible_css_selectop(dn.tabs_maintenance)
        pass

    def _rou_HelpFun(self):
        """
        进入帮助页面
        :return:  暂时没有返回值
        """
        self._rou_system()
        self._visible_css_selectop(dn.tabs_help)
        pass

    # ---------------------------------数据库模块--------------------------

    def _verify_content(self):
        # 获取excle文档中标题为sql的数据信息
        my_sql = self.overall[dn.wholeQueryStatement()]
        match = self._verify_match(my_sql)  # 返回查询之后的数据信息
        return match

    def setButtonMysql(self):
        # 根据sql查询数据内容
        # 执行第一个sql之后所得到的数据集
        storage = self._verify_content()
        self.pan = PANDASDATA(storage)
        self.MYSQL_DF = self.pan.dataFrame(columns=self.setDailyTitle())

    # ---------------------------------用例/页面数据处理--------------------------
    def set_opeasselect(self, dl, text_key):
        # 筛选公告所在城市
        weizhi = self.overall[text_key]
        dl.setSelectorText(weizhi)
        self.log.info("下拉选择的数据为 %s " % weizhi)

    def getOperaSelect(self):
        # 找到城市下拉框
        dl = OperationSelector(self.driver, dn.dail_city)
        # 筛选公告所在城市
        self.set_opeasselect(dl, dn.dailyCity())

        # 筛选公告状态
        dl.setSelectData(dn.dail_status)
        self.set_opeasselect(dl, dn.dailyTitle())

        # 搜索按钮
        self._visible_css_selectop(dn.dail_button)

    def getLableExtend(self, td="td"):
        '''
        定义获取页面数据对象
        :param td: 页面标签
        :return:
        '''
        ebs = ExtendBeantifulSoup(self.driver, dn.lable_thead, self.setDailyTitle())
        EBS_DF = ebs.lableParsingList(td).interfaceToPandas()
        return EBS_DF

    def judgeAllContent(self) -> '用于比较页面数据跟查询之后的数据是否一致,没有返回值':
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

    def interface_return_validation(self, operation: "提交按钮"):
        # 3.1 执行点击操作
        self._visible_css_selectop(operation)
        # 记录提交的时间
        self.ANNOUN_SHE_TIME = self.ti.currentToStamp()
        # 3.2点击之后的返回信息
        _title = self._visible_css_selectop_text(dn.dail_title)
        # 3.3判断信息跟规定中的是否一致
        self._verify_operator(_title, self.overall[dn.whole_verification()])
        # 3.4点击OK确认按钮
        self._visible_css_selectop(dn.dail_determine)

    def submit_conditions(self, operation: "提交按钮", attribute: "公告id") -> "执行提交操作之后根据id查询数据库":
        '''
        执行提交操作，并查询数据库的内容
        :param operation:
        :param attribute:
        :return:
        '''
        # 提交操作之后，判断是否能正常的提交成功
        self.interface_return_validation(operation)

        # 3.5提交按钮之后，进行数据库查询。将查询的结果返回
        self.sleep_time(2)  # 这里不加延迟会出错。。。。和尚的锅
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
    def judge_time_only(self, status_time, status_end):
        print("---------->时间 %s %s" % (type(status_time), type(status_end)))

        # 存储状态以及操作按钮
        if self.ANNOUN_SHE_TIME < status_end and self.ANNOUN_SHE_TIME > status_time:  # 大于开始时间小于结束时间
            status = dn.RELEASE_DAILY_STATUS

        # 小于开始时间
        elif self.ANNOUN_SHE_TIME < status_time:
            status = dn.PREPARE_DAILY_STATUS

        # 大于结束时间
        elif self.ANNOUN_SHE_TIME > status_end:
            status = dn.OVERDUE_DAILY_STATUS

        else:
            status = "时间状态不行呀"
        print("status -------> %s " % status)

        return status

    def status_time_modify(self, status_time, status_end):
        status = []
        status_data = self.judge_time_only(status_time=status_time, status_end=status_end)
        status.append(status_data)
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
        self.LABLE_DF.iloc[0]["status"] = status[0]

    def defaultModifyTime(self):
        '''
        对mysql数据信息进行时间判断，并修改公告的状态以及操作按钮
        :return:
        '''
        now = self.ti.currentToStamp()  # 获取当前时间戳
        status = []  # 存状态
        defaults = []  # 存操作
        times = []  # 存时间
        for code in range(len(self.MYSQL_DF.values)):
            # 获取指定行数的数据信息
            statusda = self.MYSQL_DF.iloc[code]
            status_time = statusda["time"]  # 单条数据中，key为time 的数据
            status_end = statusda["default"]  # 单条数据中，key为default 的数据

            # 判断时间并存储状态以及操作按钮
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
            status_time = self.ti.stampToTime(status_time)
            status_end = self.ti.stampToTime(status_end)
            times.append(status_time + "-" + status_end)
        # 将状态，操作按钮，以及时间重复赋值给sql查询之后的数据。改变其内部数据
        self.MYSQL_DF["status"] = status
        self.MYSQL_DF["default"] = defaults
        self.MYSQL_DF["time"] = times

    # ------------------------------用例多次调用的方法统一起来---------------------------------
    def judge_time_click_button(self):
        '''
        检验excle上的时间参数是否符合要求，
        符合时就点击添加按钮，不符合时就提示用例失败
        :return:
        '''
        # 判断用例设置的时间是否符合该用例的场景
        self.case_time_assert(dn.announDeadline(), dn.whole_output())
        # 点击添加按钮
        self._visible_css_selectop(dn.operation)

    def judge_conditions_operation(self):
        '''
        判断是点击添加弹窗上的提交按钮还是取消按钮。
        提交之后进行mysql数据查询，看是否能查询到该数据信息
        :return:
        '''
        # 判断是否为提交按钮
        bl_cond = self.conditions_operation(dn.dailyOperation())

        if bl_cond:
            # 点击弹窗上的提交按钮,并判断提示信息是否正确
            self.interface_return_validation(dn.operation_primary)

            # 3.5提交按钮之后，进行数据库查询。将查询的结果返回
            # 提交公告之后，不对sql数据信息进行比较
            self.sleep_time(2)  # 这里不加延迟会出错。。。。和尚的锅
            statements_content = " n.title = '%s' and n.content = '%s' " % \
                                 (self.overall[dn.announTitle()], self.overall[dn.announContent()])
            # 拼接sql
            self.overall[dn.wholeQueryStatement()] = self.overall[dn.wholeQueryStatement()] + statements_content
            # 3.6查询数据库
            self.setButtonMysql()
        else:
            self._visible_css_selectop(dn.operation_default)

    def poput_to_confirm(self):
        '''
        _content元素找不到时，说明提示弹窗只有标题没有内容，此时应扑捉
        :return:
        '''
        # 2.获取二次确认弹窗的标题和内容
        _title = self._visible_css_selectop_text(dn.dail_title)
        try:
            _content = self._visible_css_selectop_text(dn.dail_content)
            _title = {"title": _title, "content": _content}
            # 2.1获取用例上弹窗的数据信息，并转换成json数据格式
            _content = self.strTodict(self.overall[dn.whole_result()])
        except Exception as ex:
            _content = self.overall[dn.whole_result()]
            print("弹窗没有内容，只有文字。")

        # 2.22判断是否一致
        self._verify_operator(_title, _content)

    def popup_title_content(self, bl_button=True) -> "二次确认弹窗的信息比较":
        # 点击停止/发布按钮，弹出二次确认弹窗
        attribute = self.lable_button_click(bl_button)

        # 二次弹窗的标题以及提示消息的判断
        self.poput_to_confirm()

        # 3.获取用户执行的动作,判断是取消提交还是确定提交
        self.popup_conditions_button(dn.dail_determine, dn.dail_cancel, attribute)

    def get_popup_data(self, bl_button):
        # 点击操作按钮，开始执行 下一步的操作
        attribute = self.lable_button_click(bl_button)

        # 弹窗数据获取以及判断
        self.popup_data_obtain()

        # 对弹窗输入框进行数据输入
        popupWindows.set_popup_all_data(self, dn)

        # 获取用户执行的动作,判断是取消提交还是确定提交
        self.submit_conditions_button(dn.operation_primary, dn.operation_default, attribute)
