# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: QRCode.py
@time: 2018/3/19 15:10

可读取二维码上的数据信息
"""
import sys
from pyzbar.pyzbar import decode
import cv2


class QRCode(object):
#
# if len(sys.argv) < 2:
#     print("Usage : %s <image file>" %sys.argv[0])
#     sys.exit(1)
    filepath = r"----6.png"

    def getQRCodeData(self):
        image = cv2.imread(filepath)
        result = decode(image)
        for item in result:
            print(item.type)
            print(item.data)