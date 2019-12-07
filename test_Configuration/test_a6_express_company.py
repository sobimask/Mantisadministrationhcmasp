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


    def test_a_express_company(self):
        u"""快递公司-增加-修改-删除"""


        #新增校区名称
        express=configuration['express']
        #修改公司描述
        express_describe=configuration['express_describe']


        time.sleep(2)
        driver = self.driver
    #基础配置
        driver.find_element_by_xpath("//span[contains(.,'基础配置')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('快递公司').click()
        time.sleep(2)
    #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[1]/div/button').click()
        time.sleep(1)
        #快递公司
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(express)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#新增断言
        #查询
        driver.find_element_by_xpath("//input[@id='name']").click()
        driver.find_element_by_xpath("//input[@id='name']").send_keys(express)
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[1]').text
        print(masg)
        self.assertEqual(masg,express)
        time.sleep(2)
# 修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]/span/span[1]/a').click()
        time.sleep(2)
        #修改描述
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/textarea').send_keys(express_describe)
        time.sleep(1)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#修改断言-查询
        # 查询
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[1]/div/div/div[2]/div/span/input').clear()
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[1]/div/div/div[2]/div/span/input').send_keys(
            express)
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[2]/div/button[1]').click()
        time.sleep(2)
        masg = driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEqual(masg,express_describe)
        time.sleep(2)
# #删除  -删除
#         driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]/span/span[2]/a').click()
#         time.sleep(1)
#         #确定
#         driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
#         time.sleep(1)
# #删除断言  -查询
#         # 查询
#         driver.find_element_by_xpath(
#             '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[1]/div/div/div[2]/div/span/input').clear()
#         driver.find_element_by_xpath(
#             '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[1]/div/div/div[2]/div/span/input').send_keys(
#             express)
#         driver.find_element_by_xpath(
#             '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[2]/div/button[1]').click()
#         time.sleep(2)
#         #
#         masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/p').text
#         print(masg)
#         self.assertEqual(masg,'暂无数据')


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

