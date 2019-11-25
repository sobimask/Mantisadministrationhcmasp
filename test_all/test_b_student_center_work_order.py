# -*- coding: utf-8 -*-
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time
from configFile.config_account_and_content import student_centre

class test_c_student_center_work_order(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_c_student_center_work_order(self):
        u"""学员中心-工单"""

        # 传入参数
        #联系人电话号码
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r')
        student_phone = f.read()
        f.close()

        driver = self.driver
        time.sleep(1)
        # 学员中心
        driver.find_element_by_link_text('学员中心').click()
        time.sleep(2)
        # 查询
        driver.find_element_by_id('searchMess').clear()
        driver.find_element_by_id('searchMess').send_keys(student_phone)
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/header/div/form/div/div[2]/div/div/div/span/button[1]').click()
        time.sleep(2)
        #点击用户名称
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/a/div').click()
        time.sleep(2)
# 工单
        driver.find_element_by_link_text('工单').click()
        time.sleep(2)
        #新增工单
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/section/main/section/div/div/header/div/div[2]/button').click()
        time.sleep(2)
        #操作类型   指定回访计划
        driver.find_element_by_xpath('//*[@id="operateType"]/label[1]').click()
        #工单类型
        driver.find_element_by_xpath('//*[@id="typeCode"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #工单时间
        driver.find_element_by_xpath('//*[@id="planTime"]/div/input').click()
        driver.find_element_by_link_text('此刻').click()
        time.sleep(1)
        #
        driver.find_element_by_xpath('//*[@id="ownerType"]/label[2]/span[1]/input')

        #负责机构
        driver.find_element_by_xpath('//*[@id="ownerOrgIdIsNextWork"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        # 负责人
        driver.find_element_by_xpath('//*[@id="ownerIdIsNextWork"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)

        #工单内容
        driver.find_element_by_id('content').click()
        driver.find_element_by_id('content').send_keys('客户维护')
        #保存
        driver.find_element_by_xpath('//*[@id="followUp"]/div[1]/div[2]/form/div[3]/div/div/span/button').click()
        time.sleep(15)
        #返回
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div[2]/div/section/header/div/div[2]/button').click()
        time.sleep(2)

        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div[1]/div/section/section/main/section/main/section/main/section/div/div/main/div/div/div/div/div/div/div[3]/div[2]/div/table/tbody/tr/td/span/span[1]/a').click()
        time.sleep(2)

        # 工单备注
        driver.find_element_by_id('dealRemark').click()
        driver.find_element_by_id('dealRemark').send_keys('没事常联系')
        time.sleep(1)
        # 类型  - 不设置
        driver.find_element_by_xpath('//*[@id="isNextWork"]/label[2]/span[1]/input').click()
        time.sleep(1)
        # 回访完成
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(15)
        # f返回
        driver.find_element_by_xpath(
            "//*[@id=\"hisroot\"]/div/div/section/div/div/div/section/main/div/div[2]/div/section/header/div/div[2]/button").click()
        time.sleep(2)
        masg = driver.find_element_by_xpath("//span[@style='color: green;']").text
        print(masg)
        self.assertEqual(masg, '已处理')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

