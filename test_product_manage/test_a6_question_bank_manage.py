# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time


class test_a6_question_bank_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a6_question_bank_manage(self):
        u"""产品管理-题库管理—新增-修改"""
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'r', encoding='utf-8')
        name2 = f.read()
        f.close()

        #新增题库名称
        quest_bank_name=product_manage['quest_bank_name']
        #修改科目
        mquest_bank_name=product_manage['mquest_bank_name']

        driver = self.driver
    #产品管理
        driver.find_element_by_xpath("//span[contains(.,'产品管理')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('题库管理').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/button[2]').click()
        time.sleep(2)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[text()="' + name1 + '"]').click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[text()="' + name2 + '"]').click()
        #题库名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').send_keys(quest_bank_name)
        #包含科目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #免费题库
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[1]/div/div[2]/div/span/div/label[1]/span[1]/input').click()

        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#查询
        driver.find_element_by_id('name').click()
        driver.find_element_by_id('name').send_keys(quest_bank_name)
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)
    #d断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]').text
        print(masg)
        self.assertEqual(masg,quest_bank_name)
        time.sleep(2)
#修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[13]/div/span[1]/a').click()
        time.sleep(2)
        # 题库名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').send_keys(mquest_bank_name)
        # 保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)

        # 查询
        driver.find_element_by_id('name').clear()  #修改清空上次输入框查数据
        driver.find_element_by_id('name').send_keys(mquest_bank_name)
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)
        # d断言
        masg = driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]').text
        print(masg)
        self.assertEqual(masg, mquest_bank_name)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

