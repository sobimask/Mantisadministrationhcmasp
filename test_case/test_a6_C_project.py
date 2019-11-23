# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from configFile.config_account_and_content import *
from lib.login import *
import os


class test_a6_C_project(unittest.TestCase):
    def setUp(self):
        self.driver = my_driver
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_a6_C_project(self):
        u"""基础配置-报考项目"""


        #报考规则名称
        C_projectus=configuration['C_project']

        # 用户登录
        electronic_login(self)
        time.sleep(2)
        driver = self.driver
    #基础配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[11]/div').click()
        time.sleep(1)
        driver.find_element_by_link_text('报考项目').click()
        time.sleep(2)
        #新增报考类目
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[1]/div/div/button').click()

        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button[2]/span//*[@text="ACI营养"]').click()
        time.sleep(2)

        #报考规则名称
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/div/div[2]/div/span/input').send_keys(C_projectus)
        #学历
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div/div[4]/div[1]/div/div[1]/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #专业
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div/div[4]/div[1]/div/div[2]/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #补考规则设置
        driver.find_element_by_xpath('//*[@id="retakeRule"]/label[1]/span[1]/input').click()
        time.sleep(1)
        #报考考期配置
        driver.find_element_by_xpath('//*[@id="examDateList"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #确定
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div/div[7]/div/button[2]').click()






        # # 退出系统
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/header/div[2]/div/ul/li[11]/span/span[3]').click()
        # time.sleep(2)
        # driver.find_element_by_link_text('退出').click()
        # time.sleep(2)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

