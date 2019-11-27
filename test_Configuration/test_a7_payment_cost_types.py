# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_a_payment_cost_types(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_payment_cost_types(self):
        u"""基础配置-支付配置--费用类型-增加-修改"""


        #新增支付类型
        cost_types=configuration['cost_types']
        driver = self.driver
        #基础配置
        driver.find_element_by_xpath("//span[contains(.,'基础配置')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('支付配置').click()
        time.sleep(2)
        #费用类型
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/header/ul/li[4]/a').click()
        time.sleep(2)
        #支付类型-新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/div/button').click()
        time.sleep(2)
        #名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/input').send_keys(cost_types)
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        #断言---查询
        driver.find_element_by_id('name').click()
        driver.find_element_by_id('name').send_keys(cost_types)
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]').text
        print(masg)
        self.assertEqual(masg,cost_types)

        #支付方式
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/header/ul/li[2]').click()
        #修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[8]/span/a[1]').click()
        time.sleep(2)
        #是否算流水
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/label/span[1]/input').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        driver.find_element_by_css_selector('body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary').click()
        time.sleep(2)
        #修改断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[4]').text
        print(masg)
        self.assertEqual(masg,'否')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

