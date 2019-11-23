# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import financial_management,student_centre
from lib.add_student_allpy import add_student_allpy
from selenium import webdriver
import unittest
import time

class test_c_invoice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_c_invoice(self):
        u"""财务管理-发票管理—开票"""

#传入参数
        #新增学员电话号码
        student_phone=financial_management['invoice']
        #新增学员姓名
        student_name=student_centre['name']
        #班型选择
        student_class=student_centre['class1']
        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']
        # 发票金额
        invoice = student_centre['invoice']
        # 发票内容
        invoice_content = student_centre['invoice_content']


        #d调取新增用户-报名
        add_student_allpy(self, student_name, student_phone, student_class, assessment, paid)

        driver = self.driver
        time.sleep(1)
# 发票
        driver.find_element_by_link_text('发票').click()
        time.sleep(2)
        # 发票申请
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/section/main/section/div/div/header/div/div/h2/button').click()
        time.sleep(2)
        # 发票类型  电子发票
        driver.find_element_by_xpath('//*[@id="typeCode"]/label[2]').click()
        time.sleep(2)
        # 发票抬头
        driver.find_element_by_css_selector('#titleTypeCode > label:nth-child(1)').click()
        time.sleep(1)
        # 发票金额
        driver.find_element_by_id('amount').click()
        driver.find_element_by_id('amount').send_keys(invoice)
        time.sleep(1)
        # 发票内容
        driver.find_element_by_id('content').click()
        driver.find_element_by_id('content').send_keys(invoice_content)
        time.sleep(1)
        # 发票抬头
        driver.find_element_by_id('title').click()
        driver.find_element_by_id('title').send_keys('螳螂科技')
        time.sleep(1)
        # 纳税人识别码
        driver.find_element_by_id('dutyParagraph').click()
        driver.find_element_by_id('dutyParagraph').send_keys(student_phone)
        time.sleep(1)
        # 手机
        driver.find_element_by_id('phone').click()
        driver.find_element_by_id('phone').send_keys(student_phone)
        time.sleep(1)
        # 保存
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#财务管理
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[20]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_link_text('发票管理').click()
        time.sleep(2)
        #查询
        driver.find_element_by_xpath('//*[@id="phone"]').click()
        driver.find_element_by_xpath('//*[@id="phone"]').send_keys(student_phone)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[4]/div/button[1]').click()
        time.sleep(2)
        #开票
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[14]/span/span/a[1]').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]').text
        print(masg)
        self.assertEqual(masg,"已开票")
        time.sleep(2)
#作废
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[14]/span/span[2]/a').click()
        time.sleep(2)
        #确定
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(2)
        #弹窗
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div/div/div[2]/button').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

