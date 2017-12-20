# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: ExclusiveOperation.py
@time: 2017/12/20 22:49
@项目名称:operating
"""
class exclusiveoperation(object):
    def setStart(self):
        pass

    def setStop(self):
        pass


    def is_not_visible_css_selectop(self, locator, timeout=5):
        # 一直等待某个元素消失，默认超时10秒
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False