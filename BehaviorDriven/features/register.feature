# -*- coding: utf-8 -*-
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
#@author:  ln_company
#@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
#@software: PyCharm
#@file:  register.features.py
#@time: 2019/1/27 16:38
#@Software: PyCharm
#@Site    :
#@desc:

Feature: Register User

  As a developer
  This is my  first bdd project

  Scenario: open register website
    When I open the register website "http://reg.email.163.com/unireg/call.do?cmd=register.entrance"
    Then I expect that the title is "注册"

  Scenario: input username
      When I set with "mainPwdIpt" "nishidalao"
      And I set with "nameIpt" "nizhendeshi"
      And I set with "mainCfmPwdIpt" "nizhendeshi"
      And I set with "vcodeIpt" "nizhendeshi"
      And I click with registerbutton
      Then I expect that text "手机验证码"