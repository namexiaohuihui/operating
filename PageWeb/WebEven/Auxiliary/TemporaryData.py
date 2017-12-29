# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: TemporaryData.py
@time: 2017/12/24 20:38
@项目名称:operating
"""


class temporarystorage(object):
    """
    单例类的用法：
    用于连接两个类之间的数据数据。
    通过第三方来传递信息
    """

    def __new__(cls, *args, **kw):
        # 单例类判断。如果该类创建过就不需要重新创建了
        if not hasattr(cls, '_instance'):
            orig = super(temporarystorage, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def set_remarks(self, remarks):
        self.remarks = remarks

    def get_remarks(self):
        try:
            self.remarks = self.remarks
            return self.remarks
        except:
            return "执行失败"


if __name__ == '__main__':
    print(temporarystorage().set_remarks("nihao"))
    print(temporarystorage().get_remarks())
    print(temporarystorage().set_remarks("buhoa"))
    print(temporarystorage().get_remarks())

    from practical.config import readModel

    file_path = readModel.establish_con().get("excel", "file")
    print(file_path)
