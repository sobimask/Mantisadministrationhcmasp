# coding:utf-8
from selenium import webdriver
driver = webdriver
def get_screen():
    '''截图'''
    import time
    nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
    fllename =  "ErrorScreen/" + nowTime+ '.png'
    driver.get_screenshot_as_file(fllename)
# 自动截图装饰器
def screen(func):
    '''截图装饰器'''
    def inner(*args, **kwargs):
        try:
            f = func(*args, **kwargs)
            return f
        except:
            get_screen()  # 失败后截图
    return inner
