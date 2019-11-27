# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time



class test_a2_recorded_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a2_recorded_manage(self):
        u"""产品管理-录播管理—新增-修改-删除"""
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'r', encoding='utf-8')
        name2 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\luboshipin.txt', 'r', encoding='utf-8')
        data_name = f.read()
        f.close()


        #新增名称
        keci_name  = product_manage['keci_name']
        lubomokuai_name = product_manage['lubomokuai_name']
        recorded_name=product_manage['recorded_name']
        with open('D:\\Mantisadministrationhcmasp\\configFile\\lubomokuai_name.txt', 'w', encoding='utf-8') as f:
            f.write(lubomokuai_name)
            f.close()

        with open('D:\\Mantisadministrationhcmasp\\configFile\\recorded_name.txt', 'w', encoding='utf-8') as f:
            f.write(recorded_name)
            f.close()
        driver = self.driver
    #产品管理
        driver.find_element_by_xpath("//span[contains(.,'产品管理')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('录播管理').click()
        time.sleep(2)
        #录播配置-新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[1]/span/button[1]').click()
        time.sleep(2)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//li[text()="' + name1 + '"]').click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//li[text()="' + name2 + '"]').click()
        #录播课名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(recorded_name)
        #录播分类
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #保存并配置
        driver.find_element_by_xpath("//button[contains(.,'保存并配置')]").click()
        time.sleep(2)

        #新增模块
        driver.find_element_by_xpath("//button[contains(.,'新增模块')]").click()
        time.sleep(2)
        driver.find_element_by_xpath('//h3/span/input').send_keys(lubomokuai_name)
        time.sleep(1)
        #添加课次
        driver.find_element_by_link_text('添加课次').click()
        time.sleep(1)
        driver.find_element_by_link_text('添加课次').click()
        time.sleep(1)
        driver.find_element_by_xpath('//td[2]/div/input').send_keys(keci_name)
        time.sleep(1)
        #选择视频
        driver.find_element_by_xpath('//td[3]/div/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'"+data_name+"')]").click()
        time.sleep(1)
        #输入学习人数
        driver.find_element_by_xpath('//td[4]/div/input').send_keys(10)
        time.sleep(1)
        #保存
        driver.find_element_by_xpath("(//button[@type='button'])[15]").click()
        time.sleep(3)

        #保存并发布
        driver.find_element_by_xpath("//button[contains(.,'保存并发布')]").click()
        time.sleep(3)


#根据录播课名称查询
        driver.find_element_by_id('name').click()
        driver.find_element_by_id('name').send_keys(recorded_name)
        driver.find_element_by_xpath("//button[contains(.,'查 询')]").click()

        time.sleep(3)
        #修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[10]/span/a[1]').click()
        time.sleep(2)
        #b修改备注
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/span/textarea').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/span/textarea').send_keys('修改备注')
        #保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]').click()
        time.sleep(2)

    #断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[9]').text
        print(masg)
        self.assertEqual(masg,'修改备注')

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

