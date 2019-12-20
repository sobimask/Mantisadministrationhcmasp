# -*- coding: utf-8 -*-
from lib.login import electronic_login
from lib.addpayment import addpayment
from configFile.config_account_and_content import study_service,student_centre
from selenium import webdriver
import unittest
import time



class test_a_order_manage_return(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_order_manage_return(self):
        u"""学服中心-订单管理-退费"""

#传入参数
        #新增学员电话号码
        student_phone=study_service['return']
        #新增学员姓名
        student_name=student_centre['name']
        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']
        #退费-扣费金额
        return_money=study_service['return_money']

        #d调取新增用户-报名
        addpayment(self, student_name, student_phone, assessment, paid)
        time.sleep(5)
        driver = self.driver
        time.sleep(1)
#学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
        #查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        driver.find_element_by_xpath(
            "//button[contains(.,'查 询')]").click()
        time.sleep(2)
        #进入子订单
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span[2]').click()
        time.sleep(1)
        #退费
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr[2]/td/span/span[1]/a').click()
        time.sleep(1)
        #扣费金额
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div/div[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div/div[2]/input').send_keys(return_money)
        time.sleep(1)
        #收款人
        driver.find_element_by_id('payee').click()
        driver.find_element_by_id('payee').send_keys(student_name)
        #收款方式
        driver.find_element_by_xpath('//*[@id="categoryId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #收款账号
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div/div/div[2]/div/span/input').send_keys(student_phone)
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(5)
#d断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[2]/td').text
        print(masg)
        self.assertEqual(masg,'已退费')


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

