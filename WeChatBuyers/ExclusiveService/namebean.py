# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: namebean.py
@time: 2018/1/25 23:16
@Entry Name:operating
"""
from tools.excelname import even_exclusiveService
# 该类主要设置一些常用的属性值以及参数

class letter_parameter_names(even_exclusiveService):

    dialog_false = ".am-dialog-footer>button:nth-child(1)"  # 退出弹窗中的取消按钮
    dialog_true = ".am-dialog-footer>button:last-child"  # 退出弹窗中的取消按钮

    # 退出
    exit_head = ".nav-head"  # 头像
    exit_dialog_body = ".am-dialog-body" # 退出弹窗中的内容
    exit_dialog_morange= ".u-btn.u-btn-morange" # 提交按钮
    exit_sidebar = ".user-sidebar>li:last-child"

    # 昵称
    nickname_msg= ".sidebar-msg" # 退出弹窗中的取消按钮
    nickname_txt= ".u-txt.u-txt-l" # 退出弹窗中的取消按钮

    # 修改密码
    password_sidebar = ".user-sidebar>li:nth-child(6)" # 修改密码
    password_error_msg = ".error-msg" # 错误信息
    password_oldpwd = "J_oldpwd" # 旧密码
    password_newpwd = "J_newpwd" # 新密码
    password_repeatPwd = "J_repeatPwd" # 确认密码
    password_morange= ".u-btn.u-btn-morange" # 提交按钮

    # 修改手机
    phone_verify_from = ".verify-form-itme>span:nth-child(2)"