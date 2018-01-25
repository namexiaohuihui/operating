# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: ap.py
@time: 2018/1/4 22:13
@项目名称:operating
"""
import inspect
import os

from practical.operation.selenium_input import action_input as vai
from practical.utils.RewriteThread import inherit_thread as th
from practical.utils.browser_establish import browser_confirm
from practical.utils.config import readModel
from practical.utils.operation.selenium_click import action_click as vac

from PageWeb.WebEven.ConversionStorage import conversionstorage
from utils import DefinitionErrors as dError

"""
# ------------------内容参数的比较------------------------
"""
# 定义浏览器对象，方便进行使用
driver = 1


# 在字符串str查找ing出现的位置.从number下标开始找,返回-1表示找不到
def string_lookup_find(str, ing, number=0):
    nPos = str.find(ing, number)
    if nPos != -1:
        return True
    else:
        return False


def function_content_comparison(*parameter):
    # 单※的数据类型为一个数组
    try:
        assert parameter[0] != parameter[1], parameter[2]
    except:
        print(" %s BEI Einem Vergleich der Fehler" % parameter[2])


def function_content_verification(**parameter):
    # 双※的数据类型为一个列表
    print(parameter, type(parameter))


"""
#------------------获取浏览器部分------------------------------------
"""


def _browser():
    # 1.创建浏览器所在函数的对象
    bc = browser_confirm.__new__(browser_confirm)
    options = bc.mobile_phone_mode()

    conf = readModel.establish_con(model="model")
    url = conf.get("wap", "buyer_url")

    # 2.调用已经规划好的浏览器函数
    driver = bc.url_opens(url, options)
    return driver


"""
#------------------- 用户登录--------------------------------
"""


def get_account_account_password():
    conf = readModel.establish_con(model="model")  # 获取账号密码
    account = conf.get("username", "buyer_account")
    password = conf.get("username", "buyer_password")
    return account, password


def _route():
    # 点击信息页面
    _visible_css_selectop(".nav-user")
    vai.sleep_Rest()
    # 点击页面中的登录按钮
    _visible_css_selectop(".user-head")


def user_login():
    try:
        acc_pa = get_account_account_password()  # 获取登录账号和密码
        _route()  # 进入登录页面
        sign_user_login(acc_pa[0], acc_pa[1])  # 进行登录
    except Exception:
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(function)
        raise


def sign_switching_logon(account, password):
    """
    点击登陆之后，进行输入账号密码及切换登陆页面的事务
    :param account:
    :param password:
    :return:
    """
    try:
        # 点击登陆按钮
        btn = _visible_css_selectop('.btn>a:nth-child(1)')
        if btn != False:
            sign_user_login(account, password)
        else:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            error_log(function)

    except Exception:
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(function)
        raise


def sign_user_login(account, password):
    """
    不需要点击登录就可以直接进入登陆页面
    :param account:
    :param password:
    :return:
    """
    try:
        # 切换登陆方式：切换到账号密码登录页面
        _visible_css_selectop('.login-type>a:nth-child(1)')

        vai.sleep_Rest()
        # 账号密码的输入
        driver.find_element_by_css_selector("#J_tel").send_keys(account)
        driver.find_element_by_css_selector("#J_pwd").send_keys(password)
        vai.sleep_Rest()
        # 登陆按钮
        _visible_css_selectop(".u-btn.u-btn-morange")
        # 获取登录的提示语
        text = _visible_css_selectop_text('.toast-cont')
        print("登陆提示信息-----> %s " % text)

        # 储存登陆之后的提示
        conversionstorage().set_remarks(text)

    except Exception:
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(function)
        raise


"""
#--------------------添加商品部分-----------------------------------------
"""


def add_goods():
    """
    选择商品并进行点击
    :return:
    """
    _visible_css_selectop('.J_add.shop-goods-add.icon-font.icon-plus-str')
    vai.sleep_Rest(2)


def details_add_goods(account=None, password=None):
    """
    商品详情页点击购买商品
    :return:
    """
    _visible_css_selectop('.add-cart')  # 点击购买按钮，弹出购物车选择页面

    _visible_css_selectop('.buy-tiket-btn.cart')  # 点击加入购物车，将商品正式加入购物车

    print("添加商品的提示-----> %s" % _visible_css_selectop_text('.toast-cont'))  # 错误的原因
    vai.sleep_Rest()
    _visible_css_selectop('.buy.cur')  # 去结算

    sign_switching_logon(account, password)


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
    from utils import READEXCEL, PANDASDATA
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

    df = pan.dataFrame(columns=title_data)

    excelData = df.set_index([columnLabel])  # 设置df数据中的序列号

    return excelData


"""
#--------------------元素判断部分-----------------------------------------
"""


def _visible_css_selectop(locator, timeout=5):
    # 判断元素是否存在，如果存在就进行点击并返回对象
    vac.touchActions_selectop_prompt(driver, locator)


def _visible_css_selectop_text(locator):
    # 判断元素是否存在，如果存在就进行获取元素的text属性
    vai._visible_selectop_text(driver, locator)


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
#--------------------其他一些配置部分-----------------------------------------
"""


def Interface_sliding():
    # 实行上下滑动的效果
    vac.Interface_sliding(driver)

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
