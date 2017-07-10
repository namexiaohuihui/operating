# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/6/20 22:38

"""

'''
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

'''
#导入pymysql的包
import  pymysql.cursors

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#port 必须是数字不能为字符串
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test',
                           port=3307,
                           charset='utf8')
try:
    #获取一个游标
   with connection.cursor() as cursor:
       sql="select * from lnsm_user where phone LIKE '%1877803%' and type = 1;"
       cout=cursor.execute(sql)
       print("数量： "+ str(cout))#str(cout)转成str类型

       for row in cursor.fetchall():
           #print('%s\t%s\t%s' %row)

            #注意int类型需要使用str函数转义
           print("ID: "+str(row[0])+'  名字： '+row[1]+"  性别： "+row[2])
       connection.commit()

finally:
    connection.close()