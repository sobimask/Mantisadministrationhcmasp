# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time


class test_a_present_service(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_present_service(self):
        u"""教学运营-赠送服务"""


        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'r', encoding='utf-8')
        name2 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\commodity_name2.txt', 'r', encoding='utf-8')
        commodity_name2 = f.read()
        f.close()
        #赠送商品名称


        driver = self.driver
    #教学运营
        driver.find_element_by_xpath("//span[contains(.,'教学运营')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('赠送服务').click()
        time.sleep(2)
        #新增赠送任务
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/div/button[1]').click()
        time.sleep(2)
    #选择赠送商品学员  购买商品  一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/dl/dd/div/div[1]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name1+"')]").click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/dl/dd/div/div[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name2+"')]").click()
        #选择商品
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/dl/dd/div/div[3]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(2)
    #选择赠送服务
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/button[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(commodity_name2)
        time.sleep(1)
        #
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/span/label/span/input').click()
        #确认
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        #确认
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        #确认提示
        driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(1)
        #赠送成功
        driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button').click()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

