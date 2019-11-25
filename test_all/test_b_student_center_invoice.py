# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time
class test_c_student_center_invoice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_c_student_center_invoice(self):
        u"""学员中心-发票"""

        # 传入参数
        #联系人电话号码
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r')
        student_phone = f.read()
        f.close()
        #发票金额
        invoice = student_centre['invoice']
        #发票内容
        invoice_content=student_centre['invoice_content']

        driver = self.driver
        time.sleep(1)
        # 学员中心
        driver.find_element_by_link_text('学员中心').click()
        time.sleep(2)
        # 查询
        driver.find_element_by_id('searchMess').clear()
        driver.find_element_by_id('searchMess').send_keys(student_phone)
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/header/div/form/div/div[2]/div/div/div/span/button[1]').click()
        time.sleep(2)
        #点击用户名称
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/a/div').click()
        time.sleep(2)
#发票
        driver.find_element_by_link_text('发票').click()
        time.sleep(2)
        #发票申请
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/section/main/section/div/div/header/div/div/h2/button').click()
        time.sleep(2)
        #发票类型  电子发票
        driver.find_element_by_xpath('//*[@id="typeCode"]/label[2]').click()
        time.sleep(2)
       #发票抬头
        driver.find_element_by_css_selector('#titleTypeCode > label:nth-child(1)').click()
        time.sleep(1)
        #发票金额
        driver.find_element_by_id('amount').click()
        driver.find_element_by_id('amount').send_keys(invoice)
        time.sleep(1)
        #发票内容
        driver.find_element_by_id('content').click()
        driver.find_element_by_id('content').send_keys(invoice_content)
        time.sleep(1)
        #发票抬头
        driver.find_element_by_id('title').click()
        driver.find_element_by_id('title').send_keys('螳螂科技')
        time.sleep(1)
        #纳税人识别码
        driver.find_element_by_id('dutyParagraph').click()
        driver.find_element_by_id('dutyParagraph').send_keys(student_phone)
        time.sleep(1)
        #手机
        driver.find_element_by_id('phone').click()
        driver.find_element_by_id('phone').send_keys(student_phone)
        time.sleep(1)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)

# 断言
        masg = driver.find_element_by_xpath('//*[@id="reservation"]/ul/li/div[3]/div/div[2]/div[1]/div[1]').text
        print(masg)
        self.assertIsNotNone('已申请',masg)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

