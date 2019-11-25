# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_b_student_center_apply_addservice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_b_student_center_apply_addservice(self):
        u"""学员中心-报名-增加客服单"""

        # 传入参数
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r')
        student_phone = f.read()
        f.close()

        time.sleep(2)
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
#新增客服单
        driver.find_element_by_xpath('//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[1]/div/div[2]/div/button[1]').click()
        time.sleep(2)
        #客户单类型
        driver.find_element_by_xpath('//*[@id="typeCode"]/div/div/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #紧急程度
        driver.find_element_by_xpath('//*[@id="urgencyCode"]/div/div/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #客服单时间
        driver.find_element_by_xpath('//*[@id="bizDate"]/div/input').click()
        driver.find_element_by_link_text('今天').click()
        #负责机构
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ownerOrgId"]/div/div/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #抄送人
        driver.find_element_by_xpath('//*[@id="copyUserId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #客服单内容
        driver.find_element_by_id('content').click()
        driver.find_element_by_id('content').send_keys('新增客服单')
        time.sleep(1)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
#断言 检查客服单
        time.sleep(2)
        # 客服单
        driver.find_element_by_link_text('客服单').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="reservation"]/ul/li/div[3]/div/div[2]/div[1]/div[1]').text
        print(masg)
        self.assertIsNotNone(masg,' ')




    def tearDown(self):

        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

