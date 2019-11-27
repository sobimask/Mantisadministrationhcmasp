# -*- coding: utf-8 -*-
from configFile.config_account_and_content import configuration
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_a_project1_add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_project1_add(self):
        u"""基础配置-项目配置-一级项目-二级项目"""


        #一级项目名称
        name1=configuration['name1']
        #二级项目名称
        name2=configuration['name2']

        with open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'w',encoding= 'utf-8') as f:
            f.write(name1)
            f.close()

        with open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'w',encoding= 'utf-8') as f:
            f.write(name2)
            f.close()
        driver = self.driver
    #基础配置
        driver.find_element_by_xpath("//span[contains(.,'基础配置')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('项目配置').click()
        time.sleep(2)
        #新增descInfo
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div[1]/div/button[3]').click()
        time.sleep(2)
        #名称
        driver.find_element_by_id('name').click()
        driver.find_element_by_id('name').send_keys(name1)
        #描述
        driver.find_element_by_id('descInfo').click()
        driver.find_element_by_id('descInfo').send_keys('测试')
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#二级项目
        driver.find_element_by_link_text('二级项目').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[1]/div/button[4]').click()
        time.sleep(2)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//li[text()="'+name1+'"]').click()
        #名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/span/input').send_keys(name2)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        driver.find_element_by_xpath('//*[@id="name"]').click()
        driver.find_element_by_xpath('//*[@id="name"]').send_keys(name2)
        time.sleep(1)
        #
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div/div[5]/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]').text
        print(masg)
        self.assertEqual(masg,name1)
        #二级项目断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[4]').text
        print(masg)
        self.assertEqual(masg,name2)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

