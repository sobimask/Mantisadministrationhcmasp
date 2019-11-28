# -*- coding: utf-8 -*-
from lib.login import electronic_login
from lib.addpayment import addpayment
from configFile.config_account_and_content import study_service,student_centre
from selenium import webdriver
import unittest
import time


class test_a_order_manage_transfer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a_order_manage_transfer(self):
        u"""学服中心-订单管理-转班"""

#传入参数
        #新增学员电话号码
        student_phone=study_service['transfer']
        #新增学员姓名
        student_name=student_centre['name']
        #报名应缴费用
        assessment=student_centre['assessment']
        #报名实缴费用
        paid=student_centre['paid']
        #原班型退费金额
        transfer_return=student_centre['transfer_return']
        # 转班应缴费用
        assessment2 = student_centre['assessment2']
        #转班 实缴费用
        paid2 = student_centre['paid2']
        #转班发票号
        fapiao = student_centre['fapiao']
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\commodity_name1.txt', 'r', encoding='utf-8')
        commodity_name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\kaoqi.txt', 'r', encoding='utf-8')
        kaoqi = f.read()
        f.close()

        #d调取新增用户-报名
        addpayment(self, student_name, student_phone, assessment, paid)
        time.sleep(5)
        driver = self.driver
        time.sleep(1)
# 学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
        # 查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[21]/button[1]').click()
        time.sleep(2)
    # 进入子订单
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span[2]').click()
        time.sleep(1)
        # 转班
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/table/tbody/tr[2]/td/span/span[2]/a').click()
        time.sleep(1)
    #原班型退费  -- 扣费金额
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div/div[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div/div[2]/input').send_keys(transfer_return)
        time.sleep(1)
        #下一步
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div/button').click()
        time.sleep(2)
    #转入新班
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[1]/div/div[2]/div/button').click()
        time.sleep(1)
        #班型
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/input').send_keys(commodity_name1)
        time.sleep(1)
        #
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[1]/span/label/span/input').click()
        time.sleep(1)
        #确定
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)

        #考期
        driver.find_element_by_xpath('//td[6]/div/div/div').click()
        driver.find_element_by_xpath("//li[contains(.,'"+kaoqi+"')]").click()
        time.sleep(2)
        #应缴费用
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[7]/div/div[2]/input').send_keys(assessment2)
        #选择补发形式
        driver.find_element_by_xpath('//span[4]/div/div/div').click()

        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'现场发放')]").click()
        time.sleep(1)
        #下一步
        driver.find_element_by_xpath("//button[contains(.,'下一步')]").click()
        time.sleep(2)
        #支付信息
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #支付方式
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #小票号
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div/div[2]/div/span/input').send_keys(fapiao)
        #支付金额
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[5]/div/div[2]/div/span/div/div[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[5]/div/div[2]/div/span/div/div[2]/input').send_keys(paid2)
        time.sleep(1)
        #提交
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div/button[2]').click()
        time.sleep(2)
        #断言
        #进入子订单
        driver.find_element_by_xpath(
            '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span[2]').click()
        time.sleep(1)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[2]/td').text
        print(masg)
        self.assertIn(masg,'已转')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

