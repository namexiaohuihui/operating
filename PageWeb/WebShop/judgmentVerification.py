# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: JudgmentVerification.py
@time: 2018/1/23 10:18
"""
import os
import re

from tools.Logger import Log
from tools.openpyxlExcel import OpenExcelPandas
from utils.comparedVerify import ComparedVerify
from utils.config import readModel


class JudgmentVerification(ComparedVerify):
    # 10待付款
    STATUS_TEN = 10
    # 20已关闭
    STATUS_TWENTY = 20
    # 30付款中
    STATUS_THIRTY = 30
    # 32付款成功
    STATUS_TEN_TWO = 32
    # 50待发货
    STATUS_FIFTY = 50
    # 60发货中
    STATUS_SIXTY = 60
    # 70已收货
    STATUS_SEVENTY = 70

    # 平台
    TYPE_ONE = 1
    # 抢购
    TYPE_TWO = 2
    # 平台水票
    TYPE_THREE = 3
    # 店铺
    TYPE_FOUR = 4
    # 店铺水票
    TYPE_FIVE = 5
    # 线下
    TYPE_SIX = 6

    def setFunctionName(self, funtion):
        """
        设置需要运行的函数名
        :param funtion:  函数名
        :return:
        """
        # 记录目前执行的函数名（也可以认为目前执行的用例）
        self.FUNCTION_NAME = funtion
        self.log.functionName(self.FUNCTION_NAME)
        # 根据df标签序号获取用例
        self.overall = self.overallExcelData.loc[self.FUNCTION_NAME]
        self.ti = TimeFromat()

    # --------------------------------正则的使用--------------------------
    def re_cutting_data(self, attr):
        cutting = re.search(r'[1-9]\d{5}(?!\d)', attr)
        return cutting.group()

    # ------------------------数据比较-----------------------------

    def case_time_assert(self, announ_deadline, whole_result):

        # 指定key值获取pandas用例上相应的数据信息
        excel_time = self.overall[announ_deadline]
        assert excel_time != None, "%s get_time_status 没有设置时间" % self.FUNCTION_NAME
        # 记录当前时间
        self.ANNOUN_SHE_TIME = self.ti.currentToStamp()
        # 将时间进行切割，分成开始开始时间和结束时间
        sttus, enmd = self.ti.cutting_time_current(excel_time)
        # 判断时间用例时间
        status_type = self.judge_time_only(status_time=sttus, status_end=enmd)
        # 用例期望的状态
        whole_result = self.overall[whole_result]
        assert status_type == whole_result, "%s根据时间来判断状态出错 %s %s" % (self.FUNCTION_NAME, status_type, whole_result)

    def conditions_operation(self, operation):
        # 按钮判断在这里控制
        # 3.获取用户执行的动作
        _operation = self.overall[operation]  # 获取操作按钮
        if _operation == "确定":
            self.log.info("操作按钮为-->确定吗? %s " % _operation)
            return True
        else:
            self.log.info("操作按钮为-->取消吗? %s " % _operation)
            return False

    # ---------------------------------sql的使用部分-------------------------------
    def mysql_match(self, my_sql: "mysql语句") -> "正则切割sql语句是否为查询语句":
        return re.match('^SELECT', my_sql)

    def _verify_match(self, my_sql):
        '''
        数据库查询
        :param my_sql:  sql语句
        :return:  返回查询到的数据集，没查到数据时返回None
        '''
        regular = self.mysql_match(my_sql)
        if regular:
            # 读取数据库内容
            print("msql--->%s" % my_sql)
            result = self.mysqlTotalSelects(my_sql)
            return result
        return None

    # def _verify_single_match(self, my_sql):
    #     '''
    #     数据库查询
    #     :param my_sql:  sql语句
    #     :return:  返回查询到的数据集，没查到数据时返回None
    #     '''
    #     regular = self.mysql_match(my_sql)
    #     if regular:
    #         # 读取数据库内容
    #         result = self.mysql_single_selects(my_sql)
    #         return result
    #     return None

    """
    #------------------创建浏览器并执行登录------------------------------------
    """

    def option_browser(self):
        # 调用自定义的浏览器接口
        self.driver = self._browser(option="admin_url")

    def openingProgram(self, basename, exclefile):
        """
        定义log日志文件以及读取用例数据
        :param basename:  执行用例的文件名
        :param exclefile:  需要读取用例的文件名
        :return:  暂时没有返回值
        """
        # 这两个比较耗时间
        self.option_browser()  # 打开浏览器
        self.ps_user_login()  # 用户登录

        # 定义日志
        self.log = Log(basename)
        # 读取文档信息,MODEI_KEY_POSITION位于SystenSerup的init，
        # MODEI_CASE_POSITION位于NoticeController的init
        self.overallExcelData = self._excel_Data(self.MODEI_KEY_POSITION, self.MODEI_CASE_POSITION, exclefile)

        pass

    def _excel_Data(self, model_key, filename, SHEETNAME):

        # 获取excel路径
        conmodel = readModel.establish_con(model="excelmodel")
        consyst = conmodel.get("excel", model_key)
        excelname = conmodel.get("excel", filename)
        file_path = os.path.join(consyst, excelname)
        # 读取相应路径中的数据
        read = OpenExcelPandas(file_path, sheet=SHEETNAME)
        # 之前是用readCaseExcel这个函数但是感觉时代要变化就用了internal_read_excel
        # excelData = read.readCaseExcel()
        excelData = read.internal_read_excel()
        return excelData

    def get_account_account_password(self):
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "admin_account")
        password = conf.get("username", "admin_password")
        return account, password

    def ps_user_login(self):
        acc_pa = self.get_account_account_password()  # 获取登录账号和密码
        self.sign_user_login(acc_pa[0], acc_pa[1])  # 进行登录
        pass

    def sign_user_login(self, account, password):
        """
        不需要点击登录就可以直接进入登陆页面
        :param account:
        :param password:
        :return:
        """
        self.vai.name_input(self.driver, 'username', account)
        self.vai.name_input(self.driver, 'password', password)

        self._visible_json_click("loginBtn")
        pass

    # -----------------------输入项--------------------------------------
    def confirmInput(self, caseTitle, eleInformation):
        """获取用例数据之后并进行输入操作"""
        title = self.overall[caseTitle]  # 根据用例title来读取数据

        information = self._verify_parameter(title)  # 判断数据是否为None，如果是就返回一个空值‘’

        print("输入的内容: %s 输入的对象: %s 输入的地方: %s " % (information, eleInformation, caseTitle))
        self._visible_json_input(eleInformation, information)  # 通过元素id利用json进行输入输入

    # -----------------------城市编码和那么的获取---------------------
    def default_city_content(self, city_ele, result):
        '''默认进来页面是否为产品规定的'''
        for city in city_ele:
            if city.get_attribute('class') == 'active':
                self._verify_operator(city.text, self.overall[result])
                break

    def lable_code_name(self, city_ele, tag, bute) -> dict:
        '''
        获取城市标签中，全部的code和bane
        :param city_ele:  城市标签元素
        :param tag:  元素携带的标签
        :param bute: 子元素携带的标签
        :return: code为key，name为value的数据集
        '''
        LABLE_DF = {}
        for number in range(1, len(city_ele)):
            element = self._visible_returan_tag_name(city_ele[number], tag, 5)
            code = self.re_cutting_data(element.get_attribute(bute))
            LABLE_DF[code] = element.text
        return LABLE_DF

    def mysql_code_name(self, content) -> dict:
        '''
        根据sql语句查询数据，将数据根据code为key，name为value的原则重新排版
        :param content: sql语句
        :return: code为key，name为value的数据集
        '''
        MYSQL_DF = self._verify_match(content)
        mysql_df = {}
        for mysql in MYSQL_DF:
            mysql_df[str(mysql['city'])] = mysql['name']
        return mysql_df

    def mysql_area_name(self, content, option):
        MYSQL_DF = self._verify_match(content)
        # mysql_df = [(value for value in mysql.values()) for mysql in MYSQL_DF]
        mysql_df = [option]
        for mysql in MYSQL_DF:
            for value in mysql.values():
                mysql_df.append(value)
        return mysql_df

    def items_status_judge(self, item_status):

        if item_status == self.STATUS_TEN:
            item_status = "等待付款"
            operation = "查看|关闭|操作记录"

        elif item_status == self.STATUS_TWENTY:
            item_status = "交易关闭"
            operation = "查看|操作记录"

        elif item_status == self.STATUS_THIRTY:
            item_status = "付款中"
            operation = "查看|关闭|操作记录"

        elif item_status == self.STATUS_TEN_TWO:
            item_status = "等待派单"
            operation = "派单|查看|关闭|操作记录"

        elif item_status == self.STATUS_FIFTY:
            # 订单为预约时，就不需要出现转预约的按钮
            item_status = "等待配送"
            operation = "更换配送员|转预约|查看|关闭|操作记录"

        elif item_status == self.STATUS_SIXTY:
            # 订单为预约时，就不需要出现转预约的按钮
            item_status = "配送中"
            operation = "转预约|查看|关闭|操作记录"

        elif item_status == self.STATUS_SEVENTY:
            item_status = "交易完成"
            operation = "查看|操作记录"

        return item_status, operation

    def items_type_judge(self, item_type):
        # if item_type == self.TYPE_ONE:
        #     item_type = "平台"

        if item_type == self.TYPE_TWO:
            item_type = "抢购"

        # elif item_type == self.TYPE_THREE:
        #     item_type = "水票"

        # elif item_type == self.TYPE_FOUR:
        #     item_type = "店铺"

        # elif item_type == self.TYPE_FIVE:
        #     item_type = "店铺水票"

        elif item_type == self.TYPE_SIX:
            item_type = "线下"

        return item_type


if __name__ == '__main__':
    str_mysql = '''SELECT
	o.id,o.type,o.arrive_time,o.communicate,o.large_quantity,
	b.nickname,
	ora.contact,
	ora.address,
	ora.house_number,
	ca.`name`,
	o.`status`,
	o.add_time
FROM
	lnsm_order AS o
LEFT JOIN lnsm_buyer AS b ON b.buyer_id = o.buyer_id
LEFT JOIN lnsm_order_receive_addr AS ora ON ora.order_id = o.id
LEFT JOIN lnsm_custom_area AS ca ON ora.custom_area_id = ca.id
LEFT JOIN lnsm_custom_area_staff AS cas2 ON ora.custom_area_id = cas2.custom_area_id
AND cas2.job_level = 2
AND cas2.`status` = 1
WHERE
	o.add_time BETWEEN 1528300800
			AND 1528385039
AND (
	o.type IN (1, 2, 3, 6)
)
GROUP BY
	o.id
ORDER BY
	o.id DESC;
    '''
    import pprint
    from utils.timeFromat import TimeFromat

    jvf = JudgmentVerification()
    mysql_jieguo = jvf._verify_match(str_mysql)
    pprint.pprint(mysql_jieguo)

    # 　开始转换内容
    mysql_df = {}
    mysql_title = ["#订单编号", "订单标签", "买家名称", "收货地址", "所属区域", "状态", "下单时间", "操作"]
    items = 0
    # 订单编号
    mysql_df[mysql_title[0]] = mysql_jieguo[items]["id"]

    # 订单标签  店铺\平台 抢购  线下  调度(调度可以忽略吧)  预约  大客户  新用户
    """
    arrive_time 预约时间
