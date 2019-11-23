# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time
import win32gui
import win32con


class test_a3_data_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)


    def test_a3_data_manage(self):
        u"""产品管理-资料管理—新增-修改"""


        #计划名称
        data_name=product_manage['data_name']

        driver = self.driver
    #产品管理
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[14]/div').click()
        time.sleep(1)
        driver.find_element_by_link_text('资料管理').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/div/button[1]').click()
        time.sleep(2)
        #名称
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').send_keys(data_name)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #类型
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/div/div/label[2]').click()
        time.sleep(1)
        #上传资料
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[1]/div/div[2]/div/span/a').click()
        time.sleep(2)
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\Users\\SobiM\\Desktop\\shipin.mp4')
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        time.sleep(5)
        # 关闭上传弹窗
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        time.sleep(5)
        #查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[1]/div[1]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[1]/div[1]/div/div[2]/div/span/input').send_keys(data_name)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div[2]/div[3]/button[1]').click()
        time.sleep(1)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]').text
        print(masg)
        self.assertEqual(masg,data_name)
        time.sleep(2)
#修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[10]/span/span[1]/a').click()
        time.sleep(2)
        #修改备注
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/div[2]/div/span/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/div[2]/div/span/textarea').send_keys('修改备注')
        #确定
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(4)
#断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[9]').text
        print(masg)
        self.assertEquals(masg,'修改备注')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

