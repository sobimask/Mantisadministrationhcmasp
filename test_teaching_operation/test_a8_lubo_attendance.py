# -*- coding: utf-8 -*-
from lib.login import electronic_login
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
        u"""教学运营-录播考勤"""
        driver = self.driver
    #教学运营
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[14]/div').click()
        time.sleep(1)
        driver.find_element_by_link_text('录播考勤').click()
        time.sleep(2)
        #进课时间
        driver.find_element_by_xpath('//*[@id="dateRange"]/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[6]').click()

        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/section/header/form/div/div[13]/button[1]').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

