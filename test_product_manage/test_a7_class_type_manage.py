# -*- coding: utf-8 -*-
from lib.login import electronic_login
from configFile.config_account_and_content import product_manage
from selenium import webdriver
import unittest
import time



class test_a7_class_type_manage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        electronic_login(self)

    def test_a7_class_type_manage(self):
        u"""产品管理-班型管理—新增-修改"""
        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name1.txt', 'r', encoding='utf-8')
        name1 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\name2.txt', 'r', encoding='utf-8')
        name2 = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\recorded_name.txt', 'r', encoding='utf-8')
        recorded_name = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\lubomokuai_name.txt', 'r', encoding='utf-8')
        lubomokuai_name = f.read()
        f.close()

        f = open('D:\\Mantisadministrationhcmasp\\configFile\\mcurriculum_name.txt', 'r', encoding='utf-8')
        mcurriculum_name = f.read()
        f.close()
        #新增班型名称
        class_type=product_manage['class_type']
        #修改科目
        mclass_type=product_manage['mclass_type']

        driver = self.driver
    #产品管理
        driver.find_element_by_xpath("//span[contains(.,'产品管理')]").click()
        time.sleep(1)
        driver.find_element_by_link_text('班型管理').click()
        time.sleep(2)
        #新增
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/span/button[1]').click()
        time.sleep(2)
        #班型名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').send_keys(class_type)
        #一级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//li[text()="' + name1 + '"]').click()
        time.sleep(1)
        #二级项目
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[4]/div/div[2]/div/span/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//li[text()="' + name2 + '"]').click()
        #班型类型
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div/span/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(.,'普通班型')]").click()
        #结算方式
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        #结算值
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div/div[2]/div/span/input').send_keys(99)
        #成本价
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div[2]/div/span/input').send_keys(88)
        #服务期
        driver.find_element_by_id('servicePeriod').click()
        time.sleep(1)
        driver.find_element_by_id('servicePeriod').send_keys(180)
        #课号
        driver.find_element_by_xpath("//button[contains(.,'选 择')]").click()
        time.sleep(2)
        #选择一级项目下的课号
        driver.find_element_by_id('courseModuleName').send_keys(mcurriculum_name)
        time.sleep(2)
        #选择课号
        driver.find_element_by_xpath('//div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td/span/label/span/input').click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'下一步')]").click()
        time.sleep(2)
        #选择模块名
        driver.find_element_by_xpath('//div[2]/div[2]/div/ul/li').click()
        time.sleep(1)
        #点击完成
        driver.find_element_by_xpath("//button[contains(.,'完 成')]").click()
        time.sleep(2)




        #选择录播
        driver.find_element_by_xpath("(//button[@type='button'])[8]").click()
        time.sleep(2)
        #输入录播课名称
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(recorded_name)
        time.sleep(2)
        #选择录播
        driver.find_element_by_xpath('//div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td/span/label/span/input').click()
        #点击下一步
        driver.find_element_by_xpath("//button[contains(.,'下一步')]").click()
        time.sleep(3)
        #选择模块
        driver.find_element_by_xpath("//li[contains(.,'"+ lubomokuai_name+"')]").click()
        time.sleep(1)
        #点击完成
        try:
            driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div[3]/div/button[3]').click()
        except:
            driver.find_element_by_xpath("//button[contains(.,'完 成')]").click()
        time.sleep(2)  #选择录播完成


        #选择教材
        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
        time.sleep(2)
        # #选择一级项目
        # driver.find_element_by_xpath("(//div[@id='firstProductId']/div/div/div)[6]").click()
        # time.sleep(2)
        # ul = driver.find_element_by_xpath("//div[10]/div/div/div/ul")     #定位ul位置
        # lis = ul.find_elements_by_xpath('li')                             #获取lu下所有li，返回lis为列表格式
        # lis[-1].click()                                                   #选择列表最后一个值点击

        #选择一级项目 第二种
        driver.find_element_by_xpath("(//div[@id='firstProductId']/div/div/div)[6]").click()
        time.sleep(2)
        li = driver.find_elements_by_xpath('/html/body/div[9]/div/div/div/ul/li')  # 获取所有li

        for i in li:
            if i.text == name1:    #判断li值和一级项目名
                i.click()
            else:
                print(i.text + "不是" +name1)

        time.sleep(2)

        #全选教材
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/table/thead/tr/th[1]/span/div/span[1]/div/label/span/input').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)   #选择教材完成




        #保存并发布班型
        #driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[3]').click()
        driver.find_element_by_xpath("//button[contains(.,'保存并发布')]").click()
        time.sleep(2)
#查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[3]/div/div[2]/div/span/input').click()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[3]/div/div[2]/div/span/input').send_keys(class_type)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[7]/button[1]').click()
        time.sleep(2)
    #断言
        masg=driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text
        print(masg)
        self.assertEqual(masg,class_type)
        time.sleep(2)
#修改
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[12]/span/a[2]').click()
        time.sleep(2)
        # 班型名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/input').send_keys(mclass_type)
        # 保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        time.sleep(2)
        # 查询
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[3]/div/div[2]/div/span/input').clear()
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[3]/div/div[2]/div/span/input').send_keys(mclass_type)
        driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[7]/button[1]').click()
        time.sleep(2)
        # 断言
        masg = driver.find_element_by_xpath( '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text
        print(masg)
        self.assertEqual(masg, mclass_type)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

