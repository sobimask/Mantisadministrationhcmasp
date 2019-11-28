# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time


class test_a_student_center_allpy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_student_center_allpy(self):
        u"""学员中心-报名"""

#传入参数
        #新增学员电话号码
        f=open('D:\\Mantisadministrationhcmasp\\configFile\\student.txt', 'r',encoding='utf-8')
        student_phone = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\commodity_name.txt', 'r',encoding='utf-8')
        class_type = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\kaoqi.txt', 'r', encoding='utf-8')
        kaoqi = f.read()
        f.close()

        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']
        #报名班型


        # time.sleep(2)
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
        # 点击用户名称

        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/a/div').click()
        time.sleep(2)
        # 报名
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/header/div/div[2]/button[2]').click()
        time.sleep(2)
        # 性别
        driver.find_element_by_xpath(
            '//*[@id="sex"]/label[1]').click()
        time.sleep(1)
        # 电话
        driver.find_element_by_id('phone1').clear()
        driver.find_element_by_id('phone1').send_keys(student_phone)
        time.sleep(1)
        # 年龄
        driver.find_element_by_id('age').clear()
        driver.find_element_by_id('age').send_keys(18)
        # 证件类型
        driver.find_element_by_xpath('//*[@id="documentTypeCode"]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[text()="身份证"]').click()
        time.sleep(1)
        # 证件号码
        driver.find_element_by_id('documentNumber').click()
        driver.find_element_by_id('documentNumber').send_keys(410882199808096789)
        time.sleep(2)
        # 下一步
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div/button').click()
        time.sleep(2)
        # 报名信息#
        # 校区
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name(
            'ant-select-dropdown-menu-item').click()
        # 增加班型
        driver.find_element_by_xpath("//button[contains(.,'增加班型')]").click()
        time.sleep(3)
        driver.find_element_by_xpath('//div/span/input').send_keys(class_type)
        time.sleep(1)
        driver.find_element_by_xpath('//span/label/span/input').click()
        time.sleep(1)
        # 确定
        driver.find_element_by_xpath("//button[contains(.,'确 定')]").click()
        time.sleep(3)
        # 考期正确操作
        driver.find_element_by_xpath('//td[6]/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+kaoqi+"')]").click()
        time.sleep(1)
        # 金额
        driver.find_element_by_xpath('//div[2]/input').send_keys(assessment)
        time.sleep(1)
        # 补发形式
        driver.find_element_by_xpath('//span[4]/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'现场发放')]").click()
        # 下一步
        driver.find_element_by_xpath("//button[contains(.,'下一步')]").click()
        time.sleep(3)
        # 支付信息
        # 费用类型
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name(
            'ant-select-dropdown-menu-item').click()
        time.sleep(1)
        # 支付方式
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name(
            'ant-select-dropdown-menu-item').click()
        time.sleep(1)
        # 小票号
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div/div[2]/div/span/input').send_keys(
            student_phone)
        time.sleep(1)

        # 支付金额
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[5]/div/div[2]/div/span/div/div[2]/input').click()
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[5]/div/div[2]/div/span/div/div[2]/input').send_keys(
            paid)
        # 提交
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div/button[2]').click()
        time.sleep(8)
        # 断言
        # xx学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(1)
        # 查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        time.sleep(1)

        #23早更改查询元素定位
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[21]/button[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span[2]').click()
        masg = driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]/span').text
        print(masg)
        self.assertIsNotNone(masg)




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

