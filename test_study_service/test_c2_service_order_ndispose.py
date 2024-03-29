# -*- coding: utf-8 -*-
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_c_service_order_dispose(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_c_service_order_dispose(self):
        u"""学员中心-客服单管理-处理客服单"""

        # 传入参数
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r', encoding='utf-8')
        student_phone = f.read()
        f.close()
        time.sleep(2)
        driver = self.driver
        time.sleep(1)
    # 学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
     # 查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        driver.find_element_by_xpath(
            "//button[contains(.,'查 询')]").click()
        time.sleep(2)
    # 获取订单id
        id = driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]/span').text
        time.sleep(1)
    #客服单管理
        driver.find_element_by_link_text('客服单管理').click()
        time.sleep(2)
        # 更多查询条件
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[12]/button[5]').click()
        time.sleep(1)
        #查询
        driver.find_element_by_id('mspCustomerId').click()
        driver.find_element_by_id('mspCustomerId').send_keys(id)
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(1)
        #处理
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr/td/span/span[2]/a').click()
        time.sleep(4)
        #状态
        driver.find_element_by_xpath("(//div[@id='statusCode']/div/div)[2]").click()
        driver.find_element_by_xpath("//li[contains(.,'已处理')]").click()
        time.sleep(1)
        #处理结果
        driver.find_element_by_xpath('//*[@id="dealRemark"]').click()
        driver.find_element_by_xpath('//*[@id="dealRemark"]').send_keys('已完成')
        #确定
        driver.find_element_by_xpath("//button[contains(.,'保 存')]").click()
        time.sleep(4)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span[2]').text
        print(masg)
        self.assertEqual(masg,'已处理')
        self.asset
    def tearDown(self):

        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

