# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_dailybulletin.py
@time: 2018/4/9 18:04

"""
import os
import inspect
import unittest

from PageWeb.WebShop.SystemSetup.NoticeController.dailyOperationSteps import DailyOperationSteps

disSte = DailyOperationSteps()


class DailyBulletin(unittest.TestCase):
    """公告用例类"""

    @classmethod
    def setUp(cls):
        # 该类运行时优先调用的函数
        basename = os.path.splitext(os.path.basename(__file__))[0]
        disSte.setDailyBulletin(basename)
        # 进入路径
        disSte._rou_DailyFun()
        pass

    @classmethod
    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            # disSte.driver.quit()
            # disSte.sleep_time(1)
            pass
        except UnicodeDecodeError:
            disSte.log.info("又出现UTF-8的错误........")

    # ------------------------------------页面信息验证-------------------------------------
    # @unittest.skip(r"跳过:test_AllTitle")
    def ttest_AllTitle(self) -> "检查页面上标签是否正确":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 进入路径
        disSte.getAllTitle()
        pass

    # @unittest.skip(r"跳过:test_AllContent")
    def ttest_AllContent(self) -> "获取页面展示的数据是否正确":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllContent()

    # ---------------------------------筛选城市部分-----------------------------
    # @unittest.skip(r"跳过:test_AllCity")
    def ttest_AllCity(self) -> "筛选所有城市的公告":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllCity()

    # @unittest.skip(r"跳过:test_SingleCity")
    def ttest_SingleCity(self) -> "筛选单个城市的公告":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllCity()
        pass

    # ---------------------------------筛选状态部分-----------------------------
    #     @unittest.skip(r"跳过:test_WholeCityRelease")
    def ttest_WholeCityRelease(self) -> "全部公告+发布中筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_WholeCityStops")
    def ttest_WholeCityStops(self) -> "全部公告+已停止筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_WholeCityPrepared")
    def ttest_WholeCityPrepared(self) -> "全部公告+未开始筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_WholeCityOverdue")
    def ttest_WholeCityOverdue(self) -> "全部公告+已过期筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # ---------------------------------筛选城市+状态部分-----------------------------
    # @unittest.skip(r"跳过:test_AllCityRelease")
    def ttest_AllCityRelease(self) -> "所有城市+发布中筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_AllCityStops")
    def ttest_AllCityStops(self) -> "所有城市+已停止筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_AllCityPrepared")
    def ttest_AllCityPrepared(self) -> "所有城市+未开始筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_AllCityOverdue")
    def ttest_AllCityOverdue(self) -> "所有城市+已过期筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_SingleCityRelease")
    def ttest_SingleCityRelease(self) -> "单个城市+发布中筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_SingleCityStops")
    def ttest_SingleCityStops(self) -> "单个城市+已停止筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_SingleCityPrepared")
    def ttest_SingleCityPrepared(self) -> "单个城市+未开始筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_SingleCityOverdue")
    def ttest_SingleCityOverdue(self) -> "单个城市+已过期筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

    # @unittest.skip(r"跳过:test_stopReleaseWhole")
    def ttest_stopReleaseWhole(self) -> "停止发布中中一个公告":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.getStopRelease()

    # @unittest.skip(r"跳过:test_overdueModifyWhole")
    def test_overdueModifyWhole(self):
        """
        修改某个已过期的公告，改变所属地
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()


if __name__ == '__main__':
    unittest.main(verbosity=2)
