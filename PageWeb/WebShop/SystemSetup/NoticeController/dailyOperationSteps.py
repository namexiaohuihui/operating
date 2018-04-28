# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: dailyOperationSteps.py
@time: 2018/4/16 10:25
"""
import json
from tools.Logger import Log
import time
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
        # dn = DailyLabelNames()
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
        match = self._verify_match(my_sql) # 返回查询之后的数据信息
        return match

    def oneStorage(self):
        # 执行第一个sql之后所得到的数据集
        storage = self._verify_content(dn.wholeQueryStatement())
        self.pan = PANDASDATA(storage)
        df = self.pan.dataFrame(columns=self.setDailyTitle())
        return df


    # ---------------------------------页面数据获取--------------------------
    def getLableExtend(self, load, td="td"):
        ebs = ExtendBeantifulSoup(self.driver, load, self.setDailyTitle())
        df = ebs.lableParsingList(td).interfaceToPandas()
        return df

    def getAllTitle(self):
        df = self.getLableExtend(dn.lable_thead, "th").iloc[0]
        df = list(df)
        ddf = self.overall[dn.whole_result()]
        ddf = ddf.split(",")
        self._verify_operator(df, ddf)
        pass

    def getAllContent(self):

        # 第一个sql的数据
        df = self.oneStorage()

        # 修改时间和操作
        df = self.defaultModifyTime(df)

        # 获取页面数据
        dfebs = self.extendSoup(df)

        # 比较两个数据是否一致
        dfop = self._verify_operator(df, dfebs)

        # 将读取的数据以及比较的结果保存为一个文档
        self.pan.functionConcat(self.FUNCTION_NAME, df, dfebs, dfop)

    def getAllCity(self):
        # 筛选数据的函数
        # 找到下拉框
        dl = OperationSelector(self.driver,dn.dail_city)
        # 设置数据
        weizhi = self.overall[dn.dailyCity()]
        dl.setSelectorText(weizhi)
        self._visible_css_selectop(dn.dail_button)
        # 获取数据的函数
        self.getAllContent()

    def getAllRelease(self):
        # 筛选数据的函数
        # 找到下拉框
        dl = OperationSelector(self.driver,dn.dail_status)
        # 设置数据
        weizhi = self.overall[dn.dailyTitle()]
        print(weizhi)
        dl.setSelectorText(weizhi)
        self._visible_css_selectop(dn.dail_button)
        # 获取数据的函数
        self.getAllContent()


    def extendSoup(self,df):
        '''
        读取网页的数据并进行转换操作
        :param df:
        :return:
        '''
        ele = self._visible_return_selectop(dn.lable_tbody)
        if ele != False:  # 判断是否出现
            # 读取页面数据
            ebs = ExtendBeantifulSoup(self.driver, dn.lable_tbody, self.setDailyTitle())
            # 判断是否需要翻页读取数据
            self.sizeLen(ebs, len(df.values))

            dfebs = ebs.interfaceToPandas()
            default = dfebs["default"]
            df_dault = []
            for deff in default:
                df_dault.append(deff.replace("\n\n\n", ""))
            dfebs["default"] = df_dault
            return dfebs
        else:
            self.log.info("公告页面的tbody不存在")
            return ele
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
        return df
