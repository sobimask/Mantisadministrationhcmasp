# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import financial_management,student_centre,study_service
from lib.addpayment import addpayment
from selenium import webdriver
import unittest
import time


class test_b_return_manage_affirm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_b_return_manage_affirm(self):
        u"""财务管理-退费管理-查看记录-确认"""

#传入参数
        #新增学员电话号码
        student_phone=financial_management['return']
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

        driver = self.driver
        time.sleep(5)  #增加等待时间，防止通知遮挡元素
#学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(2)
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
        #查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[21]/button[1]').click()   #查询按钮26改为21
        time.sleep(2)
        #获取订单id
        id=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]').text
        time.sleep(1)
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
# 财务管理
        driver.find_element_by_xpath("//span[contains(.,'财务管理')]").click()
        time.sleep(2)
        driver.find_element_by_link_text('退费管理').click()
        time.sleep(2)
        #查询
        driver.find_element_by_xpath('//*[@id="mspCustomerId"]').click()
        driver.find_element_by_xpath('//*[@id="mspCustomerId"]').send_keys(id)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[7]/button[1]').click()
        time.sleep(2)
        #查看记录
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr/td/div/span[2]/span/a').click()
        time.sleep(2)
#查看记录断言
        masg=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div').text
        print(masg)
        self.assertEqual(masg,'退费记录')
        time.sleep(1)
        #取消
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button').click()
        time.sleep(2)
        #确认
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr/td/div/span[1]/a').click()
        time.sleep(2)
        #打款金额
        driver.find_element_by_id('amount').click()
        driver.find_element_by_id('amount').send_keys('2998')
        time.sleep(1)
        #打款时间
        driver.find_element_by_xpath('//*[@id="bizTime"]/div/input').click()
        driver.find_element_by_link_text('今天').click()
        time.sleep(1)
        #预计到账时间
        driver.find_element_by_xpath('//*[@id="expectTime"]/div/input').click()
        driver.find_element_by_link_text('今天').click()
        time.sleep(1)
        #保存
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言 --状态
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td[1]/span[2]').text
        print(masg)
        self.assertEqual(masg,"已打款")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

