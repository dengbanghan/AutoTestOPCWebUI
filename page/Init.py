# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:35
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : init.py
# @Software: PyCharm

import unittest
from utils.operationXml import *
from selenium import webdriver
from base.getToken import *
from base.getSmsCode import *
from tools.time_convert import *
import re

class InitWeb(unittest.TestCase, OperationXml, GetToken, getCode, TimeConvert):
    log = Logger("debug")
    tc = TimeConvert()

    chrome_note = tools.config.config('setUp.ini', 'chrome')
    login_info = tools.config.config('loginInfo.ini', 'login')
    chrome_driver = chrome_note['driver_path']

    chrome_options = webdriver.ChromeOptions()
    # 禁用W3C
    # chrome_options.add_experimental_option('w3c', False)

    # 后台挂起 Google Chrome 浏览器，运行用例时隐藏 Google Chrome
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    host = login_info['host_web']
    areaNum = login_info['area_num']
    phoneNum = login_info['phone_num']
    smsCode = getCode().getCode(phoneNum)
    access_token = GetToken().get_token(phoneNum,areaNum)

    # def setUp(self):
    #     '''每个测试case运行之前运行'''
    #     self.driver.refresh()

    # def tearDown(self):
    #     '''每个测试case运行完之后执行'''
    #     self.driver.quit()

    @classmethod
    def setUpClass(self):
        '''必须使用@classmethod 装饰器,  所有case运行之前只运行一次'''
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.host)

        expire_time_stamp = str(self.tc.get_shanghai_timestamp((str(datetime.datetime.now() + datetime.timedelta(days=7)))[:-7]))
        value = ["'{"+'"value":"{}"'.format(self.access_token)+',"expire":'+expire_time_stamp+'0000'+"}'"] # expire 为 token 的有效时间，expire_time_stamp 为当前时间+7天后的时间戳
        js = 'window.localStorage.setItem("pro__Access-Token", {});'.format(value[0])

        self.driver.execute_script(js)
        self.driver.refresh()

    @classmethod
    def tearDownClass(self):
        '''必须使用@classmethod装饰器, 所有case运行完之后只运行一次'''
        self.driver.quit()