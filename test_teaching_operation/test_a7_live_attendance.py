# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time


class test_a_live_attendance(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_live_attendance(self):
        u"""教学运营-直播考勤"""

        driver = self.driver
    #教学运营
        driver.find_element_by_xpath("//span[contains(.,'教学运营')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('直播考勤').click()
        time.sleep(2)
        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div/div[9]/button[1]').click()
        time.sleep(1)



    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

