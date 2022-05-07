# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:40
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : allTest.py
# @Software: PyCharm

from base import HTMLTestRunnerNew
import os
import time
import unittest

def allTests():
    '''获取所有需要执行的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), 'testCase'),
        pattern='test_001*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    '''获取当前的时间'''
    # 精确到秒的时间格式：%Y-%m-%d %H_%M_%S
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))

if __name__ == '__main__':

    report_path = os.path.join(os.path.dirname(__file__), 'report')
    if not os.path.exists(report_path):  # 创建报告目录
        os.makedirs(report_path)
    fileName = os.path.join(os.path.dirname(__file__), 'report', 'EddidTestReport_{0}.html'.format(getNowTime()))
    with open(fileName, 'wb+') as file:
        runner = HTMLTestRunnerNew.HTMLTestRunner(
            file,
            title='个人中心测试报告',
            description='个人中心',
            tester='dengbanghan')
        runner.run(allTests())