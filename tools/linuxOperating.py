# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: linuxOperating.py
@time: 2018/6/27 14:45
通过账号密码简单的执行linux的一些指令动作
"""
import traceback

import paramiko


class LinuxOperating(object):
    def __init__(self, l_dict):
        self.hostname = l_dict["host"]  # The Linux port
        self.username = l_dict["user"]  # The user name
        self.password = l_dict["pass"]  # The  login password
        self.port = l_dict["port"]  # The Linux port
        self.to_linux_close()
        pass

    def to_linux_close(self):
        self.to_connection()
        self.to_instruction()
        self.client.close()

    def to_linux(self):
        self.to_connection()
        self.to_instruction()

    def to_connection(self, timeout=4):
        try:
            self.client = paramiko.SSHClient()
            # 允许连接不在know_hosts文件中的主机
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 输入指定的端口和用户名
            self.client.connect(self.hostname, self.port, username=self.username, password=self.password,
                                timeout=timeout)
        except:
            print(traceback.format_exc())

    def to_instruction(self, timeout=4):
        '''
        exec_command为单个会话,执行完成之后会回到登录时的缺省目录
        以分号;分隔表示先后执行两个命令;可以传入多个参数

        stdout.readlines() 执行动作之后，可读取文档数据信息
        :param timeout:
        :return:
        '''
        try:
            stdin, stdout, stderr = self.client.exec_command(
                l_dict['cmd'])
            self.stdout_content = stdout.readlines()
        except:
            print(traceback.format_exc())

    def set_parameter(self, parameter):
        self.parameter_dict = parameter

    def get_parameter(self):
        return self.parameter_dict

    def set_stdout_content(self, stdout):
        self.log_content = stdout

    def get_stdout_content(self):
        return self.log_content

    linux_parameter = property(get_parameter,
                               set_parameter, doc="The Linux parameters were set incorrectly.")

    stdout_content = property(get_stdout_content,
                              set_stdout_content, doc="Linux data acquisition failed.")


if __name__ == '__main__':
    l_dict = {
        "host": "192.168.10.203",
        "user": "--",
        "pass": "**",
        "port": 22,
        "cmd": "cd log/;cat sms-2018-25.log"}
    content = LinuxOperating(l_dict).stdout_content
    print(content)
    for neirong in content:
        if '13566667878' in neirong and 'Tue, 19 Jun 18 18:10' in neirong:
            print(neirong)
            break
