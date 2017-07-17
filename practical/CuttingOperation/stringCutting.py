# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: stringCutting.py
@time: 2017/7/10 21:03
@项目名称:operating
"""


# 切割字符：str字符，op指定切割的元素，num切割的数量，ber获取的数量
def specified_cut(str, op, num, ber):
    string = str.split(op, num)[ber]
    return string;


def specified_cut(str, op, num):
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


# Replaces the default substitution space by the specified string
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

#将s中的字符和数字筛选出
def OnlyCharNum(s):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;


