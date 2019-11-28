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


        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'r', encoding='utf-8')
        name2 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\kaoqi.txt', 'r', encoding='utf-8')
        kaoqi = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\recorded_name.txt', 'r', encoding='utf-8')
        recorded_name = f.read()
        f.close()
        #修改课次

        recorded_broadcast=teaching_operation['recorded_broadcast']
        driver = self.driver
    #教学运营
        driver.find_element_by_xpath("//span[contains(.,'教学运营')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('录播课号').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath("//button[contains(.,'新 增')]").click()
        time.sleep(2)
        # 一级项目
        driver.find_element_by_xpath("(//div[@id='firstProductId']/div/div/div)[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name1+"')]").click()
        time.sleep(1)
        #二级项目
        driver.find_element_by_xpath("(//div[@id='secondProductId']/div/div)[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name2+"')]").click()
        time.sleep(1)
        #录播课程
        driver.find_element_by_xpath("(//div[@id='courseRecordId']/div/div/div)[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+recorded_name+"')]").click()
        time.sleep(1)
        #考期
        driver.find_element_by_xpath("(//div[@id='baseExamId']/div/div)[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[text()="' + kaoqi + '"]').click()
        time.sleep(1)
        #开班点
        driver.find_element_by_xpath("//span[@id='startDay']/div/input").click()
        time.sleep(1)
        driver.find_element_by_link_text('今天').click()
        time.sleep(3)
        #班别
        driver.find_element_by_xpath("(//div[@id='scheduleTypeCode']/div/div/div)[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'周末班')]").click()
        time.sleep(1)
        #招生上线

        driver.find_element_by_id('maxPerson').send_keys(30)
        time.sleep(1)
        #排课
        driver.find_element_by_xpath('//*[@id="scheduleDays"]/span/label[1]/span[1]/input').click()
        time.sleep(2)

        #预排课
        driver.find_element_by_xpath("//button[contains(.,'预排课')]").click()
        time.sleep(2)
        #保存
        driver.find_element_by_xpath("//button[contains(.,'保 存')]").click()
        time.sleep(2)
#查询

        #一级项目
        driver.find_element_by_xpath("//div[@id='firstProductId']/div/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'" + name1 + "')]").click()
        time.sleep(1)

        #查询
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)
#断言
        cpno=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[4]').text
        print(cpno)
        self.assertIsNotNone(cpno,' ')
        time.sleep(1)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

