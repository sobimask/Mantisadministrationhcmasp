# -*- coding: utf-8 -*-
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_a_network_school(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_network_school(self):
        u"""基础配置-网校配置"""

        driver = self.driver
    #基础配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[12]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_link_text('网校配置').click()
        time.sleep(2)
        #保存
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/div/div[2]/button').click()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

