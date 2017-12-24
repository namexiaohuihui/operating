# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: TemporaryData.py
@time: 2017/12/24 20:38
@项目名称:operating
"""
class temporarystorage(object):
    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(temporarystorage, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
    def set_remarks(self,remarks):
        self.remarks = remarks
        return self.remarks

    def get_remarks(self):
        return self.remarks
if __name__ == '__main__':
    print(temporarystorage().set_remarks("nihao"))
    print(temporarystorage().get_remarks())
    print(temporarystorage().set_remarks("buhoa"))
    print(temporarystorage().get_remarks())
