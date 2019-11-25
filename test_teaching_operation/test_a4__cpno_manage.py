# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time


class test_a4__cpno_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a4__cpno_manage(self):
        u"""教学运营-课号管理-新增-管理-删除"""

        # 修改课次
        cpno_manage = teaching_operation['cpno_manage']

        driver = self.driver
    #教学运营
        driver.find_element_by_xpath("//span[contains(.,'教学运营')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('课号管理').click()
        time.sleep(2)
    #新增普通课号
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/button[1]').click()
        time.sleep(2)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[1]/div[3]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #课程
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[2]/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #考期
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[3]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #开班点
        driver.find_element_by_xpath('//*[@id="startDay"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[3]').click()
        #班别
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[3]/div[5]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #课次开始时间
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[3]/div[6]/div/div[2]/div/span/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[17]').click()
        #排课
        driver.find_element_by_xpath('//*[@id="scheduleDays"]/span/label[1]/span[1]/input').click()
        #driver.find_element_by_xpath('//*[@id="intervalNum"]/div/div[2]/input').send_keys(1)

        #招生上线
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[4]/div[2]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[4]/div[2]/div/div[2]/div/span/input').send_keys(30)

        #授课教师
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[5]/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #直播厂商
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[6]/div/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()

        #预排课
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[7]/button').click()
        time.sleep(2)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/main/div[2]/button[2]').click()
        time.sleep(2)
#查询
        #一级项目
        driver.find_element_by_xpath('//*[@id="firstProductId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #二级项目
        driver.find_element_by_xpath('//*[@id="secondProductId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #课程
        driver.find_element_by_xpath('//*[@id="courseModuleId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #考期
        driver.find_element_by_xpath('//*[@id="baseExamId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div/button[1]').click()
        time.sleep(2)
#断言
        cpno=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[5]').text
        print(cpno)
        self.assertIsNotNone(cpno,' ')
        time.sleep(2)
#管理
        driver.find_element_by_link_text('管理').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[9]/div/a').click()
        time.sleep(2)
        #课次
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]/div/input').clear()
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]/div/input').send_keys(cpno_manage)
        #完成
        driver.find_element_by_link_text('完成').click()
        time.sleep(2)
        #返回
        driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/button').click()
        time.sleep(1)
#删除
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[12]/div/span/span/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(1)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

