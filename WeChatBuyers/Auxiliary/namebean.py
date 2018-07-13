# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: namebean.py
@time: 2018/1/25 22:13
@Entry Name:operating
"""

from tools.excelname import even_auxiliary
# 该类主要设置一些常用的属性值以及参数

class letter_parameter_names(even_auxiliary):

    # 首页的按钮点击位置
    home_gobuy = ".J_goBuy.m-cart-by"  # 点击去结算
    home_cart = ".m-cart-total" # 进入购物车
    home_gobuy_cart = ".J_btn.u-btn" # 进入购物车里面点击去结算
    home_goods_cur = ".shop-goods.shop-goods-cur li:nth-child(1)" # 点击位于第一个位置的商品进入详情
    home_tiket_items = ".shop-tiket-items.J_buyTiket a:nth-of-type(1)" # 点击首页的水票
    home_gobuy_tiket = "#J_detailLst>p:last-child" # 点击水票弹窗的去结算
    home_cur_detail = ".shop-tiket-items.detail-add>a:last-child" # 详情内添加购物车
    home_gobuy_detail = ".buy-tiket-btn" # 登陆弹窗
    home_goods_evaluate = '.goods-nav>a:nth-child(3)' # 商品评价
    home_goods_detail = '.goods-nav>a:last-child' # 切换到商品详情页面

    # 一键送水按钮
    key_onekey = '.nav-onekey' #一键送水按钮
    key_onekey_dis = '.onekey-btn.dis' # 暂时未知


    # 订单页面
    order_order = ".nav-order"


    # 注册页面页面
    registered_user = ".nav-user" # 个人页面
    registered_head = ".nav-head" # 头像
    registered_login_type = ".login-type>a:nth-child(2)" # 切换注册
    registered_protocol = "J_protocol" # 协议
    registered_over_box = ".over-box" # 协议的内容
    registered_privacy= "J_privacy" # 协议的内容
    registered_message_tip= ".message-tip" # 协议的内容
    registered_close= ".close" # 协议的内容

    #　用户页面
    user_user = ".nav-user"
    user_payment = ".msg-nav>a:nth-child(1)" # 待付款
    user_delivery = ".msg-nav>a:nth-child(2)" # 待发货
    user_distribution = ".msg-nav>a:nth-child(3)" # 配送中
    user_evaluated = ".msg-nav>a:nth-child(4)" # 待评价

    user_envelopes = ".user-sidebar>li:nth-child(1)" # 红包
    user_coupons = ".user-sidebar>li:nth-child(2)" # 卡券
    user_ticket = ".user-sidebar>li:nth-child(3)" # 水票
    user_address = ".user-sidebar>li:nth-child(4)" # 地址

    # 水票页面
    water_watikis = '.nav-watikis' # 进入水票
    water_dialog = ".am-dialog-button" #　点击水票进行选购
    water_tiket_price = '.shop-tiket-price>a:nth-child(2)' #　点击水票弹窗中的购买
    water_sign_login = '.buy-tiket-btn' #　点击登录
    water_watikis_detail = '.tiket-buy-lst>li:nth-child(1)' #　水票详情页面
    water_add_detail = ".shop-tiket-items.detail-add>a:nth-of-type(1)" #　详情中购买
    water_nth_detail = ".select-watikis>a:nth-child(2)" #　点击个人水票







