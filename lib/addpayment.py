# -*- coding: utf-8 -*-
import unittest
from configFile.config_account_and_content import tomorrowr
import time

def addpayment(self,student_name,student_phone,student_class,assessment,paid):
    u"""增加支付单-报名"""

    # 用户登录
    # electronic_login(self)
    time.sleep(2)
    driver = self.driver
    # 新增学员
    driver.find_element_by_xpath(
        '//*[@id="hisroot"]/div/div/section/div/div/div/section/header/div[2]/div/ul/li[1]/button').click()
    time.sleep(1)
    # 姓名
    driver.find_element_by_id('name').click()
    driver.find_element_by_id('name').send_keys(student_name)
    # 上课手机号
    driver.find_element_by_id('account').click()
    driver.find_element_by_id('account').send_keys(student_phone)
    time.sleep(1)
    # 地域
    driver.find_element_by_xpath('//*[@id="area"]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name(
        'ant-select-dropdown-menu-item').click()
    time.sleep(1)
    # 学院
    driver.find_element_by_xpath('//*[@id="collegeId"]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name(
        'ant-select-dropdown-menu-item').click()
    time.sleep(1)
    # 来源
    driver.find_element_by_xpath('//*[@id="mscCode"]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name(
        'ant-select-dropdown-menu-item').click()
    # 咨询项目
    driver.find_element_by_xpath('//*[@id="consultId"]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name(
        'ant-select-dropdown-menu-item').click()
    time.sleep(1)
    # 校区
    driver.find_element_by_xpath('//*[@id="campusId"]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul').find_element_by_class_name(
        'ant-select-dropdown-menu-item').click()
    # 确定
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(9)

#学员中心
    driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[15]/a').click()
    time.sleep(4)
    #查询
    driver.find_element_by_id('searchMess').clear()
    driver.find_element_by_id('searchMess').send_keys(student_phone)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/header/div/form/div/div[2]/div/div/div/span/button[1]').click()
    #点击用户名称
    driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/main/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/a/div').click()
    time.sleep(2)
    #报名
    driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/div/section/section/main/section/header/div/div[2]/button[2]').click()
    time.sleep(2)
    #性别
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[1]/div[2]/div/div[2]/div/span/div/label[1]').click()
    time.sleep(1)
    #电话
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div[1]/div/div[2]/div/span/input').clear()
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div[1]/div/div[2]/div/span/input').send_keys(student_phone)
    time.sleep(1)
    #年龄
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[7]/div[1]/div/div[2]/div/span/div/div[2]/input').clear()
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[7]/div[1]/div/div[2]/div/span/div/div[2]/input').send_keys(18)
    #证件类型
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[8]/div[1]/div/div[2]/div/span/div/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//li[text()="身份证"]').click()
    time.sleep(1)
    #证件号码
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[8]/div[2]/div/div[2]/div/span/input').click()
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[8]/div[2]/div/div[2]/div/span/input').send_keys(410882199808096789)
    time.sleep(1)
    #下一步
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div/button').click()
    time.sleep(2)
 #报名信息#
    #校区
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
    #增加班型
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[1]/div/div[2]/div/button').click()
    time.sleep(3)
    #班型
    driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/input').click()
    driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[1]/span/label/span/input').click()
    time.sleep(1)
    #确定
    driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(3)
    #考期正确操作
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[6]/div/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[12]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
    time.sleep(1)
    #金额
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[8]/div/div[2]/input').send_keys(assessment)
    time.sleep(1)
    #补发形式
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[2]/span[4]/div/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[13]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
    #下一步
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div[3]/button[2]').click()
    time.sleep(3)
 #支付信息
    #费用类型
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[1]/div/div[2]/div/span/div/div/div').click()
    driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
    time.sleep(1)
    #支付方式
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[2]/div/div[2]/div/span/div/div/div').click()
    driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
    time.sleep(1)
    #小票号
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div/div[2]/div/span/input').click()
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[3]/div/div[2]/div/span/input').send_keys(student_phone)
    time.sleep(1)
    #支付金额
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[5]/div/div[2]/div/span/div/div[2]/input').click()
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/form/div[3]/div/div[5]/div/div[2]/div/span/div/div[2]/input').send_keys(paid)
    #预补缴日期
    try:
        driver.find_element_by_xpath("//input[@placeholder='请选择补缴日期']").click()
        time.sleep(2)
        driver.find_element_by_xpath('//div/div/div/div/div/div/input').send_keys(tomorrowr)
        time.sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/section/main/div/div/div/div/button[2]').click()
        time.sleep(2)
    except:
        pass


    #提交



if __name__ == "__main__":
    unittest.main()

