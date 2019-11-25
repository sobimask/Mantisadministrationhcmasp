# -*- coding: utf-8 -*-
from lib.login import electronic_login
from lib.add_student_allpy import add_student_allpy
from configFile.config_account_and_content import study_service,student_centre
from selenium import webdriver
import unittest
import time



class test_a_order_mansge_addpllay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_order_mansge_addpllay(self):
        u"""学服中心-订单管理-增加报考"""

#传入参数
        #新增学员电话号码
        student_phone=study_service['addpllay']
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
        #报考
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td/div/a[2]').click()
        time.sleep(1)
        #新增
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/button').click()
        time.sleep(1)
        #报考年份
        driver.find_element_by_id('candidateYear').click()
        time.sleep(1)
        driver.find_element_by_id('candidateYear').send_keys('2019')
        time.sleep(1)
        #报考省份
        driver.find_element_by_xpath('//*[@id="provinceId"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        time.sleep(1)
        #报考类型
        driver.find_element_by_xpath('//*[@id="candidateType"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[12]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #是否报考
        driver.find_element_by_xpath('//*[@id="iscandidate"]/label[1]/span[1]/input').click()
        #报考资料提交
        driver.find_element_by_xpath('//*[@id="candidateDataSubmit"]/label[1]/span[1]/input').click()
        #保存
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text
        print(masg)
        self.assertIsNotNone(masg,' ')
        #关闭
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button').click()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

