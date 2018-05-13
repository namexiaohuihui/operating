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
        pass

    # @unittest.skip(r"跳过:test_WholeCityStops")
    def ttest_WholeCityStops(self) -> "全部公告+已停止筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_WholeCityPrepared")
    def ttest_WholeCityPrepared(self) -> "全部公告+未开始筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_WholeCityOverdue")
    def ttest_WholeCityOverdue(self) -> "全部公告+已过期筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # ---------------------------------筛选城市+状态部分-----------------------------
    # @unittest.skip(r"跳过:test_AllCityRelease")
    def ttest_AllCityRelease(self) -> "所有城市+发布中筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_AllCityStops")
    def ttest_AllCityStops(self) -> "所有城市+已停止筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_AllCityPrepared")
    def ttest_AllCityPrepared(self) -> "所有城市+未开始筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_AllCityOverdue")
    def ttest_AllCityOverdue(self) -> "所有城市+已过期筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityRelease")
    def ttest_SingleCityRelease(self) -> "单个城市+发布中筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityStops")
    def ttest_SingleCityStops(self) -> "单个城市+已停止筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityPrepared")
    def ttest_SingleCityPrepared(self) -> "单个城市+未开始筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityOverdue")
    def ttest_SingleCityOverdue(self) -> "单个城市+已过期筛选":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_stopReleaseWhole")
    def ttest_stopReleaseWhole(self) -> "停止发布中的中一个公告":
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.getStopRelease()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyCity")
    def ttest_overdueModifyCity(self) -> "修改某个已过期的公告,改变所属地":
        """
        修改某个已过期的公告，改变所属地
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyTitle")
    def test_overdueModifyTitle(self) -> "修改某个已过期的公告,改变标题":
        """
        修改某个已过期的公告，改变标题
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyContent")
    def test_overdueModifyContent(self) -> "修改某个已过期的公告,改变内容":
        """
        修改某个已过期的公告，改变内容
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyReleaseTime")
    def test_overdueModifyReleaseTime(self) -> "修改某个已过期的公告,改变时间":
        """
        修改某个已过期的公告，当前时间在有限期内
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass

    # @unittest.skip(r"跳过:test_overdueModifyNotStart")
    def test_overdueModifyNotStart(self) -> "修改某个已过期的公告,改变时间":
        """
        修改某个已过期的公告，当前时间小于有限期
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass

    # @unittest.skip(r"跳过:test_overdueModifyOverdue")
    def test_overdueModifyOverdue(self) -> "修改某个已过期的公告,改变时间":
        """
        修改某个已过期的公告，当前时间大于有限期
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass

    # @unittest.skip(r"跳过:test_stopsModifyCity")
    def test_stopsModifyCity(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告，改变所属地
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyTitle")
    def test_stopsModifyTitle(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告，改变标题
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyContent(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告，改变内容
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyReleaseTime(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告（当前时间在有效期内）
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyNotStart(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告（当前时间小于有限期）
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyStops(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告（当前时间大于有效期）
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass






    # @unittest.skip(r"跳过:test_preparedModifyCity")
    def test_preparedModifyCity(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告，改变所属地
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyTitle")
    def test_preparedModifyTitle(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告，改变标题
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyContent")
    def test_preparedModifyContent(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告，改变内容
        :return: None
        """
        disSte.setFunctionName(inspect.stack()[0][3])
        disSte.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyReleaseTime")
    def test_preparedModifyReleaseTime(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告（当前时间在有效期内）
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass

    # @unittest.skip(r"跳过:test_preparedModifyNotStart")
    def test_preparedModifyNotStart(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告（当前时间小于有限期）
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass

    # @unittest.skip(r"跳过:test_preparedModifyStops")
    def test_preparedModifyStops(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告（当前时间大于有效期）
        :return: None
        """
        # disSte.setFunctionName(inspect.stack()[0][3])
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
