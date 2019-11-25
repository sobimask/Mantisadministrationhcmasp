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
        #服务商名称
        service_provider=configuration['service_provider']

        driver = self.driver
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
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)
#断言

        driver.find_element_by_xpath('//*[@id="name"]').send_keys(campus)
        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[2]/div/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEqual(masg,campus)
#修改校区配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[7]/span/span/a').click()
        time.sleep(2)
        #是否默认校区---修改为是默认校区
        driver.find_element_by_xpath('//*[@id="defaultFlag"]/label[2]/span[1]/input').click()
        time.sleep(1)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)
#修改后断言        #查询
        driver.find_element_by_xpath('//*[@id="name"]').clear()
        driver.find_element_by_xpath('//*[@id="name"]').send_keys(campus)
        # 查询
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[2]/div/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[4]').text
        print(masg)
        self.assertEquals(masg,('否'))



    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

