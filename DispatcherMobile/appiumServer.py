# -*- coding: utf-8 -*-
"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      appiumServer.py
@time:      2019/1/7 16:12
@desc:
"""
import socket
import subprocess


class AppiumServer():

    def check_port(self, host, port):
        """检测端口是否被占用"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            s.shutdown(2)
            print('port %s is uesd !' %port)
            return False
        except:
            print('port %s is available!' %port)
            return True

    def start_appium(self,host,port):
        """启动appium 服务"""
        erromessage=""
        appium_server_url=""
        bootstrap_port=str(port+1)

        try:
            if self.check_port(host,port):

                cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port)
                print(cmd)

                # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                p = subprocess.Popen(cmd, shell=True, stdout=open('E:/logs.log','a'), stderr=subprocess.STDOUT)
                p.wait()

                appium_server_url = 'http://' + host + ':' + str(port) + '/wd/hub'
                print(appium_server_url)

        except Exception as msg:
            erromessage=str(msg)

        return appium_server_url,erromessage


if __name__ == '__main__':
    s=AppiumServer()
    s.start_appium('127.0.0.1',4729)
    s.start_appium('127.0.0.1',4725)