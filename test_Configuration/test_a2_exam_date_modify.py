# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_a2_exam_date_modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a2_exam_date_modify(self):
        u"""基础配置—考期配置-修改考期"""


        #一级项目名称
        name1=configuration['name1']

        driver = self.driver
    #基础配置
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[12]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_link_text('考期配置').click()
        time.sleep(2)
#查询
        #一级项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/section/main/div/div/form/div/div[1]/div/div[2]/div/span/div/div/div').click()
        time.sleep(5)
        driver.find_element_by_xpath('//li[text()="'+name1+'"]').click()
        time.sleep(1)
        #二级项目
        driver.find_element_by_xpath('//*[@id="secondProductId"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()

        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[3]/button[1]').click()
        time.sleep(2)
    #修改
        #获取当前考期时间
        old_date=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[4]').text
        print(old_date)
        #修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[6]/a').click()
        time.sleep(2)
        #考期
        driver.find_element_by_xpath('//*[@id="examDate"]/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[3]/a').click()
        #保存
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        new_date=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[4]').text
        print(new_date)
        self.assertNotEqual(new_date,old_date)




    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

