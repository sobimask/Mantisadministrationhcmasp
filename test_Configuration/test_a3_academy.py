# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_a_academy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_academy(self):
        u"""基础配置-学院配置"""


        #新增学院名称
        academy_name=configuration['academy_name']
        #修改学员名称
        macademy_name=configuration['macademy_name']
        driver = self.driver
    #基础配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[12]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_link_text('学院配置').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[1]/div/button').click()
        time.sleep(2)
        #学院名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()

        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(academy_name)
        #确定
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        driver.find_element_by_xpath('//*[@id="name"]').click()
        driver.find_element_by_xpath('//*[@id="name"]').send_keys(academy_name)
        time.sleep(1)
        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[2]/div/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEqual(masg,academy_name)
    #修改
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[4]/span/span/a').click()
        time.sleep(2)
        # 学院名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').clear()

        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(macademy_name)
        # 确定
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#修改断言
        driver.find_element_by_xpath('//*[@id="name"]').clear()
        driver.find_element_by_xpath('//*[@id="name"]').send_keys(macademy_name)
        time.sleep(1)
        # 查询
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[2]/div/button[1]').click()
        time.sleep(2)
        masg = driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEqual(masg,macademy_name)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

