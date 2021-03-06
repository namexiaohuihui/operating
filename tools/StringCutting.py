# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: stringCutting.py
@time: 2017/7/10 21:03
@项目名称:operating
"""

import re


# 切割字符：strr字符，op指定切割的元素，num切割的数量，ber获取的数量
def specified_ber_num(strr, op, num, ber):
    strr = str.split(strr, op, num)[ber]
    return strr


def specified_cut_ber(strr, op=',', ber: int = 0):
    strr = str.split(str(strr), op)[ber]
    return strr


def specified_cut_num(strr, op, num):
    strr = str.split(strr, op, num)
    return strr


def specified_cut(strr, op=','):
    strr = str.split(strr, op)
    return strr


# 去除右边的空格:rstrip
def spaces_right(str):
    str = str.rstrip()
    return str


# 去除左边的空格
def spaces_left(str):
    str = str.lstrip()
    return str


# 去除两边的空格
def spaces_sides(strr):
    strr = str.strip(strr)
    return strr


# 用指定的字符代替现有的字符
def spaces_replace(strr, op=' ', oa=''):
    strr = strr.replace(op, oa)
    return strr


# 指定位置进行切割数据,str数据，num开始位置，ber结束位置
def string_cutting(str, num=0, ber=0):
    if ber == 0:
        ber = len(str)
    str = str[num:ber]
    return str


# 在字符串str查找ing出现的位置.从number下标开始找,返回-1表示找不到
def string_search_number(str, ing, number=0):
    nPos = str.find(ing, number)
    if nPos != -1:
        return True
    else:
        return False


# 在字符串str查找ing出现的位置.找不到时就抛出异常
def string_lookup_index(whole, local):
    try:
        nPos = whole.index(local)
        return nPos
    except Exception as orr:
        return -1


# 大小写转换。输入大于0转换成大写，反之小写
def transformation_upper_lower(str, bl):
    if bl >= 0:
        str = str.upper()
    else:
        str = str.lower()
    return str


# 在str中追加ing内容。n为追加的长度
def additional_len(str, ing, n=0):
    if n == 0:
        n = len(ing)
    str += ing[0:n]
    return str


# str中将n之前的数据替换成ch，m为需要多少个ch
def replace_specified(str, ch, n=0, m=1):
    str = n * ch + str[m:]
    return str


# 翻转字符串
def string_flip(str):
    str = str[::-1]
    return str


# 在str数组中将ing的进行替换
def string_join(str, ing):
    str = ing.join(str)
    return str


# 将s中的字符和数字在fomart中出现过的全部筛选出
def OnlyCharNum(s):
    s2 = s.lower()
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c, '')
    return s


# len：返回字符串、列表、字典、元组等长度
# 参数:要计算的字符串、列表、字典、元组等
# list() 函数是对象迭代器，把对象转为一个列表。返回的变量类型为列表。
def thleng(str):
    kk = len(str)
    return kk


# range(x):表示从0到x，不包括x
# range() 函数返回的是一个可迭代对象（类型是对象），
# 而不是列表类型， 所以打印的时候不会打印列表。
# 2.x版本的就返回0到x之间的全部数据。
# 3.x版本的就返回指定需要的数据，比如range（x）之后返回range(0, x)
def range_range(msg=0, para=99):
    range(msg, para)


# 传入需要提取的参数。正则将非数字的其他字符全部替换。然后将替换之后的数字返回
def extract_number(visible, extract=""):
    matchObj = re.sub("\D", "", visible)
    return matchObj


# 退出时来个提示,一般主程序中使用此退出.
def sys_information(msg):
    sys.exit(msg)


# sys.exit(n) 退出程序引发SystemExit异常
def sys_direct():
    sys.exit(0)


# os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出.
def os_direct():
    os._exit(0)


def regular(str_text: str, pattern='^select') -> bool:
    '''
    re.match只匹配字符串的开始是否为符合的
    :param str_text:  需要匹配的字符
    :return:  返回结果，找到返回真，没找到返回假
    '''
    regular = re.match(pattern, str_text)
    if regular != None:
        return True
    else:
        return False


def re_zip_code(str_text: str, pattern="[1-9]\d{5}(?!\d)"):
    '''
    re.search匹配整个字符串，直到找到一个匹配
    :param str_text: 需要匹配的字符
    :return:
    '''
    searchObj = re.search(pattern, str_text)
    # searchObj = re.findall(pattern,str_text)
    # re_span = searchObj.span()  # 返回已查到的数据信息所在位置
    # searchObj = searchObj.group()  # 返回已查到的数据信息
    return searchObj.group() if searchObj else searchObj


def parsing_action(action):
    # 根据分号区分要执行的步骤,根据星号切割数据
    content_list = action.split(';')
    content_action = {}
    for content in range(len(content_list)):
        content_action[content] = content_list[content].replace('\n', '').split('****')[-1]
        pass

    content_list = {}
    # 根据关键字切分动作
    for action in range(len(content_action)):

        content = content_action[action]
        if content:

            content_split = content.split(',')
            input_action = content_split[0].split('-')[0]
            input_element = content_split[0].split('-')[-1]

            if len(content_split) > 1:
                input_content = content_split[-1].split('-')[-1]
            else:
                input_content = ''

            action_list = {'ele': input_element, 'content': input_content, 'action': input_action}

            # 整合数据并执行储存操作
            content_list[action] = action_list

            # 清空内容以防万一
            del action_list

        else:
            print('内容为空')
    return content_list