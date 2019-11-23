# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_a_service_provider(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_service_provider(self):
        u"""基础配置-服务商配置"""


        #新增服务商
        service_provider=configuration['service_provider']

        time.sleep(2)
        driver = self.driver
    #基础配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[12]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_link_text('服务商配置').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/div/button').click()
        time.sleep(2)
        #服务商名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(service_provider)
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#新增服务商断言
        driver.find_element_by_id('name').click()
        driver.find_element_by_id('name').send_keys(service_provider)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[4]/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]/span').text
        print(masg)
        self.assertEqual(masg,service_provider)
#修改服务商
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[7]/span/span/a').click()
        time.sleep(2)
        #指定默认服务商
        driver.find_element_by_xpath('//*[@id="defaultFlag"]/label[1]/span[1]/input').click()
        time.sleep(1)
        #确认
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[6]').text
        print(masg)
        self.assertEqual(masg,'是')
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

