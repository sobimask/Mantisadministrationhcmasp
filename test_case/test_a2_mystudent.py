# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time

class test_a1_term_plan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a1_term_plan(self):
        u"""教学运营-学期计划"""


        #计划名称
        plan_name=teaching_operation['plan_name']
        #修改计划名称
        mplan_name = teaching_operation['mplan_name']


        time.sleep(2)
        driver = self.driver
    #教学运营
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[14]/div').click()
        time.sleep(1)
        driver.find_element_by_link_text('我的学员').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

