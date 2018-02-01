# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: JudgmentVerification.py
@time: 2018/1/23 10:18
"""
import inspect
import os
import time

from utils.operation.selenium_input import action_input
from utils.RewriteThread import inherit_thread as th
from utils.browser_establish import browser_confirm
from utils.config import readModel
from utils.operation.selenium_click import action_click
from utils.PymysqlMain import pymysqls
from utils import DefinitionErrors as dError
from utils.OpenpyxlExcel import READEXCEL, PANDASDATA

"""
# ------------------内容参数的比较------------------------
"""
vac = action_click()
vai = action_input()


# 在字符串str查找ing出现的位置.从number下标开始找,返回-1表示找不到
def string_lookup_find(str, ing, number=0):
    nPos = str.find(ing, number)
    if nPos != -1:
        return True
    else:
        return False


"""
#------------------获取浏览器部分------------------------------------
"""


def _browser():
    # 1.创建浏览器所在函数的对象
    bc = browser_confirm.__new__(browser_confirm)

    conf = readModel.establish_con(model="model")
    url = conf.get("wap", "admin_url")

    # 2.调用已经规划好的浏览器函数
    driver = bc.url_opens(url)
    return driver


def get_account_account_password():
    conf = readModel.establish_con(model="model")  # 获取账号密码
    account = conf.get("username", "admin_account")
    password = conf.get("username", "admin_password")
    return account, password


def _route():
    # 点击信息页面
    _visible_css_selectop(".nav-user")
    vai.sleep_Rest()
    # 点击页面中的登录按钮
    _visible_css_selectop(".user-head")


def user_login():
    acc_pa = get_account_account_password()  # 获取登录账号和密码
    sign_user_login(acc_pa[0], acc_pa[1])  # 进行登录


def sign_user_login(account, password):
    """
    不需要点击登录就可以直接进入登陆页面
    :param account:
    :param password:
    :return:
    """
    try:

        vai.name_input(driver, 'username', account)
        vai.name_input(driver, 'password', password)

        _visible_json_click("loginBtn")

    except Exception:
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(function)
        raise


"""
#--------------------读取excel表格数据部分-----------------------------------------
"""


def _excel_Data(filename, SHEETNAME=1):
    """
    从excel表格中获取数据并进行转换
    :param file_path:
    :return:
    """
    # 获取excel路径
    file_path = readModel.establish_con(model="excelmodel").get("excel", filename)

    # 读取相应路径中的数据
    read = READEXCEL(file_path, SHEETNAME=SHEETNAME)

    # 获取case
    whole = read.position_sheet_row_value()

    # 将case中内容的数据读出
    row_col_data = whole[0]

    # 将case中标题的内容读出
    title_data = whole[1]

    # 获取case中某个指定key的内容读出
    columnLabel = read.die_angegebene_keys(row_col_data=row_col_data, title_data=title_data)

    # 数据转换
    pan = PANDASDATA(row_col_data)

    df = pan.dataFrame(columns=title_data)  # 设置标题名

    excelData = df.set_index([columnLabel])  # 设置df数据中的序列号

    return excelData


"""
#--------------------元素判断部分-----------------------------------------
"""


def _visible_return_selectop(locator, timeout=5):
    # 判断元素是否存在，如果存在就进行点击并返回对象
    vac.return_css_click(driver, locator)


def _visible_css_selectop(locator, timeout=5):
    # 判断元素是否存在，如果存在就进行点击并返回对象
    vac.css_click(driver, locator)


def _visible_css_selectop_text(locator):
    # 判断元素是否存在，如果存在就进行获取元素的text属性
    _text = vai._visible_selectop_text(driver, locator)
    return _text


def _visible_css_selectop_attribute(locator):
    # 判断元素是否存在，如果存在就获取元素的value属性内容
    vai._visible_selectop_attribute(driver, locator)


def _sendKeys_css_selectop(locator, content):
    # 判断元素是否存在，如果存在就进行输入
    vai.css_input(driver, locator, content)


def _visible_json_click(locator):
    vac.id_confirm_prompt(driver, locator)


def _visible_json_input(ordinal, parameter):
    vai.id_js_input(driver, ordinal, parameter)


"""
# 数据库查询及内容返回
"""


def mysql_selects(sql):
    pm = pymysqls()

    pm.connects_readModel()
    result = pm.single_selects(sql)
    pm.closes()

    return result


"""
#--------------------其他一些配置部分-----------------------------------------
"""


def error_log(function):
    # 执行文件的文件名
    basename = os.path.splitext(os.path.basename(__file__))[0]

    # 拼接名字
    name_tion = basename + "_" + function

    # 调用错误类
    dError.error_output(name_tion, driver)


def _start_thread_pool(funktion):  # 开启线程池
    # funktion = [ap._excel_Data, get_basename]  # 该列表存放需要执行的函数
    print("Opening thread execution %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    faden = []  # 该列表存放已经开启的线程

    inhalt = []  # 该列表存放线程中所执行的函数返回值内容

    for para in funktion:  # 遍历函数开启线程
        threads = th(para)
        faden.append(threads)
        threads.start()

    for argu in faden:  # 开启的线程中，进行阻塞，当子线程完成之后才继续下一步
        argu.join()
        inhalt.append(argu.get_result())

    # overall_ExcelData = inhalt[0]  # df转换的数据，方便对excel进行操作r
    print("Thread execution finished %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    return inhalt
