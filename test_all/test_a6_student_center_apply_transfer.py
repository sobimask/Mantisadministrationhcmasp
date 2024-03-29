# -*- coding: utf-8 -*-
from configFile.config_account_and_content import student_centre
from lib.login import electronic_login
from selenium import webdriver
import unittest
import time
from lib.addpayment import addpayment

class test_a_student_center_apply_transfer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a_student_center_apply_transfer(self):
        u"""学员中心-报名-转班"""

#传入参数
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\commodity_name1.txt', 'r', encoding='utf-8')
        commodity_name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\payment_way.txt', 'r', encoding='utf-8')
        payment_way = f.read()
        f.close()

        #新增学员电话号码
        student_phone=student_centre['transfer']
        #新增学员姓名
        student_name=student_centre['name']
        #报名应缴费用
        assessment=student_centre['assessment']
        #报名实缴费用
        paid=student_centre['paid']
        #原班型退费金额
        transfer_return=student_centre['transfer_return']
        #转班班型
        # 转班应缴费用
        assessment2 = student_centre['assessment2']
        #转班 实缴费用
        paid2 = student_centre['paid2']

        #d调取新增用户-报名
        addpayment(self, student_name, student_phone, assessment, paid)

        driver = self.driver
        time.sleep(1)
    #点击报名
        driver.find_element_by_xpath('//*[@id="student-detail-menu"]/ul/li[10]/a').click()
        time.sleep(1)
        # 点击操作
        driver.find_element_by_xpath(
            '//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(1)
        # 转班
        driver.find_element_by_xpath('/html/body/div[9]/div/div/ul/li[1]').click()
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
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[6]/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name(
            'ant-select-dropdown-menu-item').click()
        time.sleep(3)
        #应缴费用
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[7]/div/div[2]/input').send_keys(assessment2)
        #选择补发形式
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[2]/span[4]/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[12]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #下一步
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
    #支付信息
        # 费用类型   16号修改支付信息页面新UI
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[1]/div[1]/div/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[contains(.,'定金费')]").click()
        time.sleep(3)
        # 支付方式
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[contains(.,'" + payment_way + "')]").click()
        time.sleep(1)
        # 小票号
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div[3]/div/div[2]/div/span/input').send_keys(
            student_phone)
        time.sleep(1)
        # 支付金额
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div[2]/div/div[2]/div/span/div/div[2]/input').send_keys(
            paid2)


        try:
            #分期数
            driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[4]/div/div[2]/div/span/div/div/div').click()
            driver.find_element_by_xpath('/html/body/div[12]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        except:
            pass
        finally:
            #提交
            driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div/button[2]').click()
            time.sleep(2)
    #断言
            masg=driver.find_element_by_xpath('//*[@id="reservation"]/div/div/ul/li/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/span/span').text
            print(masg)
            self.assertIn(masg,'已转')



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

