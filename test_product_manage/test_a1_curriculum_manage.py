# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time

class test_a1_recorded_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a1_recorded_manage(self):
        u"""产品管理-—新增-修改-删除"""


        #新增课程名称
        curriculum_name=product_manage['curriculum_name']
        #修改课程名称
        mcurriculum_name=product_manage['mcurriculum_name']
        # 新增模块名称
        module_name=product_manage['module_name']
        #新增课次名称
        class_time=product_manage['class_time']
        driver = self.driver
    #产品管理
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[14]/div').click()
        time.sleep(1)
        driver.find_element_by_link_text('课程管理').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[1]/span/button[1]').click()
        time.sleep(2)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #课程名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(curriculum_name)
        #授课方式
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[4]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #课程分类
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #保存并配置
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[3]').click()
        time.sleep(2)
        #新增模块
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/h4/button').click()
        time.sleep(2)
        #模块名称
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h3/span/input').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h3/span/input').send_keys(module_name)
        #添加课次
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h4/a[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h4/a[2]').click()
        time.sleep(1)
        #课次名称
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[2]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[2]/div/input').send_keys(class_time)
        #课时
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/div/input').send_keys(2)
        #保存
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
        #保存并发布
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)




#查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(curriculum_name)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[2]/div[5]/button[1]').click()
        time.sleep(4)
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text
        print(masg)
        self.assertEqual(masg,curriculum_name)
        time.sleep(2)
#修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[12]/div/a[1]').click()
        time.sleep(2)
        # 课程名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(mcurriculum_name)
        time.sleep(1)
        # 保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
    # 查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[1]/div[3]/div/div[2]/div/span/input').clear()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(mcurriculum_name)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/header/form/div[2]/div[5]/button[1]').click()
        time.sleep(2)
        masg = driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text
        print(masg)
        self.assertEquals(masg, mcurriculum_name)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

