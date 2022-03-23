# -*- coding: utf-8 -*-
# @Time    : 2020/5/22
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : UserInfo.py
# @Software: PyCharm

from base.basePage import *
from selenium.webdriver.common.by import By

class UserInfo(WebDriver):
    '''用户信息页面的元素和操作'''
    # 用户名
    user_name = (By.CLASS_NAME,'name')
    # 手机号码
    user_phone = (By.CLASS_NAME,'phone')
    # 地址
    address_text = (By.CLASS_NAME,'address-text')
    # 邮箱地址
    email_text = (By.CLASS_NAME,'email-text')
    # 副标题文案
    subtitle_text = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/p')
    # 添加记录超链接
    add_recording = (By.CLASS_NAME,'bank-card-info')
    # 添加香港银行卡按钮
    add_bank = (By.CLASS_NAME,'add-bank')

    def userInfo(self):
        '''
        将用户信息存放在列表中
        [0]用户名
        [1]手机号码
        [2]地址
        [3]邮箱地址
        '''
        user_info = []
        user_info.append(self.findElement(*self.user_name).text)
        user_info.append(self.findElement(*self.user_phone).text)
        user_info.append(self.findElement(*self.address_text).text)
        user_info.append(self.findElement(*self.email_text).text)
        return user_info

    def bankCardInfo(self):
        '''
        将用户信息存放在列表中
        [0]副标题
        [1]添加记录 按钮
        [2]添加香港银行卡 按钮
        '''
        bank_card_info = []
        bank_card_info.append(self.findElement(*self.subtitle_text))
        bank_card_info.append(self.findElement(*self.add_recording))
        bank_card_info.append(self.findElement(*self.add_bank))
        return bank_card_info

