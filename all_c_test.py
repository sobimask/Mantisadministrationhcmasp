
import unittest
import time
import HTMLTestRunner


# 循环添加用例

pyname = ["test_configuration","test_product_manage","test_all","test_study_service","test_teaching_operation",'test_financial_management']
#pyname = ['test_all']
for i in range(len(pyname)):
    listcases = pyname[i]
    # 添加用例文件夹到discover方法中
    discover = unittest.defaultTestLoader.discover(listcases, pattern='test*.py', top_level_dir = '../')   #由于discover多次调用，top_level_dir参数要写成子目录的上级目录，默认为None
    testunit = unittest.TestSuite()
    #测试集在discover中循环添加
    for test_suite in discover:
        #case在测试集中循环添加
        for test_case in test_suite:
            testunit.addTests(test_case)

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 把当前时间加到测试报告文件名中
    filename = "testResult/" + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'test result',
                                           description=u'the status of test case execution')
    runner.run(discover)


