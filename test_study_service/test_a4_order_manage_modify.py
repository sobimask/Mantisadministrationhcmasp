# -*- coding: utf-8 -*-
from lib.login import electronic_login
from lib.add_student_allpy import add_student_allpy
from configFile.config_account_and_content import study_service,student_centre
from selenium import webdriver
import unittest
import time

class test_a_order_manage_modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_order_manage_modify(self):
        u"""学服中心-订单管理-修改支付详情"""

#传入参数
        #新增学员电话号码
        student_phone=study_service['modify']
        #新增学员姓名
        student_name=student_centre['name']
        #班型选择
        student_class=student_centre['class1']
        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']
        #修改支付信息-备注信息内容
        modify_remark=study_service['modify_remark']

        #d调取新增用户-报名
        add_student_allpy(self, student_name, student_phone, student_class, assessment, paid)

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
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[26]/button[1]').click()
        time.sleep(2)
        #修改支付详情
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td/div/span[2]/a').click()
        time.sleep(1)
        #
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[14]/span/span[1]/a').click()
        time.sleep(1)
        #修改备注
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[8]/div/div/div[2]/div/span/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[8]/div/div/div[2]/div/span/textarea').send_keys(modify_remark)
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(3)
#断言
        masg=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[11]').text
        print(masg)
        self.assertEqual(masg,modify_remark)
        #取消
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button').click()


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

