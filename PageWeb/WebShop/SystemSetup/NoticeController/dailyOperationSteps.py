# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: dailyOperationSteps.py
@time: 2018/4/16 10:25
"""
import json
from tools.Logger import Log
import time
from pandas import DataFrame
from utils.timeFromat import TimeFromat
from tools.openpyxlExcel import PANDASDATA
from tools.extendBeantifulSoup import ExtendBeantifulSoup
from PageWeb.WebShop.judgmentVerification import JudgmentVerification
from PageWeb.WebShop.SystemSetup.NoticeController.dailyLabelNames import DailyLabelNames
from tools.operationSelector import OperationSelector


class DailyOperationSteps(JudgmentVerification):
    global dn
    dn = DailyLabelNames()

    # ----------------------------------文件配置函数-----------------------------------
    def setDailyTitle(self):
        """
        pandas标题的设置
        :return:
        """
        daily = ["type", "city", "title", "content", "time", "status", "default"]
        return daily

    def setDailyBulletin(self, basename):
        """
            定义文件名以及工作薄，方便统一进行修改
        """
        EXCLE_FILE = dn.getDailyBulletin()
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

    def _verify_content(self, whole):
        my_sql = self.overall[whole]  # 获取sql语句
        match = self._verify_match(my_sql)  # 返回查询之后的数据信息
        return match

    def oneStorage(self):
        # 执行第一个sql之后所得到的数据集
        storage = self._verify_content(dn.wholeQueryStatement())
        self.pan = PANDASDATA(storage)
        df = self.pan.dataFrame(columns=self.setDailyTitle())
        return df

    def setButtonMysql(self):
        # 根据sql查询数据内容
        df = self.oneStorage()
        return df

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
        df = ebs.lableParsingList(td).interfaceToPandas()
        return df

    def getAllTitle(self):
        '''
        获取标签为th的数据信息
        :return:
        '''
        df = self.getLableExtend(dn.lable_thead, "th").iloc[0]
        df = list(df)
        ddf = self.overall[dn.whole_result()]
        ddf = ddf.split(",")
        self._verify_operator(df, ddf)
        pass

    def judgeAllContent(self,df,dfebs):
        if type(dfebs) is DataFrame:
            # 比较两个数据是否一致
            dfop = self._verify_operator(df, dfebs)

            # 将读取的数据以及比较的结果保存为一个文档
            self.pan.functionConcat(self.FUNCTION_NAME, df, dfebs, dfop)

        else:
            self.log.info("getAllTitle + 公告页面的tbody不存在")

    def getAllScreening(self)->"不需要转换查询数据":
        # 执行点击按钮之后执行查询语句
        df = self.setButtonMysql()
        # 获取页面数据
        dfebs = self.getLableTbodyPage(df)
        # 数据比较
        self.judgeAllContent(df, dfebs)

    def getAllContent(self)->"选择转换查询数据":
        # 执行点击按钮之后执行查询语句
        df = self.setButtonMysql()
        # 修改时间和操作
        df = self.defaultModifyTime(df)
        # 获取页面数据
        dfebs = self.extendSoup(df)
        #　比较操作
        self.judgeAllContent(df,dfebs)

    def getLableTbodyPage(self,df):
        '''
        获取标签为lable_tbody的全部数据并进行转换操作
        :return:
        '''
        # 获取页面数据
        ele = self._visible_return_selectop(dn.lable_tbody)
        if ele != False:  # 判断是否出现
            # 读取页面数据
            ebs = ExtendBeantifulSoup(self.driver, dn.lable_tbody, self.setDailyTitle())
            # 判断是否需要翻页读取数据
            self.sizeLen(ebs, len(df.values))
            dfebs = ebs.interfaceToPandas()
            return dfebs
        else:
            self.log.info("getLableTbodyPage + 公告页面的tbody不存在")
            return ele

    def extendSoup(self, df):
        '''
        将转换的数据进行切割重组
        :param df:
        :return:
        '''
        dfebs = self.getLableTbodyPage(df)
        if type(dfebs) is DataFrame:  # 判断是否出现
            default = dfebs["default"]
            df_dault = []
            for deff in default:
                df_dault.append(deff.replace("\n\n\n", ""))
            dfebs["default"] = df_dault
            return dfebs
        else:
            self.log.info("extendSoup + 公告页面的tbody不存在")
            return dfebs

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

    def defaultModifyTime(self, df):
        tf = TimeFromat()
        now = tf.currentToStamp()  # 获取当前时间戳
        status = []  # 存状态
        defaults = []  # 存操作
        times = []  # 存时间
        for code in range(len(df.values)):
            # 获取时间
            statusda = df.iloc[code]
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
        df["status"] = status
        df["default"] = defaults
        df["time"] = times

        """
        weizhi = self.overall[dn.dailyTitle()]
        df = df[df['status'].isin([weizhi])]
        """

        return df

    #-----------------------------------------用例直接使用-----------------

    def getAllCity(self)->"获取城市内容":
        # 筛选数据的函数
        self.getOperaSelect()
        # 获取数据的函数
        self.getAllContent()
        pass


    def getAllRelease(self):

        # 下拉筛选的选择
        self.getOperaSelect()

        # 剩下的数据获取和比较操作
        self.getAllScreening()
        pass

    def getStopRelease(self):
        # 下拉筛选的选择
        self.getOperaSelect()

        tbody = self._visible_return_selectop(dn.lable_tbody )
        tbody_tr = tbody.find_elements_by_tag_name("tr")
        if len(tbody_tr) > 0 :
            print(tbody_tr[0].text)
            tbody_tr = tbody_tr[0].find_elements_by_tag_name("td")
            print(tbody_tr[len(tbody_tr) -1 ].text)
            # tbody_tr[len(tbody_tr) - 1].click()
            tbody_tr[len(tbody_tr) -1].find_element_by_css_selector(".btn.btn-default.btn-sm.confirm-btn").click()