communicate 新用户
large_quantity 大客户
type 1配送点商品订单 2配送点秒杀订单 3配送点水票支付订单 4普通店铺商品订单 5普通店铺水票支付订单 6线下订单'
    """
    judge_type = jvf.items_type_judge(mysql_jieguo[items]["type"])
    arrive_time = 0 if mysql_jieguo[items]["arrive_time"] == 0 else "预约"
    large_quantity = 1 if mysql_jieguo[items]["large_quantity"] == 1 else "大客户"
    communicate = 1 if mysql_jieguo[items]["communicate"] == 1 else "新用户"

    if type(judge_type) is str:
        mysql_df[mysql_title[1]] = "|%s" % (judge_type)

    if type(arrive_time) is str:
        mysql_df[mysql_title[1]] = "|%s" % (arrive_time)

    if type(large_quantity) is str:
        mysql_df[mysql_title[1]] = "|%s" % (large_quantity)

    if type(communicate) is str:
        mysql_df[mysql_title[1]] = "|%s" % (communicate)
    else:
        mysql_df[mysql_title[1]] = "666666666"

    # 买家名称
    mysql_df[mysql_title[2]] = mysql_jieguo[items]["nickname"]

    # 收货地址
    house_number = mysql_jieguo[items]["house_number"].replace("|", '')
    mysql_df[mysql_title[3]] ="%s,%s%s" % (mysql_jieguo[items]["contact"],mysql_jieguo[items]["address"],house_number)

    # 所属区域
    mysql_df[mysql_title[4]] = mysql_jieguo[items]["name"]

    # 状态 以及 操作
    items_status = mysql_jieguo[items]["status"]
    mysql_df[mysql_title[5]], mysql_df[mysql_title[7]] = jvf.items_status_judge(items_status)

    # 下单时间
    tm_format = "%Y-%m-%d %H:%M"
    mysql_df[mysql_title[6]] = TimeFromat().stampToTime(mysql_jieguo[items]["add_time"], tm_format)

    pprint.pprint(mysql_df)

    import pandas as pd

    df = pd.DataFrame(mysql_df, index=range(1), columns=mysql_title)
    print(df)
    df.to_excel("nihao.xlsx")

