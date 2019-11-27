# -*- coding: utf-8 -*-
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time
import os


class test_a_student_name(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_student_name(self):
        u"""支付管理-支付确认-点击学员姓名"""

#传入参数
        #新增学员电话号码
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student1.txt', 'r', encoding='utf-8')
        student_phone = f.read()
        f.close()        #修改查询电话号码

        time.sleep(2)
        driver = self.driver
        time.sleep(2)
#财务管理
        driver.find_element_by_xpath("//span[contains(.,'财务管理')]").click()
        time.sleep(2)
        driver.find_element_by_link_text('支付确认').click()
        time.sleep(1)
        #查询
        driver.find_element_by_id('phone').click()
        driver.find_element_by_id('phone').send_keys(student_phone)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div/button[1]').click()
        time.sleep(2)
        #点击学员姓名
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[8]/a').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/section/main/section/header/div/div/div/label/span[2]').text
        print(masg)
        self.assertIsNotNone(masg,' ')


    def tearDown(self):
        os.remove('D:\\Mantisadministrationhcmasp\\configFile\\student1.txt')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

