# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import financial_management,student_centre
from lib.add_student_allpy import add_student_allpy
from selenium import webdriver
import unittest
import time


class test_a_affirm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_affirm(self):

        u"""支付管理-支付确认-确认"""

        #传入参数
        #新增学员电话号码
        student_phone=financial_management['affirm']
        #新增学员姓名
        student_name=student_centre['name']
        #班型选择
        student_class=student_centre['class1']
        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']

        #d调取新增用户-报名

        add_student_allpy(self, student_name, student_phone, student_class, assessment, paid)

        driver = self.driver
        time.sleep(8)
        #财务管理
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[20]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_link_text('支付确认').click()
        time.sleep(1)
        #查询
        driver.find_element_by_id('phone').click()
        driver.find_element_by_id('phone').send_keys(student_phone)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div/button[1]').click()
        time.sleep(2)
        #确认
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[2]/span[2]/a[1]').click()
        time.sleep(2)
        #确认
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        time.sleep(2)
        #
        #断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[4]').text
        print(masg)
        self.assertEqual(masg,"已确认")

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

