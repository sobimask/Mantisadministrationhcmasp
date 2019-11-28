# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import teaching_operation
from selenium import webdriver
import unittest
import time

class test_a_workorder_masnage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_workorder_masnage(self):
        u"""教学运营-工单管理"""
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\commodity_name.txt', 'r', encoding='utf-8')
        class_type = f.read()
        f.close()

        driver = self.driver
    #教学运营
        driver.find_element_by_xpath("//span[contains(.,'教学运营')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('工单管理').click()
        time.sleep(2)
        #批量新增工单
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/div/button[1]').click()
        time.sleep(2)
        #报名时间
        driver.find_element_by_xpath('//*[@id="orderBizTime"]/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[5]').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[3]').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/a[2]').click()

        #发送范围  指定范围
        driver.find_element_by_xpath('//*[@id="sendScope"]/label[2]/span[1]/input').click()
        time.sleep(1)
        #商品维度
        driver.find_element_by_xpath('//*[@id="workTaskScopeType"]/label[1]/span[1]/input').click()
        #选择商品
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/button').click()
        time.sleep(2)
        #班型
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/input').send_keys(class_type)
        #
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[1]/span/label/span/input').click()
        #确定
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)

        #工单类型
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #计划时间
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[6]/div[2]/div/span/span/div/input').click()
        driver.find_element_by_link_text('此刻').click()
        time.sleep(1)
        #工单内容
        driver.find_element_by_id('content').click()
        driver.find_element_by_id('content').send_keys('工单内容')
        #确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        #确认
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(2)
#   #根据登陆用户name查询创建工单
        name = driver.find_element_by_xpath('//span[3]').text
        print(name)
        driver.find_element_by_id('createrName').click()
        driver.find_element_by_id('createrName').send_keys(name)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/div/form/div[2]/div/button[1]').click()
        time.sleep(1)

#处理
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/table/tbody/tr[2]/td/span/span/a').click()
        time.sleep(1)
        #工单备注
        driver.find_element_by_id('dealRemark').click()
        driver.find_element_by_id('dealRemark').send_keys('工单备注')
        time.sleep(1)
        #工单类型
        driver.find_element_by_xpath('//*[@id="typeCode"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #下次计划时间
        driver.find_element_by_xpath('//*[@id="planTime"]/div/input').click()
        time.sleep(1)
        driver.find_element_by_link_text('此刻').click()
        time.sleep(1)
        #负责人
        driver.find_element_by_xpath('//*[@id="ownerType"]/label[1]/span[1]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="followUpEdit"]/div[1]/div[2]/form/div[5]/div[4]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[1]/span/label/span/input').click()
        #工单内容
        time.sleep(1)
        driver.find_element_by_id('content').click()
        driver.find_element_by_id('content').send_keys('工单内容')
        time.sleep(1)
        #工单完成
        driver.find_element_by_xpath("//button[contains(.,'工单完成')]").click()
        time.sleep(15)
    #返回
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div[2]/div/section/header/div/div[2]/button').click()
        time.sleep(1)
#d断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[5]/span').text
        print(masg)
        self.assertEqual(masg,'已处理')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

