# -*- coding: utf-8 -*-
# @Time    : 2020/6/5
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : Login.py
# @Software: PyCharm

from time import sleep

import base.basePage
from .PublicElement import *

class Login(PublicElement,WebDriver):
    '''登录页面的元素和操作'''
    # 跳转到登录页面的按钮
    login_title = (By.CLASS_NAME, 'logo-title')

    # 手机号tab
    phone_tab =(By.CLASS_NAME, 'phone-label')

    # 邮箱tab
    email_tab = (By.CLASS_NAME, 'email-label')

    # 区号下拉框
    area_item = (By.CLASS_NAME, 'select-item')

    #
    dropdown_content = (By.CLASS_NAME, 'ant-select-dropdown-content')

    # 弹窗提示
    notice_text = (By.CLASS_NAME,'ant-notification-notice-description')

    # 错误提示
    error_msg = (By.CLASS_NAME,'ant-notification-notice-description')

    # 输入框
    input_box = (By.CLASS_NAME, 'ant-input-lg')

    # 输入框标题
    input_box_title = (By.CLASS_NAME, 'ant-form-item-no-colon')

    # 获取验证码按钮
    code_btn = (By.CLASS_NAME, 'getCaptcha')

    # 登录按钮
    login_btn = (By.CLASS_NAME, 'login-button')

    # 未输入提示文案
    null_text = (By.CLASS_NAME,'ant-form-explain')

    def getselectId(self):
        sleep(0.5)
        return self.findElement(*self.dropdown_content).get_attribute("id")

    def getTitleText(self):
        '''获取标题'''
        return self.findElement(*self.login_title).text

    def getPhoneTabText(self):
        '''获取手机号tab标题'''
        return self.findElement(*self.phone_tab).text

    def getEmailTabText(self):
        '''获取邮箱tab标题'''
        return self.findElement(*self.email_tab).text

    def getDefaultAreaText(self):
        '''获取默认的区号'''
        return self.findElements(*self.area_item)[0].text

    def getCNAreaText(self):
        '''获取大陆区号'''
        id = self.getselectId()
        # 中国文案
        self.cn_text = (By.XPATH, '//*[@id="{0}"]/ul/li[1]/div/span[1]'.format(id))
        # +86文案
        self.bl_text = (By.XPATH, '//*[@id="{0}"]/ul/li[1]/div/span[2]'.format(id))
        return self.findElement(*self.cn_text).text + self.findElement(*self.bl_text).text

    def getHKAreaText(self):
        '''获取香港区号'''
        id = self.getselectId()
        # 中国香港文案
        self.hk_text = (By.XPATH, '//*[@id="{0}"]/ul/li[2]/div/span[1]'.format(id))
        # +852文案
        self.bwe_text = (By.XPATH, '//*[@id="{0}"]/ul/li[2]/div/span[2]'.format(id))
        return self.findElement(*self.hk_text).text + self.findElement(*self.bwe_text).text

    def getPhoneInputText(self):
        '''获取手机输入框文案'''
        return self.findElements(*self.input_box)[0].get_attribute("placeholder")

    def getEmailInputText(self):
        '''获取邮箱输入框文案'''
        return self.findElements(*self.input_box)[0].get_attribute("placeholder")

    def getCodeTitleText(self):
        '''获取验证码标题文案'''
        return self.findElements(*self.input_box_title)[1].text

    def getCodeInputText(self):
        '''获取验证码输入框文案'''
        return self.findElements(*self.input_box)[1].get_attribute("placeholder")

    def getCodeBtnText(self):
        '''获取验证码输入框文案'''
        return self.findElement(*self.code_btn).text

    def getLoginBtnText(self):
        '''获取验证码输入框文案'''
        return self.findElement(*self.login_btn).text

    def getPhoneNullText(self):
        '''获取手机号输入框为空的提示'''
        return self.findElements(*self.null_text)[0].get_attribute("textContent")

    def getEmailNullText(self):
        '''获取邮箱输入框为空的提示'''
        return self.findElements(*self.null_text)[0].get_attribute("textContent")

    def getCodeNullText(self):
        '''获取验证码输入框为空的提示'''
        return self.findElements(*self.null_text)[1].get_attribute("textContent")

    def getNoticeText(self):
        '''获取右上角弹窗提示信息'''
        return self.findElement(*self.notice_text).get_attribute("textContent")

    def getErrorText(self):
        '''获取错误提示信息'''
        return self.findElement(*self.notice_text).get_attribute("textContent")

    def getPhoenLength(self):
        '''获取手机号输入框已经输入文字的长度'''
        phone_input = self.findElements(*self.input_box)[0].get_attribute("value")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>",phone_input)
        return len(phone_input)

    def getCodeLength(self):
        '''获取验证码输入框已经输入文字的长度'''
        code_input = self.findElements(*self.input_box)[1].get_attribute("value")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>",code_input)
        return len(code_input)

    def clickSelectBtn(self):
        '''点击区号下拉框'''
        self.findElements(*self.area_item)[0].click()

    def clickCNBtn(self):
        '''点击大陆区号选项'''
        self.findElements(*self.area_item)[1].click()

    def clickHKBtn(self):
        '''点击香港区号选项'''
        self.findElements(*self.area_item)[2].click()

    def clickEmailTab(self):
        '''点击邮箱tab标题'''
        return self.findElement(*self.email_tab).click()

    def sendPhoneBox(self,phone):
        '''输入手机号'''
        self.findElements(*self.input_box)[0].send_keys(phone)

    def sendEmailBox(self,phone):
        '''输入邮箱'''
        self.findElements(*self.input_box)[0].send_keys(phone)

    def sendCodeBox(self,code):
        '''输入验证码'''
        self.findElements(*self.input_box)[1].send_keys(code)

    def clickLoginBtn(self):
        '''登录按钮'''
        self.findElement(*self.login_btn).click()

    def clickCodeBtn(self):
        '''获取验证码按钮'''
        self.findElement(*self.code_btn).click()

    def clickPhoneBox(self):
        '''点击手机号输入框'''
        self.findElements(*self.input_box)[0].click()

    def clickEmailBox(self):
        '''点击邮箱输入框'''
        self.findElements(*self.input_box)[0].click()

    def clickCodeBox(self):
        '''点击验证码输入框'''
        self.findElements(*self.input_box)[1].click()


    def login(self,phone,code):
        '''登录流程的完整操作步骤'''
        self.sendPhoneBox(phone)
        sleep(1)
        self.sendCodeBox(code)
        sleep(1)
        self.clickLoginBtn()
