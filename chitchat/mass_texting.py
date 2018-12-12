# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: wxpyLiaotian.py
@time: 2018/9/22 7:08
@Entry Name:operating
"""
from chitchat.open_wxpy import OpenWxpy
import time


# 初始化一个机器人对象

# KeyError: 'pass_ticket'

def danliao(bot):
    # 向文件传输助手发送给消息
    bot.file_helper.send('hello,I is DaGe')
    # 查找朋友"小号"
    my_friend = bot.friends().search('小号')[0]
    # 发送消息
    my_friend.send('趁着中秋佳节来到,我有一点点想要......邀你喝一杯,毕竟举杯邀明月，天涯共此时嘛~节日快乐哦!')
    pass


def qunfa(bot):
    # 群发消息（谨慎使用，哈哈哈）
    my_friends = bot.friends(update=False)
    my_friends.pop(0)  # 去除列表第一个元素（自己）
    l_my = len(my_friends)
    for i in range(120, l_my):  # 时间限制2分钟内最多发120次（具体看wxpy官方文档异常处理）
        friend = my_friends[i]
        print(friend)
        print(i)
        print("----------------")
        friend.send('趁着中秋佳节来到,我有一点点想要......邀你喝一杯,毕竟举杯邀明月，天涯共此时嘛~节日快乐哦!')
        time.sleep(2)
        friend.send('不用回复，生活中一起加油！')
        time.sleep(2)
        pass
    pass


def gei_qun_fasong(bot):
    wxpy_groups = bot.groups(update=False).search("测试")
    for gr in wxpy_groups:
        print(gr)
        gr.send("测试")
        gr.send_image(r'F:\图片\22.png')
        pass
    bot.join()
    bot.logout()

def denglu_gongzhonghao(bot):
    # 登陆用户的全部公众号
    bot_mps = bot.mps(update=False)
    for m in bot_mps:
        str_m = str(m).strip().split(':', 2)[1].replace(">", '')
        print(str_m)
        print(type(str_m))

if __name__ == '__main__':
    bot_open = OpenWxpy()
    bot = bot_open.bot
    # my_friend = bot.friends().search('小号')[0]
    # # 发送消息
    # my_friend.send_image(r'F:\图片\22.png')
