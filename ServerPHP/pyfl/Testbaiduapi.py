# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: Testbaiduapi.py
@time: 2017/11/29 22:56
@项目名称:operating
"""
import requests,unittest,json,HTMLTestRunner
class Testbaiduapi(unittest.TestCase):
    def setUp(self):
        url = "http://fanyi.baidu.com/v2transapi"
    def testzhen(self):
        params = {
        "from":"en",
        "to":"zh",
        "query": "study" #
    }
        url = "http://fanyi.baidu.com/v2transapi"
        r = requests.request("post", url, params=params)
        r=json.loads(r.text)
        print(r)
        assert  u'学习' in r['liju_result']['tag']
    def testzhen1(self):
        params = {
        "from":"en",
        "to":"h",
        "query": "stud" #
 }
        url = "http://fanyi.baidu.com/v2transapi"
        r = requests.request("post", url, params=params)
        r=json.loads(r.text)
        print(r)
        try:
            assert u'学习' in r['liju_result']['tag']
        except Exception:
            print("11111111111")
    def tearDown(self):
        pass
if __name__=='__main__':
    report_dir = r's.html'
    re_open = open(report_dir, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(Testbaiduapi)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=re_open,
        title=u'百度翻译api接口测试报告',
        description=u'百度翻译api接口测试详情'
    )
    runner.run(suite)