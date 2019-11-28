# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time

class test_a1_term_plan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a1_term_plan(self):
        u"""教学运营-学期计划-新增-修改"""

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'r', encoding='utf-8')
        name2 = f.read()
        f.close()
        #计划名称
        plan_name=teaching_operation['plan_name']
        #修改计划名称
        mplan_name = teaching_operation['mplan_name']


        driver = self.driver
    #教学运营
        driver.find_element_by_xpath("//span[contains(.,'教学运营')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('学期计划').click()
        time.sleep(2)
    #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/button[1]').click()
        time.sleep(2)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name1+"')]").click()
        time.sleep(1)
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name2+"')]").click()
        time.sleep(1)
        #计划名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/span/input').send_keys(plan_name)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        #查询
        driver.find_element_by_xpath('//*[@id="planName"]').click()
        driver.find_element_by_xpath('//*[@id="planName"]').send_keys(plan_name)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[3]/div/button[1]').click()
        time.sleep(2)
        #
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text
        print(masg)
        self.assertIsNotNone(masg,' ')
        time.sleep(2)
#修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[8]/div/span[1]/a').click()
        time.sleep(2)
        #修改计划名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/span/input').clear()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/span/input').send_keys(mplan_name)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(4)

#修改--断言
        #查询
        driver.find_element_by_xpath('//*[@id="planName"]').clear()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="planName"]').send_keys(mplan_name)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[3]/div/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text
        print(masg)
        self.assertEqual(masg,mplan_name)



    def tearDown(self):

        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

