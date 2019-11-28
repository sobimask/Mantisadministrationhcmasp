# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from lib.addpayment import addpayment
from selenium import webdriver
import unittest
import time

class test_a_student_center_apply_return(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_student_center_apply_return(self):
        u"""学员中心-报名-退费"""

        #传入参数
        #新增学员电话号码
        student_phone=student_centre['return']
        #新增学员姓名
        student_name=student_centre['name']
        #班型选择
        student_class=student_centre['class1']
        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']

        #d调取新增用户-报名
        addpayment(self, student_name, student_phone, assessment, paid)

        driver = self.driver
        time.sleep(1)
    #点击报名
        driver.find_element_by_xpath('//*[@id="student-detail-menu"]/ul/li[10]/a').click()
        time.sleep(1)
        #点击操作
        driver.find_element_by_xpath('//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(1)
        #退费
        driver.find_element_by_xpath('/html/body/div[9]/div/div/ul/li[3]').click()
        time.sleep(2)  #新增等待
        #扣费金额
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div/div[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div/div[2]/input').send_keys(1)
        time.sleep(1)
        #收款人
        driver.find_element_by_id('payee').click()
        driver.find_element_by_id('payee').send_keys(student_name)
        #收款方式
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="categoryId"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #收款账号
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div/div/div[2]/div/span/input').send_keys(student_phone)
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div/div[1]/div/div[1]/div/span[1]/div').text
        print(masg)
        self.assertEqual(masg,'已退费')



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

