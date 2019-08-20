# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: wxpyLiaotian.py
@time: 2018/9/22 7:08
@Entry Name:operating
"""

from wxpy import *
import re
import os
import ctypes

bot = Bot(cache_path='logoo.pkl', qr_path='QR.png')

# 指定一个好友
my_friend = bot.friends()
print(my_friend)
# 查看他的 puid
print(my_friend.puid)


# 下载文件并向文件传输助手发送
def dlDoc(fPath, ra, content, flag):
    ra.get('Text')(fPath)
    bot.file_helper.send(content)
    if 4 == flag:
        bot.file_helper.send_image(fPath)
    elif 7 == flag:
        bot.file_helper.send_video(fPath)
    else:
        bot.file_helper.send_file(fPath)
    os.remove(fPath)


# 文本 TEXT = 'Text'
# 位置 MAP = 'Map' 1
# 名片 CARD = 'Card' 2
# 分享 SHARING = 'Sharing' 3
# 图片 PICTURE = 'Picture'  4
# 语音 RECORDING = 'Recording' 5
# 文件 ATTACHMENT = 'Attachment' 6
# 视频 VIDEO = 'Video' 7
@bot.register(except_self=False, run_async=True, enabled=True)
def handleReceiveMsg(msg):
    '''
    监听消息
    :param msg:
    :return:
    '''
    ra = msg.raw
    mss = msg.bot.messages
    le = len(mss)

    if ra['Status'] == 4:
        # 获取消息ID
        oldmsgid = re.search(re.compile('<msgid>(.*?)</msgid>', re.S), ra['Content']).group(1)
        for i in range(le - 1, -1, -1):
            if oldmsgid == str(mss[i].id):
                name = msg.chat.name
                if name == None or name == '':
                    name = msg.chat.nick_name
                if mss[i].type == 'Text':
                    bot.file_helper.send(name + '撤回了一条消息：' + mss[i].text)
                    break
                elif mss[i].type == 'Map':
                    bot.file_helper.send(name + '撤回了一个位置信息：' + (mss[i].location)['label'])
                    break
                elif mss[i].type == 'Card':
                    card = mss[i].card
                    name = card.name
                    if name == None or name == '':
                        name = card.nick_name
                    sex = str(card.sex)
                    if sex == '1':
                        sex = '男'
                    else:
                        sex = '女'
                    bot.file_helper.send(name + '撤回了一张名片：名称：' + name + ',性别：' + sex)
                    break
                elif mss[i].type == 'Sharing':
                    bot.file_helper.send(name + '撤回了一个分享：' + mss[i].url)
                    break
                elif mss[i].type == 'Picture':
                    dlDoc(mss[i].file_name, mss[i].raw, name + '撤回了一张图片，图片正在加载。。。')
                    break
                elif mss[i].type == 'Recording':
                    dlDoc(mss[i].file_name, mss[i].raw, name + '撤回了一条语音，语音正在加载。。。')
                    break
                elif mss[i].type == 'Attachment':
                    dlDoc(mss[i].file_name, mss[i].raw, name + '撤回了一个文件，文件正在加载。。。')
                    break
                elif mss[i].type == 'Video':
                    dlDoc(mss[i].file_name, mss[i].raw, name + '撤回了一个视频，视频正在加载。。。')
                    break


embed()
