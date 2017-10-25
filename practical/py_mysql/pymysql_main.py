# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: pymysql_main.py
@time: 2017/7/13 16:12
"""
import pymysql

class pymysqls(object):

    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(pymysqls, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            print('pymysqls')
        return cls._instance

    #数据库和游标一起创建
    def connects_cureors(self, host,port,user,passwd,db,charset):
        self.connect = pymysql.Connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset
        )
        self.cursor = self.connect.cursor()
        return self.cursor

    # 连接数据库
    def connects(self, host,port,user,passwd,db,charset):
        #链接数据库，定义账号密码以及用户名
        self.connect = pymysql.Connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset
        )
        return self.connect

    def cureors(self):
        # 通过连接数据来获取游标
        self.cursor = self.connect.cursor()
        return self.cursor


    def selects(self,sql=None):
        print("查询")
        if sql != None:
            self.cursor.execute(sql)

            # 好像是打印字段的属性
            index = self.cursor.description

            # 定义一个容器，好比java的jsona
            result = []

            # fetchall():接收全部的返回结果行.
            for res in self.cursor.fetchall():

                # 定义一个容器，好比java的jsons
                row = {}

                # range(x):表示从0到x，不包括x
                # len:返回字符串、列表、字典、元组等长度
                for i in range(len(index)):
                    # index[i][0] 获取字段里属性中的局部信息
                    row[index[i][0]] = res[i]
                result.append(row)

            return result
        else:
            print('sql语句为空不进行查询')

    def closes(self):
        # 关闭游标
        self.cursor.close()
        # 关闭库链接
        self.connect.close()

    def testing(self):
        # 事务处理
        sql_1 = "UPDATE money SET saving = saving + 1000 WHERE account = '18012345678' "
        sql_2 = "UPDATE money SET expend = expend + 1000 WHERE account = '18012345678' "
        sql_3 = "UPDATE money SET income = income + 2000 WHERE account = '18012345678' "

        try:
            self.cursor.execute(sql_1)  # 储蓄增加1000
            self.cursor.execute(sql_2)  # 支出增加1000
            self.cursor.execute(sql_3)  # 收入增加2000
        except Exception as e:
            self.connect.rollback()  # 事务回滚
            print('事务处理失败', e)
        else:
            # 事务提交，如果不提交事务那就插入数据的语句就不会执行
            self.connect.commit()
            print('事务处理成功', self.cursor.rowcount)


    def query(self, sql):
        self.cursor.execute(sql)

        # 好像是打印字段的属性
        index = self.cursor.description

        #定义一个容器，好比java的jsona
        result = []

        # fetchall():接收全部的返回结果行.
        for res in self.cursor.fetchall():

            # 定义一个容器，好比java的jsons
            row = {}

            #range(x):表示从0到x，不包括x
            # len:返回字符串、列表、字典、元组等长度
            for i in range(len(index)):
                # index[i][0] 获取字段里属性中的局部信息
                row[index[i][0]] = res[i]
            result.append(row)

        return result

if __name__ == '__main__':
    pm = pymysqls.__new__(pymysqls)
    pm.connects_cureors('localhost', 3306, 'root', 'xiaodingdong', 'ph_exclusive', 'utf8')
    sql = "select * from ph_exclusive.ph_gonggao;"
    data = ('---')
    pm.selects(sql)
    pm.closes()