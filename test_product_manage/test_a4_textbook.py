# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time
from lib.randomphone import randomphone

class test_a4_textbook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a4_textbook(self):
        u"""产品管理-教材教辅—新增-修改"""

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()


        #修改教材价格
        textbook_money=product_manage['textbook_money']
        driver = self.driver
    #产品管理

        driver.find_element_by_xpath("//span[contains(.,'产品管理')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('教材教辅').click()
        time.sleep(2)
        for i in range(4):
            if i < 4:
                # 新增教材名称
                textbook_name='测试教材'+randomphone()
                #新增
                driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[1]/div/button[2]').click()
                time.sleep(1)
                #教材名称
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').send_keys(textbook_name)
                #一级项目
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('//li[text()="' + name1 + '"]').click()
                #价格
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').send_keys(128)
                #作者
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/span/input').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/span/input').send_keys('xier')
                #保存
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
                time.sleep(2)
                #查询
                driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[1]/div[1]/div/div[2]/div/span/input').clear()
                driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[1]/div[1]/div/div[2]/div/span/input').send_keys(textbook_name)
                driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div[2]/div[2]/button[1]').click()
                time.sleep(2)
                #断言
                masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[3]').text
                print(masg)
                self.assertEqual(masg,textbook_name)
                time.sleep(2)
                #修改
                driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[11]/span/span/a').click()
                time.sleep(2)
                #修改价格
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').clear()
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/input').send_keys(textbook_money)
                #保存
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
                time.sleep(2)
                #断言
                masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[6]').text
                print(masg)
                self.assertEqual(masg,textbook_money)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

