
import unittest
import HTMLTestRunner
import time

# 自动读取test_case文件夹下面所有以test开头的所有测试用例.

listcases = "test_study_service/"


def creatsuitel():
    testunit = unittest.TestSuite()

    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(listcases, pattern='test*.py', top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    print(testunit)
    return testunit





alltestnames = creatsuitel()

# 取前面时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 把当前时间加到测试报告文件名中
filename = now + listcases+'result.html'
fp = open(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'test result',
                                       description=u'the status of test case execution')

runner.run(alltestnames)
