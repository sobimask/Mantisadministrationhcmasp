# -*- coding: utf-8 -*-
from lib.login import electronic_login
from lib.addpayment import addpayment
from configFile.config_account_and_content import study_service,student_centre
from selenium import webdriver
import unittest
import time


class test_a_order_manage_addpayment(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_order_manage_addpayment(self):
        u"""学服中心-订单管理-增加支付单"""

#传入参数
        #新增学员电话号码
        student_phone=study_service['addpayment']
        #新增学员姓名
        student_name=student_centre['name']
        #应缴费用
        assessment=study_service['assessment']
        #实缴费用
        paid=study_service['paid']
        #支付单补缴金额
        repair=study_service['repair']

        #d调取新增用户-报名
        addpayment(self, student_name, student_phone, assessment, paid)

        driver = self.driver
        time.sleep(8)  #增加通知消失时间
        #学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(1)
        #订单管理
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
        #查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[21]/button[1]').click()
        time.sleep(2)

        #支付单
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td/div/a[1]').click()
        time.sleep(1)
        #新增支付单
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/button').click()
        time.sleep(2)
        #新增支付金额
        driver.find_element_by_xpath('//*[@id="amount"]').click()
        driver.find_element_by_xpath('//*[@id="amount"]').send_keys(repair)
        #费用类型
        driver.find_element_by_xpath('//*[@id="feeTypeId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        time.sleep(1)
#断言

        masg=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[4]').text
        print(masg)
        self.assertIsNotNone(masg,' ')
        #取消
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

