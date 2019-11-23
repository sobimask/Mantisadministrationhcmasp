# -*- coding: utf-8 -*-
from configFile.config_account_and_content import administration_url,name,password
import time
import unittest
def electronic_login(self): 
    u"""登录"""
    #管理员首次登陆
    driver = self.driver
    driver.get(administration_url + "/")
    try:
        driver.switch_to.alert().accept()
    except:
        try:
            driver.maximize_window()
        except:
            print('已经最大化 不用最大化了')
    finally:
        time.sleep(2)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(name)
        time.sleep(2)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/div[2]/div/div/div/div/form/div[3]/div/div/span/button').click()
        time.sleep(3)


