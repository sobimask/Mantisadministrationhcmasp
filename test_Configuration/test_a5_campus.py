# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_a_campus(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_campus(self):
        u"""基础配置-校区配置"""


        #新增校区名称
        campus=configuration['campus']
        #服务商名称                新增服务商数据保存调用
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\service_provider.txt', 'r', encoding='utf-8')
        service_provider = f.read()
        f.close()

        driver = self.driver
        time.sleep(2)
    #基础配置
        driver.find_element_by_xpath("//span[contains(.,'基础配置')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('校区配置').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[1]/div/button').click()
        time.sleep(2)
        #校区名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(campus)
        #服务商
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[text()="'+service_provider+'"]').click()
        time.sleep(2)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)
        #断言
        driver.find_element_by_xpath('//*[@id="name"]').send_keys(campus)
        time.sleep(2)
        #查询
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEqual(masg,campus)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

