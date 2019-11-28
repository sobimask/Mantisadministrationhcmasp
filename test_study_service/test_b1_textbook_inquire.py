# -*- coding: utf-8 -*-
from lib.login import electronic_login
from lib.addpayment import addpayment
from configFile.config_account_and_content import study_service,student_centre
from selenium import webdriver
import unittest
import time


class test_b_textbook_inquire(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_b_textbook_inquire(self):
        u"""学服中心-补发教材-快递补发"""

#传入参数
        #新增学员电话号码
        student_phone=study_service['textbook']
        with open('D:\\Mantisadministrationhcmasp\\configFile\\student2.txt', 'w') as f:
            f.write(student_phone)
            f.close()
        #新增学员姓名
        student_name=student_centre['name']

        #应缴费用
        assessment=student_centre['assessment']
        #实缴费用
        paid=student_centre['paid']
        #快递补发地址
        site=student_centre['site']

        #d调取新增用户-报名
        addpayment(self, student_name, student_phone,  assessment, paid)
        time.sleep(5)
        driver = self.driver
        time.sleep(1)
#学服中心
        driver.find_element_by_xpath("//span[contains(.,'学服中心')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
        #查询
        driver.find_element_by_id('customerInfo').click()
        driver.find_element_by_id('customerInfo').send_keys(student_phone)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/form/div/div[21]/button[1]').click()
        time.sleep(2)
        #获取订单id
        id=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]/span').text
        time.sleep(1)
#教材补发
        driver.find_element_by_link_text('教材补发').click()
        time.sleep(2)
        #根据客户id进行查询'
        driver.find_element_by_id('mspCustomerId').click()
        driver.find_element_by_id('mspCustomerId').send_keys(id)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div[3]/button[2]').click()
        time.sleep(2)
    #快递补发
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[11]/span/a[1]').click()
        time.sleep(2)
        #获取补发教材名称
        book=driver.find_element_by_xpath('//*[@id="bookes"]/label[1]/span[2]').text
        #选择教材
        driver.find_element_by_xpath('//*[@id="bookes"]/label[1]/span[1]/input').click()
      #收件地址
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/button').click()
        time.sleep(2)

        #收货人
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').send_keys(student_name)
        #联系方式
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/input').send_keys(student_phone)
        #地址
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/span/textarea').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/span/textarea').send_keys(site)
        #确定
        driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
     #快递信息-邮寄日期
        driver.find_element_by_xpath('//*[@id="bizDate"]/div/input').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('今天').click()
        #快递公司
        driver.find_element_by_xpath('//*[@id="expressInfoId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[12]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        time.sleep(1)
        #快递单号
        driver.find_element_by_id('expressCode').click()
        driver.find_element_by_id('expressCode').send_keys(student_phone)
        time.sleep(1)
        #保存
        driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[9]').text
        print(masg)
        self.assertNotIn(masg,book)



    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

