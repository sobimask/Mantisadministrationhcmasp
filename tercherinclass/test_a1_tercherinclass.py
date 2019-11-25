from lib.login import electronic_login,electronic_login1
import datetime
import time
import unittest
from selenium import webdriver
from configFile.config_account_and_content import product_manage
from selenium.webdriver.common.action_chains import ActionChains

startday = (datetime.datetime.now()).strftime("%Y-%m-%d")
starthour = (datetime.datetime.now() + datetime.timedelta(hours=0.5)).strftime("%H:%M")
endhour = (datetime.datetime.now() + datetime.timedelta(hours=2.5)).strftime("%H:%M")


class test_a1_tercherinclass(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 用户登录
        #electronic_login(self)

    def test_a1_tercherinclass(self):
        # # 新增课程名称
        # curriculum_name = product_manage['curriculum_name']
        # # 新增模块名称
        # module_name = product_manage['module_name']
        # # 新增课次名称
        #class_time = product_manage['class_time']
        class_time = '课次名称1932'
        driver = self.driver
        # #产品管理
        # driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[13]/div').click()
        # time.sleep(1)
        # driver.find_element_by_link_text('课程管理').click()
        # time.sleep(2)
        # # 新增
        # driver.find_element_by_xpath(
        #     '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/div/main/section/main/div/div/div/div/div/div/div/div[1]/span/button[1]').click()
        # time.sleep(2)
        # # 一级项目
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/span/div/div/div').click()
        # driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # # 二级项目
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # # 课程名称
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').click()
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div/span/input').send_keys(
        #     curriculum_name)
        # # 授课方式
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[4]/div/div[2]/div/span/div/div/div').click()
        # driver.find_element_by_xpath('//li[text()="直播"]').click()
        # # driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name(
        # #     'ant-select-dropdown-menu-item').click()
        # # 课程分类
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div[2]/div/span/div/div/div').click()
        #
        # driver.find_element_by_xpath('//li[text()="普通课程"]').click()
        #
        # # 保存并配置
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[3]').click()
        # time.sleep(2)
        # # 新增模块
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/h4/button').click()
        # time.sleep(2)
        # # 模块名称
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h3/span/input').click()
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h3/span/input').send_keys(
        #     module_name)
        # # 添加课次
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h4/a[2]').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/h4/a[2]').click()
        # time.sleep(1)
        # # 课次名称
        # driver.find_element_by_xpath(
        #     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[2]/div/input').click()
        # driver.find_element_by_xpath(
        #     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[2]/div/input').send_keys(
        #     class_time)
        # time.sleep(1)
        # # 课时
        # driver.find_element_by_xpath(
        #     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/div/input').click()
        # driver.find_element_by_xpath(
        #     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/div/input').send_keys(
        #     2)
        # time.sleep(1)
        # # 保存
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        # time.sleep(2)
        # # 保存并发布
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        # time.sleep(2)
        # # 教学运营
        # driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[14]/div').click()
        # time.sleep(1)
        # driver.find_element_by_link_text('课号管理').click()
        # time.sleep(2)
        # # 新增普通课号
        # driver.find_element_by_xpath(
        #     '//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/main/div/div/div/div/div/div/div/div[1]/div/button[1]').click()
        # time.sleep(2)
        # # 一级项目
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[1]/div[2]/div/div[2]/div/span/div/div/div').click()
        # driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # time.sleep(1)
        # # 二级项目
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[1]/div[3]/div/div[2]/div/span/div/div/div').click()
        # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # time.sleep(1)
        # # 课程
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[2]/div[1]/div/div[2]/div/span//*[@id="courseModuleId"]/div/div').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul').find_element_by_class_name('ant-select-dropdown-menu-item').click()
        # time.sleep(1)
        # # 考期
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[3]/div[2]/div/div[2]/div/span/div/div/div').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # time.sleep(1)
        # # 开班点
        # driver.find_element_by_xpath('//*[@id="startDay"]/div/input').click()
        # time.sleep(1)
        # driver.find_element_by_css_selector('body > div:nth-child(11) > div > div > div > div > div.ant-calendar-date-panel > div.ant-calendar-footer > span > a').click()
        # time.sleep(1)
        # # 班别
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[3]/div[5]/div/div[2]/div/span/div/div/div').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # time.sleep(1)
        # time.sleep(1)
        # # 课次开始时间
        # driver.find_element_by_css_selector('#startTime').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[1]/input').send_keys(starthour)
        # time.sleep(1)
        #
        # time.sleep(1)
        # # 排课
        # driver.find_element_by_xpath('//*[@id="scheduleDay"]/label[1]/span[1]/input').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="intervalNum"]/div/div[2]/input').send_keys(1)
        # # 招生上线
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[4]/div[2]/div/div[2]/div/span/input').click()
        # time.sleep(1)
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[4]/div[2]/div/div[2]/div/span/input').send_keys(
        #     30)
        # time.sleep(1)
        #
        # # 授课教师
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[5]/div[1]/div/div[2]/div/span/div/div/div').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # time.sleep(1)
        # # 直播厂商
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[6]/div/div/div[2]/div/span/div/div/div').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul').find_element_by_class_name(
        #     'ant-select-dropdown-menu-item').click()
        # time.sleep(1)
        #
        # # 预排课
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/header/form/div[7]/button').click()
        # time.sleep(1)
        # time.sleep(2)
        # # 保存
        # driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/section/main/div[2]/button[2]').click()
        # time.sleep(2)
        # #教学通知
        # #driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/aside/div/ul/li[14]/div').click()
        # time.sleep(1)
        # driver.find_element_by_link_text('教学通知').click()
        # time.sleep(2)
        # #查询课号
        # driver.find_element_by_css_selector('#className').click()
        # driver.find_element_by_css_selector('#className').send_keys(class_time)
        # #driver.find_element_by_xpath('//*[@id="courseModuleClassName"]').send_keys(classname)
        # driver.find_element_by_xpath('//*[@id="hisroot"]/div/div/section/div/div/div/section/main/div/section/header/form/div/div[13]/button[1]').click()
        # time.sleep(3)
        # #异动
        # driver.find_element_by_css_selector('#hisroot > div > div > section > div > div > div > section > main > div > section > main > div > div > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(19) > span > span:nth-child(3) > a').click()
        # #输入上课日
        # time.sleep(3)
        #
        # driver.find_element_by_xpath('//*[@id="scheduleDay"]/div/input').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a').click()
        # time.sleep(1)
        #
        # #输入上课时
        # driver.find_element_by_xpath('//*[@id="startTime"]').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/input').send_keys(starthour)
        # time.sleep(1)
        #
        # #输入下课时
        # driver.find_element_by_xpath('//*[@id="endTime"]').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/input').send_keys(endhour)
        # time.sleep(1)
        #
        # #选择直播间
        # driver.find_element_by_xpath('//*[@id="resourceRoomId"]/div/div').click()
        # driver.find_element_by_xpath('//li[text()="直播间1"]').click()
        # time.sleep(1)
        #
        # #保存并确认
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[3]').click()
        # time.sleep(2)

        # 老师登陆
        electronic_login1(self)
        time.sleep(2)
        #
        # # 查询今天课程
        # driver.find_element_by_xpath('//*[@id="courseTime"]').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div/div[1]').click()
        # time.sleep(1)

        # 开始讲课
        w = driver.find_element_by_xpath("//td[contains(.,'" + class_time + "')]")
        try:
            ActionChains(driver).move_to_element_with_offset(w, 652, 17).click().perform()
        except:
            ActionChains(driver).move_to_element_with_offset(w, 582, 17).click().perform()
        finally:
            time.sleep(3)
            # 切换窗口句柄
            all = driver.window_handles
            driver.switch_to.window(all[1])

            # 点击启动云直播
            driver.switch_to.frame(0)
            driver.find_element_by_link_text('启动云直播').click()
            driver.switch_to.default_content()
            time.sleep(3)
            # 弹窗确认
            text = driver.switch_to.alert().text
            print(text)
            #driver.switch_to.alert().accept()

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
