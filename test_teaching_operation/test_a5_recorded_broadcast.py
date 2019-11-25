# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time


class test_a5_recorded_broadcast(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a5_recorded_broadcast(self):
        u"""教学运营-录播课号-修改课次"""


        #修改课次

        recorded_broadcast=teaching_operation['recorded_broadcast']
        driver = self.driver
    #教学运营
        driver.find_element_by_xpath("//span[contains(.,'教学运营')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('录播课号').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/button[1]').click()
        time.sleep(2)
        # 一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[1]/div[3]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #录播课程
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[2]/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #考期
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[3]/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #开班点
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[3]/div[2]/div/div[2]/div/span/span/div/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[6]').click()
        #班别
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[3]/div[4]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #招生上线
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[3]/div[5]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[3]/div[5]/div/div[2]/div/span/input').send_keys(30)
        #排课
        driver.find_element_by_xpath('//*[@id="scheduleDays"]/span/label[1]/span[1]/input').click()
        time.sleep(1)
        #预排课
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/header/form/div[5]/button').click()
        time.sleep(2)
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div[2]/button[2]').click()
        time.sleep(2)
#查询
        #一级项目
        driver.find_element_by_xpath('//*[@id="firstProductId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #二级项目
        driver.find_element_by_xpath('//*[@id="secondProductId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #录播课程
        driver.find_element_by_xpath('//*[@id="courseRecordId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div/button[1]').click()
        time.sleep(2)
#断言
        cpno=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[4]').text
        print(cpno)
        self.assertIsNotNone(cpno,' ')
        time.sleep(1)
#管理
        driver.find_element_by_link_text('管理').click()
        time.sleep(2)
        #修改
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/main/div/section/div/div/main/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[9]/div/a[1]').click()
        time.sleep(2)
        #课次
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/main/div/section/div/div/main/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/input').clear()
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/main/div/section/div/div/main/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/input').send_keys(recorded_broadcast)
        #完成
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/main/div/section/div/div/main/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[9]/div/a[1]').click()
        time.sleep(2)
        #返回
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/button').click()
        time.sleep(2)
        #删除
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[9]/div/span/span/a').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(2)
#查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div/button[1]').click()
        time.sleep(2)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div[2]/div/p').text
        print(masg)
        self.assertEquals(masg,'暂无数据')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

