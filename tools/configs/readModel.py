# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: readModel.py
@time: 2017/12/20 23:30
@项目名称:operating
"""
import configparser
import os

cur_path = r'E:\drivers\CasePlan'
# cur_path = os.path.dirname(os.path.realpath(__file__))


def establish_con(model):
    configPath = os.path.join(cur_path, model + ".ini")
    conf = configparser.ConfigParser()
    conf.read(configPath)
    return conf


def url():
    conf = establish_con("excel")
    url = conf.get("excel", "parameterSetting")
    print(url)


def obtain_con(conf):
    email_smtp_server = conf.get("email", "smtp_server")
    email_port = conf.get("email", "port")
    email_sender = conf.get("email", "sender")
    email_psw = conf.get("email", "psw")
    email_receiver = conf.get("email", "receiver")
    print(conf)


if __name__ == '__main__':
    connn = establish_con("model")

    print(connn.get("email", "port"))
