# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 18:26
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : test_login.py
# @Software: PyCharm


from page.Login import *
from page.init import *

class Login(InitWeb,Login):
    log = Logger("debug")
    '''登录页面测试用例'''
    def test_LoginPage_001(self):
        '''大陆手机号登录'''
        self.driver.refresh()
        self.login("17722527464","666666")

    def test_LoginPage_002(self):
        '''点击获取验证码按钮'''
        self.driver.refresh()
        self.sendPhoneEmailBox("17722527464")
        self.clickCodeBtn()


    def test_LoginPage_003(self):
        '''点击获取验证码按钮'''
        self.driver.refresh()