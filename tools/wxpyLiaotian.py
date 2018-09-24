# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: wxpyLiaotian.py
@time: 2018/9/22 7:08
@Entry Name:operating
"""
from wxpy import *
import time
# 初始化一个机器人对象
# bot = Bot(cache_path='E:\wxpy.pkl',console_qr='E:\operating\tools\QR.png')
'''
cache_path –
    设置当前会话的缓存路径，并开启缓存功能；为 None (默认) 则不开启缓存功能。
    开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
    设为 True 时，使用默认的缓存路径 ‘wxpy.pkl’。
qr_path – 保存二维码的路径
console_qr – 在终端中显示登陆二维码
'''
bot=Bot(cache_path="logoo.pkl",qr_path='QR,png')
# bot=Bot(console_qr=True,cache_path="logoo.pkl",qr_path='QR,png')

# 向文件传输助手发送给消息
# bot.file_helper.send('hello,I is DaGe')

# 查找朋友"小号"
# my_friend = bot.friends().search('小号')[0]
# 发送消息
# my_friend.send('趁着中秋佳节来到,我有一点点想要......邀你喝一杯,毕竟举杯邀明月，天涯共此时嘛~节日快乐哦!')

# 群发消息（谨慎使用，哈哈哈）
my_friends = bot.friends(update=False)
my_friends.pop(0)   # 去除列表第一个元素（自己）
l_my = len(my_friends)
for i in range(120,l_my): # 时间限制2分钟内最多发120次（具体看wxpy官方文档异常处理）
    friend = my_friends[i]
    print(friend)
    print(i)
    print("----------------")
    friend.send('趁着中秋佳节来到,我有一点点想要......邀你喝一杯,毕竟举杯邀明月，天涯共此时嘛~节日快乐哦!')
    time.sleep(2)
    # friend.send('不用回复，生活中一起加油！')