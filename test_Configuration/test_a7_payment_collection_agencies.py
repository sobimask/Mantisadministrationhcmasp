# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_a_express_company(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_express_company(self):
        u"""基础配置-支付配置-收款机构-增加-修改"""


        #新增收款机构
        collection =configuration['collection']
        #修改备注
        collection_remark=configuration['collection_remark']
        driver = self.driver
    #基础配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[12]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_link_text('支付配置').click()
        time.sleep(2)
        #收款机构
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/header/ul/li[6]/a').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/div/div/div/div/div/div/div/div/div[1]/div/button').click()
        time.sleep(2)
        #收款机构
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(collection)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/div/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/div/form/div[1]/div/div/div[2]/div/span/input').send_keys(collection)
        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/div/form/div[2]/div/button[1]').click()
        time.sleep(2)
        #
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[1]').text
        print(masg)
        self.assertEqual(masg,collection)
        time.sleep(2)
#修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]/span/span[1]/a').click()
        time.sleep(2)
        #修改描述
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').send_keys(collection_remark)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#修改断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEquals(masg,collection_remark)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

