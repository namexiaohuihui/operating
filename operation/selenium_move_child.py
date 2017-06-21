# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_move_child.py
@time: 2017/6/21 22:49
@项目名称:operating_call
这是需要隐藏的元素类，通过鼠标移动之后找出隐藏的元素在通过传入相应的id，name，text，xpath，css就可以执行查找第二个元素了
"""
import os
import time
from selenium.webdriver import ActionChains

from parameter.browser import browser_establish

global browser
browser = browser_establish.browser_using().call_browser()

# 这是参数是用于识别元素路径前面携带的关键字
_id = 'id'
_name = 'name'
_text = 'text'
_xpath = 'xpath'
_css = 'css'


def parameter_move_child(a=0, move=None, child=None):
    try:
        if a == 1:
            #   找到需要转移的元素
            ele = browser.find_element_by_id(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_id(child).click()
        elif a == 2:
            #   找到需要转移的元素
            ele = browser.find_element_by_id(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_name(child).click()
        elif a == 3:
            #   找到需要转移的元素
            ele = browser.find_element_by_id(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_link_text(child).click()
        elif a == 4:
            #   找到需要转移的元素
            ele = browser.find_element_by_id(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_xpath(child).click()
        elif a == 5:
            #   找到需要转移的元素
            ele = browser.find_element_by_id(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_css_selector(child).click()
        elif a == 6:
            #   找到需要转移的元素
            ele = browser.find_element_by_name(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_id(child).click()
        elif a == 7:
            #   找到需要转移的元素
            ele = browser.find_element_by_name(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_name(child).click()
        elif a == 8:
            #   找到需要转移的元素
            ele = browser.find_element_by_name(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_link_text(child).click()
        elif a == 9:
            #   找到需要转移的元素
            ele = browser.find_element_by_name(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_xpath(child).click()
        elif a == 10:
            #   找到需要转移的元素
            ele = browser.find_element_by_name(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_css_selector(child).click()
        elif a == 11:
            #   找到需要转移的元素
            ele = browser.find_element_by_link_text(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_id(child).click()
        elif a == 12:
            #   找到需要转移的元素
            ele = browser.find_element_by_link_text(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_name(child).click()
        elif a == 13:
            #   找到需要转移的元素
            ele = browser.find_element_by_link_text(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_link_text(child).click()
        elif a == 14:
            #   找到需要转移的元素
            ele = browser.find_element_by_link_text(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_xpath(child).click()
        elif a == 15:
            #   找到需要转移的元素
            ele = browser.find_element_by_link_text(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_css_selector(child).click()
        elif a == 16:
            #   找到需要转移的元素
            ele = browser.find_element_by_xpath(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_id(child).click()
        elif a == 17:
            #   找到需要转移的元素
            ele = browser.find_element_by_xpath(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_name(child).click()
        elif a == 18:
            #   找到需要转移的元素
            ele = browser.find_element_by_xpath(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_link_text(child).click()
        elif a == 19:
            #   找到需要转移的元素
            ele = browser.find_element_by_xpath(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_xpath(child).click()
        elif a == 20:
            #   找到需要转移的元素
            ele = browser.find_element_by_xpath(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_css_selector(child).click()
        elif a == 21:
            #   找到需要转移的元素
            ele = browser.find_element_by_css_selector(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_id(child).click()
        elif a == 22:
            #   找到需要转移的元素
            ele = browser.find_element_by_css_selector(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_name(child).click()
        elif a == 23:
            #   找到需要转移的元素
            ele = browser.find_element_by_css_selector(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_link_text(child).click()
        elif a == 24:
            #   找到需要转移的元素
            ele = browser.find_element_by_css_selector(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_xpath(child).click()
        elif a == 25:
            #   找到需要转移的元素
            ele = browser.find_element_by_css_selector(move)
            #   实现转移指令,perform执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
            auto_move(ele)
            browser.find_element_by_css_selector(child).click()
        else:
            print("悬停寻找子类出现参数输入不对等的情况", "move=%s,child=%s" % \
                  move, child)
    except:
        writeLog()


# 查找函数 move_number = move.find(_id) :此步骤暂定
def auto_move_child(move=None, child=None):
    # 这些参数是用于识别出现了那些关键字
    move_result = 3456
    child_result = 3456
    # 这些参数是用于存储切割之后的路径
    move_route = None
    child_route = None
    str = "尼玛"
    if move.find(_id) == -1:
        if move.find(_name) == -1:
            if move.find(_text) == -1:
                if move.find(_xpath) == -1:
                    if move.find(_css) == -1:
                        print("悬停寻找父类关键字怎么出问题了,move=%s" % \
                              move)
                    else:
                        move_result = 5
                        child_result = auto_child_number(child)
                else:
                    move_result = 4
                    child_result = auto_child_number(child)
            else:
                move_result = 3
                child_result = auto_child_number(child)
        else:
            move_result = 2
            child_result = auto_child_number(child)
    else:
        move_result = 1
        child_result = auto_child_number(child)

    #获取元素的路径：
    这里有坑，应该是先移动父类然后再点击子类
    move_route = character_cutting(move_result, move)
    child_route = character_cutting(child_result, child)

    route_implement_click(move_result,move_route)
    route_implement_click(child_result,child)

# 此元素用于判断子元素的路径类型
def auto_child_number(child):
    child_result = 3456
    if child.find(_id) == -1:
        if child.find(_name) == -1:
            if child.find(_text) == -1:
                if child.find(_xpath) == -1:
                    if child.find(_css) == -1:
                        print("悬停寻找子类关键字怎么出问题了,child=%s" % \
                              child)
                    else:
                        child_result = 5
                else:
                    child_result = 4
            else:
                child_result = 3
        else:
            child_result = 2
    else:
        child_result = 1

    return child_result


# 此函数用于切割数据
def character_cutting(number=5, _move=None):
    _child = None
    if number == 1:
        _child = _move[2:]
    elif number == 2:
        _child = _move[4:]
    elif number == 3:
        _child = _move[4:]
    elif number == 4:
        _child = _move[4:]
    elif number == 5:
        _child = _move[3:]
    return _child


# 此函数用于第二个子元素的点击
def route_implement_click(number=5, move_child=None):
    if number == 1:
        browser.find_element_by_id(move_child).click()
    elif number == 2:
        browser.find_element_by_name(move_child).click()
    elif number == 3:
        browser.find_element_by_link_text(move_child).click()
    elif number == 4:
        browser.find_element_by_xpath(move_child).click()
    elif number == 5:
        browser.find_element_by_css_selector(move_child).click()


def auto_move(move_ele):
    ActionChains(browser).move_to_element(move_ele).perform()
    time.sleep(2)


def writeLog():
    basename = os.path.splitext(os.path.basename(__file__))[0]
    print("文件出现错误,名为名=%s" % \
          basename, )
    raise
