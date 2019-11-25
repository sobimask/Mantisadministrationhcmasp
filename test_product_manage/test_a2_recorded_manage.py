# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time



class test_a2_recorded_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a2_recorded_manage(self):
        u"""产品管理-录播管理—新增-修改-删除"""


        #新增名称
        recorded_name=product_manage['recorded_name']
        driver = self.driver
    #产品管理
        driver.find_element_by_xpath("//span[contains(.,'产品管理')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('录播管理').click()
        time.sleep(2)
        #录播配置-新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[1]/span/button[1]').click()
        time.sleep(2)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #录播课名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(recorded_name)
        #录播分类
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]').click()
        time.sleep(2)
#根据录播课名称查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(recorded_name)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[3]/div[2]/button[1]').click()
        time.sleep(3)
        #修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[10]/span/a[1]').click()
        time.sleep(2)
        #b修改备注
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/span/textarea').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/span/textarea').send_keys('修改备注')
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]').click()
        time.sleep(2)
    #断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[9]').text
        print(masg)
        self.assertEqual(masg,'修改备注')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

