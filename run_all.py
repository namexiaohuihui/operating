# coding:utf-8
import unittest
import os
import HTMLTestRunner

# 用例路径
import time

if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), "page_web")
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), "report")

    # 设置时间格式
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))

    # html报告文件
    # report_abspath = os.path.join(report_path, "result" + now + ".html")
    report_abspath = os.path.join(report_path, "result.html")

    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="*participate.py",
                                                   top_level_dir=None)

    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(discover)
    fp.close()
