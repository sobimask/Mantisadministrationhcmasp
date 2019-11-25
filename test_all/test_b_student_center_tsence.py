# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_b_student_center_tsence(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_b_student_center_tsence(self):
        u"""学员中心-报名-现场发放"""

        # 传入参数
        #联系人电话号码
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r')
        student_phone = f.read()
        f.close()

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
# 报名
        driver.find_element_by_link_text('报名').click()
        time.sleep(2)
#现场发发放
        driver.find_element_by_xpath('//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/span/button[2]').click()
        time.sleep(2)
     #选择教材
        textbook=driver.find_element_by_xpath('//*[@id="bookes"]/label[1]/span[2]').text
        driver.find_element_by_xpath('//*[@id="bookes"]/label[1]/span[1]/input').click()
        time.sleep(1)

        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)
#断言
        #学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
        #查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[21]/button[1]').click()
        time.sleep(1)
        id=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]/span').text
        print(id)
        time.sleep(1)
        #教材补发
        driver.find_element_by_link_text('教材补发').click()
        time.sleep(2)
        #根据ID查询
        driver.find_element_by_id('mspCustomerId').click()
        driver.find_element_by_id('mspCustomerId').send_keys(id)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        #
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[9]/div').text
        print(masg)
        self.assertNotEqual(textbook,masg)
        time.sleep(1)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

