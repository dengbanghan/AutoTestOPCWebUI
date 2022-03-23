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
from time import sleep

class InitWeb(unittest.TestCase,OperationXml,GetToken):
    log = Logger("debug")
    # chrome_driver = tools.config.config('setUp.ini', 'chrome')
    chrome_driver = r"D:\Program Files (x86)\Anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    # 禁用W3C
    # chrome_options.add_experimental_option('w3c', False)

    # 后台挂起 Google Chrome 浏览器，运行用例时隐藏 Google Chrome
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    url = "https://operation-center-web-sz-develop.eddid.com.cn:1443/"
    gt = GetToken()
    access_token = gt.sign_login('17722527464', '+86', '666666')

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

        self.driver.get(self.url)
        value = ["'{"+'"value":"{}"'.format(self.access_token)+',"expire":1648431142300'+"}'"]
        js = 'window.localStorage.setItem("pro__Access-Token", {});'.format(value[0])
        self.driver.execute_script(js)

        self.driver.refresh()

    # @classmethod
    # def tearDownClass(self):
    #     '''必须使用@classmethod装饰器, 所有case运行完之后只运行一次'''
    #     self.driver.quit()