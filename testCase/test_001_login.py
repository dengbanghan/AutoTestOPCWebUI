# -*- coding: utf-8 -*-
# @Time    : 2020/6/8
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : test_001_login.py
# @Software: PyCharm


from utils.operationXml import *
from selenium import webdriver
from tools.logger import *
from page.Login import *
from page.Init import *
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
            self.assertEqual("请输入手机号", self.getPhoneInputText())
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
            self.assertEqual("请输入邮箱", self.getEmailInputText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_004(self):
        '''登录页面：检查手机号和验证码输入框都为空的提示'''
        self.driver.refresh()
        self.clickPhoneBox()
        self.clickCodeBox()
        self.clickCodeBtn()
        try:
            self.assertEqual("请输入正确的手机号", self.getPhoneNullText())
            self.assertEqual("请输入验证码", self.getCodeNullText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_005(self):
        '''登录页面：检查手机号输入框为空的提示'''
        self.driver.refresh()
        self.clickPhoneBox()
        self.clickCodeBtn()
        try:
            self.assertEqual("请输入正确的手机号", self.getPhoneNullText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_006(self):
        '''登录页面：检查验证码输入框为空的提示'''
        self.driver.refresh()
        self.clickCodeBox()
        self.clickCodeBtn()
        try:
            self.assertEqual("请输入验证码", self.getCodeNullText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_007(self):
        '''登录页面：检查邮箱和验证码输入框都为空的提示'''
        self.driver.refresh()
        self.clickEmailTab()
        self.clickEmailBox()
        self.clickCodeBox()
        self.clickCodeBtn()
        try:
            self.assertEqual("请输入正确的邮箱", self.getEmailNullText())
            self.assertEqual("请输入验证码", self.getCodeNullText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_008(self):
        '''登录页面：检查邮箱输入框为空的提示'''
        self.driver.refresh()
        self.clickEmailTab()
        self.clickEmailBox()
        self.clickCodeBtn()
        try:
            self.assertEqual("请输入正确的邮箱", self.getEmailNullText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_009(self):
        '''登录页面：输入错误的手机号的提示'''
        self.driver.refresh()
        self.sendPhoneBox('17722')
        self.clickCodeBtn()
        try:
            self.assertEqual("发送失败,请核对登陆账号", self.getNoticeText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_010(self):
        '''登录页面：输入错误的手机号和验证码的提示'''
        self.driver.refresh()
        self.sendPhoneBox('1772252')
        self.sendCodeBox("123456")
        self.clickLoginBtn()
        try:
            self.assertEqual("账户密码错误,请核对", self.getErrorText())
            self.assertEqual("账户密码错误,请核对", self.getNoticeText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_011(self):
        '''登录页面：输入错误的验证码的提示'''
        self.driver.refresh()
        self.sendPhoneBox('17722527464')
        self.sendCodeBox("123456")
        self.clickLoginBtn()
        try:
            self.assertEqual("验证码校验失败", self.getErrorText())
            self.assertEqual("验证码校验失败", self.getNoticeText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_loginPage_012(self):
        '''登录页面：检验验证码的长度 '''
        self.driver.refresh()
        self.sendCodeBox('1234567891011')
        try:
            self.assertEqual(6, self.getCodeLength())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

if __name__ == '__main__':
    unittest.main(verbosity=2)