# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_c_student_center_study(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_c_student_center_study(self):
        u"""学员中心-学习记录"""

        # 传入参数
        #联系人电话号码
        # f = open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r')
        # student_phone = f.read()
        # f.close()
        student_phone = student_centre['student']

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
        # 点击用户名称
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/a/div').click()
        time.sleep(2)
# 学习记录
        driver.find_element_by_link_text('学习记录').click()
        time.sleep(2)
# 断言  -验证学习记录页面可以显示
        masg = driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/section/main/div/div[1]/div[1]/div/div/div/div/div[1]/div[1]').text
        print(masg)
        self.assertEqual(masg,'直播考勤')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

