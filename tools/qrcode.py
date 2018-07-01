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


if __name__ == '__main__':
    link_range_list = [(0, 50), (51, 100), (101, 150), (151, 200), (201, 250), (251, 300)]
    print(link_range_list[0])