# -*- coding: utf-8 -*-
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time

class test_b_textbook_scene(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)
    def test_b_textbook_scene(self):
        u"""学服中心-补发教材-现场补发"""

#传入参数
        #新增学员电话号码
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student2.txt', 'r', encoding='utf-8')
        student_phone = f.read()
        f.close()
        time.sleep(2)
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
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[21]/button[1]').click()
        time.sleep(2)
        #获取订单id
        id=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]/span').text
        time.sleep(1)
#教材补发
        driver.find_element_by_link_text('教材补发').click()
        time.sleep(2)
        #根据客户id进行查询'
        driver.find_element_by_id('mspCustomerId').click()
        driver.find_element_by_id('mspCustomerId').send_keys(id)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div[3]/button[2]').click()
        time.sleep(2)
    #现场发放
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[11]/span/a[2]').click()
        time.sleep(2)
        #获取补发教材名称
        book=driver.find_element_by_xpath('//*[@id="bookes"]/label[1]/span[2]').text

        #选择教材
        driver.find_element_by_xpath('//*[@id="bookes"]/label[1]/span[1]/input').click()

        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[9]').text
        print(masg)
        self.assertNotIn(masg,book)


    def tearDown(self):

        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

