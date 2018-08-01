# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_dailybulletin.py
@time: 2018/4/9 18:04

"""
import inspect
import os
import unittest

from CenterBackground.SystemSetup.NoticeController.announcementClass import AnnouncementClass

announ = AnnouncementClass()


class TestDailyBulletin(unittest.TestCase):
    '''公告'''
    """公告用例类"""
    # 用例sheet的位置
    CASE_EXCLE_POSITION = 1
    # 期望公告处于发布中时，状态的显示
    RELEASE_STATUS__EXPECT = "发布中"
    # 期望公告处于发布中时，状态的显示
    PREPARED_STATUS__EXPECT = "未开始"
    # 期望公告处于发布中时，状态的显示
    OVERDUE_STATUS__EXPECT = "已过期"

    @classmethod
    def setUpClass(cls):
        # 设计模式有误，需要设置这个参数。。唉-----------------不严谨
        announ.modify_key = True

        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        announ.openingProgram(basename, cls.CASE_EXCLE_POSITION)
        # 进入路径
        announ._rou_daily_opera()

        pass

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            announ.driver.quit()
            # announ.driver.close()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            announ.log.info("又出现UTF-8的错误........")

    # ------------------------------------页面信息验证-------------------------------------
    # @unittest.skip(r"跳过:test_AllTitle")
    def test_AllTitle(self) -> "检查页面上标签是否正确":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 进入路径
        announ.getAllTitle()
        pass

    # @unittest.skip(r"跳过:test_AllContent")
    def test_AllContent(self) -> "获取页面展示的数据是否正确":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllContent()
        pass

    # ---------------------------------筛选城市部分-----------------------------
    # @unittest.skip(r"跳过:test_AllCity")
    def test_AllCity(self) -> "筛选所有城市的公告":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllCity()

    # @unittest.skip(r"跳过:test_SingleCity")
    def test_SingleCity(self) -> "筛选单个城市的公告":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllCity()
        pass

    # ---------------------------------筛选状态部分-----------------------------
    #     @unittest.skip(r"跳过:test_WholeCityRelease")
    def test_WholeCityRelease(self) -> "全部公告+发布中筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_WholeCityStops")
    def test_WholeCityStops(self) -> "全部公告+已停止筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_WholeCityPrepared")
    def test_WholeCityPrepared(self) -> "全部公告+未开始筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_WholeCityOverdue")
    def test_WholeCityOverdue(self) -> "全部公告+已过期筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # ---------------------------------筛选城市+状态部分-----------------------------
    # @unittest.skip(r"跳过:test_AllCityRelease")
    def test_AllCityRelease(self) -> "所有城市+发布中筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_AllCityStops")
    def test_AllCityStops(self) -> "所有城市+已停止筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_AllCityPrepared")
    def test_AllCityPrepared(self) -> "所有城市+未开始筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_AllCityOverdue")
    def test_AllCityOverdue(self) -> "所有城市+已过期筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityRelease")
    def test_SingleCityRelease(self) -> "单个城市+发布中筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityStops")
    def test_SingleCityStops(self) -> "单个城市+已停止筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityPrepared")
    def test_SingleCityPrepared(self) -> "单个城市+未开始筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_SingleCityOverdue")
    def test_SingleCityOverdue(self) -> "单个城市+已过期筛选":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.getAllRelease()
        pass

    # @unittest.skip(r"跳过:test_stopReleaseWhole")
    def test_stopReleaseWhole(self) -> "停止发布中的中一个公告":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])
        announ.getStopRelease()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyCity")
    def test_overdueModifyCity(self) -> "修改某个已过期的公告,改变所属地":
        """
        修改某个已过期的公告，改变所属地
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyTitle")
    def test_overdueModifyTitle(self) -> "修改某个已过期的公告,改变标题":
        """
        修改某个已过期的公告，改变标题
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unitest.skip(r"跳过:test_overdueModifyContent")
    def test_overdueModifyContent(self) -> "修改某个已过期的公告,改变内容":
        """
        修改某个已过期的公告，改变内容
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyReleaseTime")
    def test_overdueModifyReleaseTime(self) -> "修改某个已过期的公告,改变时间":
        """
        修改某个已过期的公告，当前时间在有限期内.此时该公告变成发布中
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyNotStart")
    def test_overdueModifyNotStart(self) -> "修改某个已过期的公告,改变时间":
        """
        修改某个已过期的公告，当前时间小于有限期
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_overdueModifyOverdue")
    def test_overdueModifyOverdue(self) -> "修改某个已过期的公告,改变时间":
        """
        修改某个已过期的公告，当前时间大于有限期
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyCity")
    def test_stopsModifyCity(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告，改变所属地
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyTitle")
    def test_stopsModifyTitle(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告，改变标题
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyContent(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告，改变内容
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyReleaseTime(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告（当前时间在有效期内）
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyNotStart(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告（当前时间小于有限期）
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_stopsModifyContent")
    def test_stopsModifyStops(self) -> "不知道给什么备注比较好":
        """
        修改某个已停止的公告（当前时间大于有效期）
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    def test_stopsModifyRelease(self):
        """
        点击已停止的公告的发布按钮
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.getStopRelease(bl_button=False)
        pass

    # @unittest.skip(r"跳过:test_preparedModifyCity")
    def test_preparedModifyCity(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告，改变所属地
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyTitle")
    def test_preparedModifyTitle(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告，改变标题
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyContent")
    def test_preparedModifyContent(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告，改变内容
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_overdue_modify()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyReleaseTime")
    def test_preparedModifyReleaseTime(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告（当前时间在有效期内）
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyNotStart")
    def test_preparedModifyNotStart(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告（当前时间小于有限期）
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_preparedModifyStops")
    def test_preparedModifyStops(self) -> "不知道给什么备注比较好":
        """
        修改某个未开始的公告（当前时间大于有效期）
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.status_judge_time()
        pass

    # @unittest.skip(r"跳过:test_preparedActionStops")
    def test_preparedActionStops(self):
        """
        停止某个未开始的公告
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.getStopRelease(bl_button=False)
        pass

    # ---------------发布公告都是执行输入动作，无法提交数据所以不进行数据库判断----------------
    # @unittest.skip(r"跳过:test_dailyReleaseCity")
    def test_dailyReleaseCity(self):
        """
        发布公告，默认选择所有城市
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseTitle")
    def test_dailyReleaseTitle(self):
        """
        发布公告，仅输入标题
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseTitle")
    def test_dailyReleaseContent(self):
        """
        发布公告，仅输入内容
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseTime")
    def test_dailyReleaseTime(self):
        """
        发布公告，输入时间
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseTime")
    def test_dailyReleaseTime(self):
        """
        发布公告，仅输入内容
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseCityTitle")
    def test_dailyReleaseCityTitle(self):
        """
        发布公告，城市+标题
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseTitleContent")
    def test_dailyReleaseTitleContent(self):
        """
        发布公告，标题+内容
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseCitvContent")
    def test_dailyReleaseCitvContent(self):
        """
        发布公告，城市+内容
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyReleaseCityTile")
    def test_dailyReleaseCityTile(self):
        """
        发布公告，城市+时间
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.get_announcement_release()
        pass

    # @unittest.skip(r"跳过:test_dailyToRelease")
    def test_dailyToRelease(self):
        """
        发布公告，公告为发布中
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.release_judge_time()
        pass

    # @unittest.skip(r"跳过:test_dailyToOverdue")
    def test_dailyToOverdue(self):
        """
        发布公告，公告为未开始
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.release_judge_time()
        pass

    # @unittest.skip(r"跳过:test_dailyToPrepare")
    def test_dailyToPrepare(self):
        """
        发布公告，当前时间小于结束时间
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.release_judge_time()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
