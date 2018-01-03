# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: ConversionStorage.py
@time: 2018/1/3 22:35
@项目名称:operating
"""

class conversionstorage(object):
    """
        单例类的用法：
        用于连接两个类之间的数据数据。
        通过第三方来传递信息
        """

    def __new__(cls, *args, **kw):
        # 单例类判断。如果该类创建过就不需要重新创建了
        if not hasattr(cls, '_instance'):
            orig = super(conversionstorage, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def set_remarks(self, remarks):
        self.remarks = remarks

    def get_remarks(self):
        try:
            return self.remarks
        except AttributeError:
            return "我返回的是默认值"
        except:
            return "执行失败"


if __name__ == '__main__':
    # print(temporarystorage().set_remarks("nihao"))
    print(conversionstorage().get_remarks())
    print(conversionstorage().set_remarks("buhoa"))
    print(conversionstorage().get_remarks())