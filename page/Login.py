# -*- coding: utf-8 -*-
# @Time    : 2020/6/5
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : Login.py
# @Software: PyCharm

from time import sleep
from .PublicElement import *

class Login(PublicElement,WebDriver):
    '''登录页面的元素和操作'''

    # 跳转到登录页面的按钮
    login_title = (By.CLASS_NAME,'logo-title')
    # 手机号tab
    login_phone =(By.CLASS_NAME,'phone-label active-label')
    # 邮箱tab
    login_email = (By.CLASS_NAME, 'email-label')
    # 区号下拉框
    area_item = (By.CLASS_NAME,'select-item')
    # 输入框
    input_box = (By.CLASS_NAME,'ant-input-lg')
    # 获取验证码按钮
    code_btn = (By.CLASS_NAME,'getCaptcha')
    # 登录按钮
    login_btn = (By.CLASS_NAME,'login-button')
    # 未输入提示文案
    explain_text = (By.CLASS_NAME,'ant-form-explain')

    def sendPhoneEmailBox(self,phone):
        '''手机号&邮箱输入框'''
        input_box = self.findElements(*self.input_box)
        input_box[0].send_keys(phone)

    def sendCodeBox(self,code):
        '''验证码输入框'''
        input_box = self.findElements(*self.input_box)
        input_box[1].send_keys(code)

    def clickLoginBtn(self):
        '''登录按钮'''
        self.findElement(*self.login_btn).click()

    def clickCodeBtn(self):
        '''获取验证码按钮'''
        self.findElement(*self.code_btn).click()

    def login(self,phone,code):
        '''登录流程的完整操作步骤'''
        self.sendPhoneEmailBox(phone)
        sleep(1)
        self.sendCodeBox(code)
        sleep(1)
        self.clickLoginBtn()
