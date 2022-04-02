# -*- coding: utf-8 -*-
# @Time    : 2020/6/8
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : test_002_login.py
# @Software: PyCharm


from utils.operationXml import *
from selenium import webdriver
from tools.logger import *
from page.Login import *
from page.init import *
import unittest
import json

class Login(unittest.TestCase,Login,OperationXml,PublicElement):
    log = Logger("debug")

    chrome_note = tools.config.config('setUp.ini', 'chrome')
    login_info = tools.config.config('loginInfo.ini', 'login')
    chrome_driver = chrome_note['driver_path']

    host = login_info['host_web']
    areaNum = login_info['area_num']
    phoneNum = login_info['phone_num']

    chrome_options = webdriver.ChromeOptions()
    # 后台挂起 Google Chrome 浏览器，运行用例时隐藏 Google Chrome
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    '''登录页面测试用例'''
    @classmethod
    def setUpClass(self):
        '''必须使用@classmethod 装饰器,  所有case运行之前只运行一次'''
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.host)

    @classmethod
    def tearDownClass(self):
        '''必须使用@classmethod装饰器, 所有case运行完之后只运行一次'''
        self.driver.quit()

    def test_LoginPage_001(self):
        '''登录页面：检查登录页面的字段'''
        sleep(0.5)
        try:
            self.assertEqual("艾德一站通-标准版", self.getTitleText())
            self.assertEqual("手机号", self.getPhoneTabText())
            self.assertEqual("邮箱", self.getEmailTabText())
            self.assertEqual("+86", self.getDefaultAreaText())
            self.assertEqual("请输入手机号", self.getPhoneEmailInputText())
            self.assertEqual("验证码", self.getCodeTitleText())
            self.assertEqual("请输入验证码", self.getCodeInputText())
            self.assertEqual("获取验证码", self.getCodeBtnText())
            self.assertEqual("立即登录", self.getLoginBtnText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_LoginPage_002(self):
        '''登录页面：检查手机区号'''
        self.driver.refresh()
        self.clickSelectBtn()
        try:
            self.assertEqual("中国+86", self.getCNAreaText())
            self.assertEqual("中国香港+852", self.getHKAreaText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_LoginPage_003(self):
        '''登录页面：检查邮箱输入框'''
        self.driver.refresh()
        self.clickEmailTab()
        try:
            self.assertEqual("请输入邮箱", self.getPhoneEmailInputText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)