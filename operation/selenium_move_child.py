# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_move_child.py
@time: 2017/6/21 22:49
@项目名称:operating_call
这是需要隐藏的元素类，通过鼠标移动之后找出隐藏的元素在通过传入相应的id，name，text，xpath，css就可以执行查找第二个元素了
"""

from operation import selenium_move
from operation import selenium_click
from constant.browser.browser_establish import browser_confirm

global browser
bc = browser_confirm.__new__(browser_confirm)
browser = bc.call_browser()

# 这是参数是用于识别元素路径前面携带的关键字
_id = 'id'
_name = 'name'
_text = 'text'
_xpath = 'xpath'
_css = 'css'

# ---------------------鼠标移动的对象为id，隐藏的对象为其他---------------------------------#
def id_move_id_child(move=None, child=None):
    selenium_move.id_move(move)
    selenium_click.id_click(child)


def id_move_name_child(move=None, child=None):
    selenium_move.id_move(move)
    selenium_click.name_click(child)


def id_move_text_child(move=None, child=None):
    selenium_move.id_move(move)
    selenium_click.text_click(child)


def id_move_xpath_child(move=None, child=None):
    selenium_move.id_move(move)
    selenium_click.xpath_click(child)


def id_move_css_child(move=None, child=None):
    selenium_move.id_move(move)
    selenium_click.css_click(child)


# ---------------------鼠标移动的对象为name，隐藏的对象为其他---------------------------------#
def name_move_id_child(move=None, child=None):
    selenium_move.name_move(move)
    selenium_click.id_click(child)


def name_move_name_child(move=None, child=None):
    selenium_move.name_move(move)
    selenium_click.name_click(child)


def name_move_text_child(move=None, child=None):
    selenium_move.name_move(move)
    selenium_click.text_click(child)


def name_move_xpath_child(move=None, child=None):
    selenium_move.name_move(move)
    selenium_click.xpath_click(child)


def name_move_css_child(move=None, child=None):
    selenium_move.name_move(move)
    selenium_click.css_click(child)


# ---------------------鼠标移动的对象为text，隐藏的对象为其他---------------------------------#
def text_move_id_click(move=None, child=None):
    selenium_move.text_move(move)
    selenium_click.id_click(child)


def text_move_name_click(move=None, child=None):
    selenium_move.text_move(move)
    selenium_click.name_click(child)


def text_move_text_click(move=None, child=None):
    selenium_move.text_move(move)
    selenium_click.text_click(child)


def text_move_xpath_click(move=None, child=None):
    selenium_move.text_move(move)
    selenium_click.xpath_click(child)


def text_move_css_click(move=None, child=None):
    selenium_move.text_move(move)
    selenium_click.css_click(child)


# ---------------------鼠标移动的对象为xpath，隐藏的对象为其他---------------------------------#
def xpath_move_id_click(move=None, child=None):
    selenium_move.xpath_move(move)
    selenium_click.id_click(child)


def xpath_move_name_click(move=None, child=None):
    selenium_move.xpath_move(move)
    selenium_click.name_click(child)


def xpath_move_text_click(move=None, child=None):
    selenium_move.xpath_move(move)
    selenium_click.text_click(child)


def xpath_move_xpath_click(move=None, child=None):
    selenium_move.xpath_move(move)
    selenium_click.xpath_click(child)


def xpath_move_css_click(move=None, child=None):
    selenium_move.xpath_move(move)
    selenium_click.css_click(child)


# ---------------------鼠标移动的对象为css，隐藏的对象为其他---------------------------------#
def css_move_id_click(move=None, child=None):
    selenium_move.css_move(move)
    selenium_click.id_click(child)


def css_move_name_click(move=None, child=None):
    selenium_move.css_move(move)
    selenium_click.name_click(child)


def css_move_text_click(move=None, child=None):
    selenium_move.css_move(move)
    selenium_click.text_click(child)


def css_move_xpath_click(move=None, child=None):
    selenium_move.css_move(move)
    selenium_click.xpath_click(child)


def css_move_css_click(move=None, child=None):
    selenium_move.css_move(move)
    selenium_click.css_click(child)


# ---------------------鼠标移动的对象和隐藏的对象未知，通过前缀进行区分---------------------------------#

def auto_move_child(move=None, child=None):
    # 这些参数是用于存储切割之后的路径
    if move.find(_id) == -1:
        if move.find(_name) == -1:
            if move.find(_text) == -1:
                if move.find(_xpath) == -1:
                    if move.find(_css) == -1:
                        print("悬停寻找父类关键字怎么出问题了,move=%s" % \
                              move)
                    else:
                        move_route = css_character_cutting(move)
                        selenium_move.css_move(move_route)
                        auto_child_number(child)
                else:
                    move_route = xpath_character_cutting(move)
                    selenium_move.xpath_move(move_route)
                    auto_child_number(child)
            else:
                move_route = text_character_cutting(move)
                selenium_move.text_move(move_route)
                auto_child_number(child)
        else:
            move_route = name_character_cutting(move)
            selenium_move.name_move(move_route)
            auto_child_number(child)
    else:
        move_route = id_character_cutting(move)
        selenium_move.id_move(move_route)
        auto_child_number(child)


# 此元素用于判断子元素的路径类型
def auto_child_number(child):
    child_result = None
    if child.find(_id) == -1:
        if child.find(_name) == -1:
            if child.find(_text) == -1:
                if child.find(_xpath) == -1:
                    if child.find(_css) == -1:
                        print("悬停寻找子类关键字怎么出问题了,child=%s" % \
                              child)
                    else:
                        child_result = css_character_cutting(child)
                        selenium_click.css_click(child_result)
                else:
                    child_result = xpath_character_cutting(child)
                    selenium_click.xpath_click(child_result)
            else:
                child_result = text_character_cutting(child)
                selenium_click.text_click(child_result)
        else:
            child_result = name_character_cutting(child)
            selenium_click.name_click(child_result)
    else:
        child_result = id_character_cutting(child)
        selenium_click.id_click(child_result)


# 根据相应的前缀进行切割
def id_character_cutting(_move):
    return _move.find[2:0]


def name_character_cutting(_move):
    return _move.find[4:0]


def text_character_cutting(_move):
    return _move.find[4:0]


def xpath_character_cutting(_move):
    return _move.find[5:0]


def css_character_cutting(_move):
    return _move.find[3:0]
