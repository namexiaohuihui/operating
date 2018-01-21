# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: stringCutting.py
@time: 2017/7/10 21:03
@项目名称:operating
"""


import re

# 切割字符：str字符，op指定切割的元素，num切割的数量，ber获取的数量
def specified_cut_ber(str, op, num, ber):
    string = str.split(op, num)[ber]
    return string;


def specified_cut_num(str, op, num):
    string = str.split(op, num)
    return string;


def specified_cut(str, op):
    string = str.split(op)
    return string;


# 去除右边的空格:rstrip
def spaces_right(str):
    str = str.rstrip()
    return str;


# 去除左边的空格
def spaces_left(str):
    str = str.lstrip()
    return str;


# 去除两边的空格
def spaces_sides(str):
    str = str.strip()
    return str;


# 用指定的字符代替现有的字符
def spaces_replace(str, op=' ', oa=''):
    str = str.replace(op, oa)
    return str;


# 指定位置进行切割数据,str数据，num开始位置，ber结束位置
def string_cutting(str, num=0, ber=0):
    if ber == 0:
        ber =len(str)
    str = str[num:ber]
    return str;


# 在字符串str查找ing出现的位置.从number下标开始找,返回-1表示找不到
def string_lookup_find(str, ing, number=0):
    nPos = str.find(ing, number)
    return nPos;


# 在字符串str查找ing出现的位置.找不到时就抛出异常
def string_lookup_index(whole,local):
    try:
        nPos = whole.index(local)
        return nPos;
    except Exception as orr:
        return -1;

#大小写转换。输入大于0转换成大写，反之小写
def transformation_upper_lower(str,bl):
    if bl >= 0:
        str = str.upper()
    else:
        str = str.lower()
    return str;

#在str中追加ing内容。n为追加的长度
def additional_len(str,ing,n=0):
    if n==0:
        n=len(ing)
    str += ing[0:n]
    return str;

#str中将n之前的数据替换成ch，m为需要多少个ch
def replace_specified(str,ch,n=0,m=1):
    str = n * ch + str[m:]
    return str;

#翻转字符串
def string_flip(str):
    str = str[::-1]
    return str;

#在str数组中将ing的进行替换
def string_join(str,ing):
    str = ing.join(str)
    return str

#将s中的字符和数字在fomart中出现过的全部筛选出
def OnlyCharNum(s):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;


# len：返回字符串、列表、字典、元组等长度
# 参数:要计算的字符串、列表、字典、元组等
# list() 函数是对象迭代器，把对象转为一个列表。返回的变量类型为列表。
def thleng(str):
    kk = len(str)
    return kk;

# range(x):表示从0到x，不包括x
# range() 函数返回的是一个可迭代对象（类型是对象），
# 而不是列表类型， 所以打印的时候不会打印列表。
# 2.x版本的就返回0到x之间的全部数据。
# 3.x版本的就返回指定需要的数据，比如range（x）之后返回range(0, x)
def range_range(msg=0,para=99):
    range(msg,para)

# 传入需要提取的参数。正则将非数字的其他字符全部替换。然后将替换之后的数字返回
def extract_number(visible,extract = ""):
    matchObj = re.sub("\D", "", visible)
    return matchObj;

#退出时来个提示,一般主程序中使用此退出.
def sys_information(msg):
    sys.exit(msg)

#sys.exit(n) 退出程序引发SystemExit异常
def sys_direct():
    sys.exit(0)

# os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出.
def os_direct():
    os._exit(0)

if __name__ == '__main__':
    str = "账号:-----,密码:*****"
    str11 = "什么呢翻就开始登陆功能"
    if str.find(",") and str.find(":") != -1:

        print(str11)
    else:
        print(str)

