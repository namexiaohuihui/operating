# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: pymysql_main.py
@time: 2017/7/13 16:12
"""
import pymysql

class pymysqls(object):
    connect = ''
    cursor = ''

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
        # 获取游标
        self.cursor = self.connect.cursor()
        return self.cursor

    def inserts(self,sql,data):
        # 插入数据
        sql = "INSERT INTO money (name, account, saving) VALUES ( '%s', '%s', %.2f )"
        data = ('雷军', '13512345678', 10000)
        self.cursor.execute(sql % data)
        self.connect.commit()
        print('成功插入', self.cursor.rowcount, '条数据')

    def selects(self,sql,data):
        print("查询")
        self.cursor.execute(sql % data)
        for row in self.cursor.fetchall():
            id = row[0]
            print("id为%s" %id)
        print('共查找出', self.cursor.rowcount, '条数据')

    def delects(self,sql,data):
        # 删除数据
        sql = "DELETE FROM money  WHERE account = '%s' LIMIT %d"
        data = ('13512345678', 1)
        self.cursor.execute(sql % data)
        self.connect.commit()
        print('成功删除', self.cursor.rowcount, '条数据')

    def closes(self):
        # 关闭连接
        self.cursor.close()
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
            self.connect.commit()  # 事务提交
            print('事务处理成功', self.cursor.rowcount)


if __name__ == '__main__':
    print("33")
    pm = pymysqls.__new__(pymysqls)
    # pm.connects()
    # pm.cureors()
    pm.connects_cureors('load', 8888, 'root', 'mima', 'table', 'utf8')
    sql = "SELECT * FROM lnsm_user WHERE phone = %s;"
    data = ('---')
    pm.selects(sql, data)