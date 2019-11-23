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


        #赠送商品名称
        present=teaching_operation['present']
        #操作人
        name=teaching_operation['name']
        driver = self.driver
    #教学运营
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[14]/div').click()
        time.sleep(1)
        driver.find_element_by_link_text('赠送服务').click()
        time.sleep(2)
        #新增赠送任务
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/div/button[1]').click()
        time.sleep(2)
    #选择赠送商品学员  购买商品  一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/dl/dd/div/div[1]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/dl/dd/div/div[2]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #选择商品
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/dl/dd/div/div[3]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(2)
    #选择赠送服务
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/button[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(present)
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


    #查询
        #时间
        driver.find_element_by_xpath('//*[@id="createTime"]/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div/div[1]').click()
        #操作人
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[1]/div[4]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[1]/div[4]/div/div[2]/div/span/input').send_keys(name)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div/button[1]').click()
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[8]').text
        print(masg)
        self.assertEquals(masg,name)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

