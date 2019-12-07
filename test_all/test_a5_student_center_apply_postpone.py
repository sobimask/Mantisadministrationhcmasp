# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
from lib.addpayment import addpayment
import unittest
import time



class test_a_student_center_apply_postpone(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_student_center_apply_postpone(self):
        u"""学员中心-报名-延期"""

#传入参数
        #新增学员电话号码
        student_phone=student_centre['postpone']
        #新增学员姓名
        student_name=student_centre['name']
        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']
        #延期时间
        postponetime=student_centre['time']

        #调取新增用户-报名
        addpayment(self, student_name, student_phone, assessment, paid)

        driver = self.driver
        time.sleep(1)
    #点击报名
        driver.find_element_by_xpath('//*[@id="student-detail-menu"]/ul/li[10]/a').click()
        time.sleep(1)
        # 点击操作
        driver.find_element_by_xpath(
            '//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(1)
        # 延期
        driver.find_element_by_xpath('/html/body/div[9]/div/div/ul/li[2]').click()
        time.sleep(1)
        #延期时间
        driver.find_element_by_xpath('//*[@id="expireDay"]/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/div[2]/div[2]/table/tbody/tr[6]/td[7]').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

