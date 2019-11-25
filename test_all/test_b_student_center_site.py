
# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_a_student_center_add_site(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_student_center_add_site(self):
        u"""学员中心-增加收货地址"""

#传入参数
        #收货联系人电话号码
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r')
        student_phone = f.read()
        f.close()

        #收货人姓名
        student_name=student_centre['name']
        #增加收货地址
        student_site=student_centre['site']
        #修改收货人姓名
        student_namem=student_centre['namem']


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
#新增收货地址
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/section/main/section/main/div/div/div[2]/div[1]/button').click()
        time.sleep(2)
        #收货人
        driver.find_element_by_id('addressee').click()
        driver.find_element_by_id('addressee').send_keys(student_name)
        time.sleep(1)
        #联系方式
        driver.find_element_by_id('addresseeNumber').click()
        driver.find_element_by_id('addresseeNumber').send_keys(student_phone)
        time.sleep(1)
        #地址
        driver.find_element_by_id('address').click()
        driver.find_element_by_id('address').send_keys(student_site)
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/section/main/section/main/div/div/div[2]/div[2]/div/div/div[2]/p[3]').text
        print(masg)
        self.assertIn(student_site,masg)
#
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

