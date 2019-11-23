# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_a_payment_way(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_payment_way(self):
        u"""基础配置-支付配置--支付方式-增加-修改"""


        #新增支付方式
        payment_way=configuration['payment_way']

        driver = self.driver
    #基础配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[12]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_link_text('支付配置').click()
        time.sleep(2)
        #支付方式-新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/button').click()
        time.sleep(2)
        #支付方式
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(payment_way)
        #手续费
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/span/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/span/span/input').send_keys(10)
        #是否需要小票单号
        driver.find_element_by_xpath('//*[@id="ticketNeed"]/label[1]/span[1]/input').click()
        time.sleep(2)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)
        #提交确认
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(2)

#断言--查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/header/form/div/div[1]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/header/form/div/div[1]/div/div[2]/div/span/input').send_keys(payment_way)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/header/form/div/div[2]/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEquals(masg,payment_way)
        time.sleep(2)
#修改支付方式
        driver.find_element_by_link_text('修改').click()
        time.sleep(2)
        #修改手续费
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/span/span/input').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/span/span/input').send_keys(5)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        #提交确认
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(2)
#修改断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]').text
        print(masg)
        self.assertEquals(masg,'5%')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

