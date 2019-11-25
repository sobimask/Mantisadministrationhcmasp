# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_a_work_order_type(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_work_order_type(self):
        u"""基础配置-工单类型-增加-修改"""


        #新增服务商
        work_order=configuration['work_order']

        driver = self.driver
    #基础配置
        driver.find_element_by_xpath("//span[contains(.,'基础配置')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('工单类型').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/div/button').click()
        time.sleep(2)
        #工单类型名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(work_order)
        #描述
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').send_keys('新增工单类型')
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[2]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[2]/div/div[2]/div/span/input').send_keys(work_order)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[3]/button[1]').click()
        time.sleep(2)
        #
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEqual(masg,work_order)
        time.sleep(2)
#修改--修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[4]/span/span/a').click()
        time.sleep(1)
        #修改备注信息
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').send_keys('修改备注信息')
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(3)
#修改断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]').text
        print(masg)
        self.assertEquals(masg,'修改备注信息')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

