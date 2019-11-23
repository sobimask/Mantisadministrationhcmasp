# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from lib.add_student_allpy import add_student_allpy
from selenium import webdriver
import unittest
import time

class test_a_student_center_apply_freeze(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_student_center_apply_freeze(self):
        u"""学员中心-报名-冻结"""
#传入参数
        #新增学员电话号码
        student_phone=student_centre['freeze']
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
        time.sleep(1)
    #点击报名
        driver.find_element_by_xpath('//*[@id="student-detail-menu"]/ul/li[10]/a').click()
        time.sleep(1)
        #冻结
        driver.find_element_by_xpath('//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div/div[1]/div/div[2]/div/button[1]').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div/div[1]/div/div[2]/div/button[1]').text
        print(masg)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

