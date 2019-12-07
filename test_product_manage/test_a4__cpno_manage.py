# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time
from lib.randomphone import randomtime

class test_a4__cpno_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a4__cpno_manage(self):
        u"""教学运营-课号管理-新增-管理-删除"""
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'r', encoding='utf-8')
        name2 = f.read()
        f.close()


        f = open('D:\\Mantisadministrationhcmasp\\configFile\\kaoqi.txt', 'r', encoding='utf-8')
        kaoqi = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\mcurriculum_name.txt', 'r', encoding='utf-8')
        mcurriculum_name = f.read()
        f.close()

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
        driver.find_element_by_xpath('//div/div/section/header/form/div/div[2]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name1+"')]").click()
        #二级项目
        driver.find_element_by_xpath('//div/div/section/header/form/div/div[3]/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+name2+"')]").click()

        #课程
        driver.find_element_by_xpath('//div[2]/div/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+mcurriculum_name+"')]").click()
        time.sleep(3)

        #考期
        driver.find_element_by_xpath("(//div[@id='baseExamId']/div/div)[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+kaoqi+"')]").click()
        time.sleep(1)
        #开班点
        driver.find_element_by_xpath('//span/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(.,'今天')]").click()
        time.sleep(1)
        #班别
        driver.find_element_by_xpath('//div[3]/div[5]/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'周末班')]").click()
        time.sleep(1)
        #课次开始时间
        driver.find_element_by_id('startTime').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[1]/input').send_keys(randomtime())
        time.sleep(1)
        #选择周六
        driver.find_element_by_xpath('//label/span[2]').click()

        #招生上线
        driver.find_element_by_id('maxPerson').click()
        driver.find_element_by_id('maxPerson').send_keys(30)

        #授课教师
        driver.find_element_by_xpath('//div[5]/div/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul').click()
        time.sleep(1)

        #直播厂商
        driver.find_element_by_xpath('//div[6]/div/div/div[2]/div/span/div/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'欢拓')]").click()

        #预排课
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[7]/button').click()
        time.sleep(2)
        #保存确认
        driver.find_element_by_xpath("//button[contains(.,'保存并确认')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(.,'确 定')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(.,'知道了')]").click()
        time.sleep(3)
#查询
        #一级项目
        driver.find_element_by_xpath('//*[@id="firstProductId"]/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[contains(.,'"+name1+"')]").click()
        time.sleep(1)
        #二级项目
        driver.find_element_by_xpath('//*[@id="secondProductId"]/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[contains(.,'"+name2+"')]").click()
        time.sleep(1)

        #查询
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()
        time.sleep(2)


#断言
        cpno=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[5]').text
        print(cpno)
        self.assertIsNotNone(cpno,' ')
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

