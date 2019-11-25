# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_all_add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_all_add_user(self):
        u"""全局—新增用户"""


        #新增学员电话号码

        student_phone = student_centre['student']

        with open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'w') as f:
            f.write(student_phone)
            f.close()
        #新增学员姓名
        student_name=student_centre['name']


        time.sleep(2)
        driver = self.driver
        #新增学员
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/header/div[2]/div/ul/li[1]/button').click()
        time.sleep(1)
        #姓名
        driver.find_element_by_id('name').click()
        driver.find_element_by_id('name').send_keys(student_name)
        #上课手机号
        driver.find_element_by_id('account').click()
        driver.find_element_by_id('account').send_keys(student_phone)
        time.sleep(1)
        #地域
        driver.find_element_by_xpath('//*[@id="area"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #学院
        driver.find_element_by_xpath('//*[@id="collegeId"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #来源
        driver.find_element_by_xpath('//*[@id="mscCode"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #咨询项目
        driver.find_element_by_xpath('//*[@id="consultId"]/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #校区
        driver.find_element_by_xpath('//*[@id="campusId"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(5)
#全局检查新增学员
        # 查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/header/div[2]/div/ul/li[2]/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/header/div[2]/div/ul/li[2]/span/input').send_keys(student_phone)
        time.sleep(3)
        name=driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div[2]/div/ul/li/div[1]/div/span').text
        print(name)
        self.assertEqual(name,student_name)
        time.sleep(2)
#学员中心检查学员
        driver.find_element_by_link_text('学员中心').click()
        time.sleep(2)
        #查询
        driver.find_element_by_id('searchMess').clear()
        driver.find_element_by_id('searchMess').send_keys(student_phone)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/header/div/form/div/div[2]/div/div/div/span/button[1]').click()
        time.sleep(2)
        #
        name=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/a/div').text
        print(name)
        self.assertEqual(name,student_name)
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

