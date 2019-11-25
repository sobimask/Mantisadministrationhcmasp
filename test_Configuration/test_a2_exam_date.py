# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_a_exam_date(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_exam_date(self):
        u"""基础配置—考期配置-新增考期"""


        #一级项目名称
        f =  open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r')
        name1 =f.read()
        f.close()


        print(name1)
        #查询考期配置
        exam=configuration['exam']

        time.sleep(2)
        driver = self.driver
    #基础配置
        driver.find_element_by_xpath("//span[contains(.,'基础配置')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('考期配置').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[1]/div/button').click()
        time.sleep(3)
        #增加考期
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//li[text()="'+name1+'"]').click()
        time.sleep(1)
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #考期
        driver.find_element_by_xpath('//*[@id="examDate"]/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]').click()
        time.sleep(1)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

