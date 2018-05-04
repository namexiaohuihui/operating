# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: promptWindow.py
@time: 2018/4/15 16:09
"""

class PromptWindow(object):
    """提示窗口的操作控制器"""
    # 提示窗口的标题
    PROMPT_TTILE = ""
    # 提示窗口的内容
    PROMPT_CONTENT = ""
    # 提示窗口的按钮
    PROMPT_BUTTON = ""

    def setPromptTitle(self,title):
        self.PROMPT_TTILE = title

    def setPromptContent(self,content):
        self.PROMPT_CONTENT = content

    def setPromptButton(self,button):
        self.PROMPT_BUTTON = button

    def __eq__(self, other):
        title_eq = self.PROMPT_TTILE.__eq__(other["title"])
        content_eq = self.PROMPT_TTILE.__eq__(other["content"])
        button_eq = self.PROMPT_TTILE.__eq__(other["button"])
        if title_eq and content_eq and button_eq :
            propt_boolean = True
        else:
            propt_boolean = False

        return propt_boolean