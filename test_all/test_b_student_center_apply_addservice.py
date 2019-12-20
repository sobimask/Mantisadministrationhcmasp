# -*- coding: utf-8 -*-
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
        driver.find_element_by_xpath("//button[contains(.,'新增客服单')]").click()
        time.sleep(1)
        #客服单时间
        driver.find_element_by_xpath("//span[@id='bizDate']/div/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'今天')]").click()
        time.sleep(1)
        #客服单类型
        driver.find_element_by_xpath("//div[@id='typeCode']/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'投诉')]").click()
        time.sleep(1)
        #紧急程度
        driver.find_element_by_xpath("//div[@id='urgencyCode']/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'一般')]").click()
        time.sleep(1)
        #客服单内容
        driver.find_element_by_id('content').send_keys('客服单内容')
        time.sleep(1)
        #负责机构
        driver.find_element_by_xpath("//div[@id='ownerOrgId']/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[6]/div/div/div/ul/li').click()
        time.sleep(1)
        #抄送人
        driver.find_element_by_xpath("//div[@id='copyUserId']/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[7]/div/div/div/ul/li').click()
        time.sleep(1)
        #123字段
        driver.find_element_by_id('expandOne').send_keys('123')
        time.sleep(1)
        #234字段
        driver.find_element_by_id('expandSix').send_keys('234')
        time.sleep(1)
        #保存
        driver.find_element_by_xpath("//button[contains(.,'保 存')]").click()
        time.sleep(3)
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

