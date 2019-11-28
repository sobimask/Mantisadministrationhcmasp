# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time



class test_a8_commodity_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a8_commodity_manage(self):
        u"""新建赠送商品"""

        #新增班型名称
        commodity_name=product_manage['commodity_name']
        #商品最低价格
        commodity_minimum_price=product_manage['commodity_minimum_price']
        # 商品出售价格
        commodity_sell_price = product_manage['commodity_sell_price']

        #用于赠送商品班型
        with open('D:\\Mantisadministrationhcmasp\\configFile\\commodity_name2.txt', 'w', encoding='utf-8') as f:
            f.write(commodity_name)
            f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        driver = self.driver
    #产品管理
        driver.find_element_by_xpath("//span[contains(.,'产品管理')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('班型管理').click()
        time.sleep(2)

#查询
        driver.find_element_by_xpath('//*[@id="firstProductId"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[text()="' + name1 + '"]').click()
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)
        #上架
        driver.find_element_by_link_text('上架').click()
        time.sleep(2)
        #所属学院
        driver.find_element_by_xpath('//div[3]/div/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[4]/div/div/div/ul/li').click()
        #商品名称
        driver.find_element_by_xpath("(//input[@id='name'])[2]").send_keys(commodity_name)
        time.sleep(1)

        #服务商
        driver.find_element_by_xpath("//div[@id='serviceAgentId']/div/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[5]/div/div/div/ul/li').click()
        time.sleep(1)
        #最低价

        driver.find_element_by_id('minPrice').send_keys(commodity_minimum_price)
        time.sleep(1)
        #出售价格

        driver.find_element_by_id('price').send_keys(commodity_sell_price)
        time.sleep(1)
        #保存
        driver.find_element_by_xpath("//button[contains(.,'保 存')]").click()
        time.sleep(2)


    #商品管理

        driver.find_element_by_link_text('商品管理').click()
        #查询

        driver.find_element_by_id('name').send_keys(commodity_name)
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)
    #断言
        masg=driver.find_element_by_xpath('//div[2]/div[2]/div/div/table/tbody/tr/td[3]').text
        print(masg)
        self.assertEqual(masg,commodity_name)
        time.sleep(2)

    def tearDown(self):
       self.driver.quit()


if __name__ == "__main__":
    unittest.main()

