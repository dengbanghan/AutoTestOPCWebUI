# -*- coding: utf-8 -*-
# @Time    : 2020/6/8
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : test_002_login.py
# @Software: PyCharm

# from browsermobproxy import Server
from utils.operationXml import *
from selenium import webdriver
from tools.logger import *
from page.Login import *
from page.init import *
import unittest
# import redis
import json

class Login(unittest.TestCase,Login,OperationXml,PublicElement):
    '''登录页面测试用例'''
    chrome_driver = r"D:\Program Files\Anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"

    # 后台挂起 Google Chrome 浏览器，运行用例时隐藏 Google Chrome
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    # 添加代理服务器
    # server = Server("F:\AutoTest\AutoTestWebUI\\base\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
    # server.start()
    # proxy = server.create_proxy()
    # proxy.new_har("ht_list2", options={'captureContent': True})

    # chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    # chrome_options.add_argument('--ignore-certificate-errors')

    url = "https://operation-center-web-sz-develop.eddid.com.cn:1443/"

    log = Logger("debug")

    # def getId(self):
    #     result = self.proxy.har
    #     for entry in result['log']['entries']:
    #         _url = entry['request']['url']
    #         # 根据URL找到数据接口,这里要找的是 http://git.liuyanlin.cn/get_ht_list 这个接口
    #         if "https://eddid-auth-center-uat.eddid.com.cn:1443/v2/captcha" in _url:
    #             _response = entry['response']
    #             _content = _response['content']
    #             _text = json.loads(_content['text'])
    #             return _text['data']['id']
    #     self.server.stop()
    #
    # def getCode(self):
    #     redis_host = 'r-wz9af3qz5xen9mi4j8pd.redis.rds.aliyuncs.com'
    #     redis_port = '6379'
    #     redis_passwd = 'admin@321'
    #     db = 1
    #     r = redis.Redis(host=redis_host, port=redis_port, password=redis_passwd,db=db,decode_responses=True)
    #     return r.get("{eac}:captcha:"+self.getId())
    #
    # @classmethod
    # def setUpClass(self):
    #     '''必须使用@classmethod 装饰器,  所有case运行之前只运行一次'''
    #     self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_options)
    #     self.driver.maximize_window()
    #     self.driver.get(self.url)
    #
    # @classmethod
    # def tearDownClass(self):
    #     '''必须使用@classmethod装饰器, 所有case运行完之后只运行一次'''
    #     self.driver.quit()
    #
    # def test_LoginPage_001(self):
    #     '''登录页面：检查登录页面的字段'''
    #     try:
    #         self.assertEqual("会员中心",self.getTitleText())
    #         self.assertEqual(self.getXmlData("Login_LangSimp"),self.selectLang().text)
    #         self.assertEqual(self.getXmlData("Login_AreaNumCN"),self.phoneAreaCode().text)
    #         self.assertEqual(self.getXmlData("Login_PhoneNumNull"), self.inputBox()[0].get_attribute('placeholder'))
    #         self.assertEqual(self.getXmlData("Login_PasswdNull"), self.inputBox()[1].get_attribute('placeholder'))
    #         self.assertEqual(self.getXmlData("Login_CodeNull"), self.inputBox()[2].get_attribute('placeholder'))
    #         self.assertEqual("登录", self.Button()[1].text)
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_002(self):
    #     '''登录页面：检查语言切换选项'''
    #     self.driver.refresh()
    #     self.selectLang().click()
    #     try:
    #         self.assertEqual(self.getXmlData("Login_LangSimp"),self.selectLangList2().text)
    #         self.assertEqual(self.getXmlData("Login_LangTraditional"),self.selectLangList1().text)
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_003(self):
    #     '''登录页面：切换语言为繁体中文'''
    #     self.driver.refresh()
    #     self.selectLang().click()
    #     self.selectLangList1().click()
    #     try:
    #         self.assertEqual(self.getXmlData("Login_LangTraditional"),self.selectLang().text)
    #         # 以下两个操作是将语言变为简体
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False, msg=e)
    #     self.selectLang().click()
    #     self.selectLangList2().click()
    #
    # def test_LoginPage_004(self):
    #     '''登录页面
    #     切换语言为简体中文'''
    #     self.driver.refresh()
    #     self.selectLang().click()
    #     self.selectLangList1().click()
    #     self.selectLang().click()
    #     self.selectLangList2().click()
    #     try:
    #         self.assertEqual(self.getXmlData("Login_LangSimp"),self.selectLang().text)
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_005(self):
    #     '''登录页面：检查区号切换选项'''
    #     self.driver.refresh()
    #     try:
    #         self.assertEqual(self.getXmlData("Login_AreaNumCN"), self.phoneAreaCode().text)
    #         self.assertEqual(self.getXmlData("Login_AreaNumHK"), self.phoneAreaCode().text)
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_006(self):
    #     '''登录页面：切换区号为中国香港'''
    #     self.driver.refresh()
    #     try:
    #         self.assertEqual(self.getXmlData("Login_AreaNumCN"),self.phoneAreaCode().text)
    #         self.assertEqual(self.getXmlData("Login_AreaNumHK"),self.phoneAreaCode().text)
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_007(self):
    #     '''登录页面：切换区号为中国内地'''
    #     self.driver.refresh()
    #     try:
    #         self.assertEqual(self.getXmlData("Login_AreaNumCN"), self.phoneAreaCode().text)
    #         self.assertEqual(self.getXmlData("Login_AreaNumHK"), self.phoneAreaCode().text)
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_008(self):
    #     '''登录页面：填写正确内容点击“登录”按钮'''
    #     self.driver.refresh()
    #     code = self.getCode()
    #     self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/personal-center")
    #     self.toLogin().click()
    #     self.login("17722527464","han920929",code)
    #     try:
    #         self.assertEqual("欢迎您",self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_009(self):
    #     '''登录页面：不填写任何内容点击“登录”按钮'''
    #     self.driver.refresh()
    #     self.login("","","")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PhoneNumNull"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdNull"),self.inputBoxMsg()[1].text)
    #         self.assertEqual(self.getXmlData("Login_CodeNull"),self.inputBoxMsg()[2].text)
    #         self.assertEqual(self.getXmlData("Login_PhoneNumNull"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_010(self):
    #     '''登录页面：输入的密码明文显示'''
    #     self.driver.refresh()
    #     self.login("17722527464","han920929","1234")
    #     try:
    #         self.assertEqual("han920929",self.inputBox()[1].get_attribute('value'))
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_011(self):
    #     '''登录页面：输入的密码密文显示'''
    #     self.driver.refresh()
    #     self.login("17722527464","han920929","1234")
    #     try:
    #         self.assertEqual("******",self.inputBox()[1].get_attribute('value'))
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_012(self):
    #     '''登录页面：不输入手机号码'''
    #     self.driver.refresh()
    #     self.login("","abc123","1234")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PhoneNumNull"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PhoneNumNull"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_013(self):
    #     '''登录页面：不输入密码'''
    #     self.driver.refresh()
    #     self.login("17722527464","","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdNull"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdNull"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_014(self):
    #     '''登录页面：不输入验证码'''
    #     self.driver.refresh()
    #     self.login("17722527464","abc123","")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_CodeNull"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_CodeNull"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_015(self):
    #     '''登录页面：输入不足11位的手机号码（内地手机号）'''
    #     self.driver.refresh()
    #     self.login("1772252746","abc123","1234")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PhoneNumRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PhoneNumRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_016(self):
    #     '''登录页面：输入超过11位的手机号码（内地手机号）'''
    #     self.driver.refresh()
    #     self.login("177225274641234","abc123","1234")
    #     try:
    #         self.assertEqual("177 2252 7464",self.inputBox()[0].get_attribute('value'))
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_017(self):
    #     '''登录页面：输入不足8位的手机号码（香港手机号）'''
    #     self.driver.refresh()
    #     self.login("1772252","abc123","1234")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PhoneNumRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PhoneNumRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_018(self):
    #     '''登录页面：输入超过8位的手机号码（香港手机号）'''
    #     self.driver.refresh()
    #     self.login("17722527464","abc123","1234")
    #     try:
    #         self.assertEqual("177 225 27",self.inputBox()[0].get_attribute('value'))
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_019(self):
    #     '''登录页面：手机号码输入框输入字符'''
    #     self.driver.refresh()
    #     self.login("asdsdafd","han920929","1234")
    #     try:
    #         self.assertEqual("",self.inputBox()[0].get_attribute('value'))
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_020(self):
    #     '''登录页面：输入错误的密码'''
    #     self.driver.refresh()
    #     self.login("17722527464","han9209291",self.getCode())
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdErr"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_021(self):
    #     '''登录页面：输入的密码为6位数的纯数字'''
    #     self.driver.refresh()
    #     self.login("17722527464","123456","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_022(self):
    #     '''登录页面：输入的密码为不足6位数的纯数字'''
    #     self.driver.refresh()
    #     self.login("17722527464","12345","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_023(self):
    #     '''登录页面：输入的密码为6位数的纯小写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","abcdef","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_024(self):
    #     '''登录页面：输入的密码为不足6位数的纯小写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","abcde","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_025(self):
    #     '''登录页面：输入的密码为6位数的纯大写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","ABCDEF","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_026(self):
    #     '''登录页面：输入的密码为不足6位数的纯大写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","ABCDE","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_027(self):
    #     '''登录页面：输入的密码为不足6位数的小写字母和数字混合'''
    #     self.driver.refresh()
    #     self.login("17722527464","abc12","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_028(self):
    #     '''登录页面：输入的密码为不足6位数的大写字母和数字混合'''
    #     self.driver.refresh()
    #     self.login("17722527464","ABC12","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_029(self):
    #     '''登录页面：输入的密码为不足6位数的大小写字母和数字混合'''
    #     self.driver.refresh()
    #     self.login("17722527464","ABc12","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_030(self):
    #     '''登录页面：输入的密码为超过16位数的纯数字'''
    #     self.driver.refresh()
    #     self.login("17722527464","12345678901234567","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_031(self):
    #     '''登录页面：输入的密码为超过16位数的纯小写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","asdfghjklqwertyui","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_032(self):
    #     '''登录页面：输入的密码为超过16位数的纯大写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","ASDFGHJKLQWERTYUI","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_033(self):
    #     '''登录页面：输入的密码为超过16位数的小写字母和数字混合'''
    #     self.driver.refresh()
    #     self.login("17722527464","123456789qwertyui","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_034(self):
    #     '''登录页面：输入的密码为超过16位数的大写字母和数字混合'''
    #     self.driver.refresh()
    #     self.login("17722527464","123456789QWERTYUI","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_035(self):
    #     '''登录页面：输入的密码为超过16位数的大小写字母和数字混合'''
    #     self.driver.refresh()
    #     self.login("17722527464","123456789qwerTYUI","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_036(self):
    #     '''登录页面：输入的密码为大于6且小于16位数的纯数字'''
    #     self.driver.refresh()
    #     self.login("17722527464","123456789","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_037(self):
    #     '''登录页面：输入的密码为大于6且小于16位数的纯小写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","abcdefg","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_038(self):
    #     '''登录页面：输入的密码为大于6且小于16位数的纯大写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","ABCDEFG","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_039(self):
    #     '''登录页面：输入的密码为大于6且小于16位数的大小写字母'''
    #     self.driver.refresh()
    #     self.login("17722527464","ABCDefg","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_PasswdRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_040(self):
    #     '''登录页面：输入的密码包含特殊字符'''
    #     self.driver.refresh()
    #     self.login("17722527464","asd12345;@",self.getCode())
    #     try:
    #         self.assertEqual(self.getXmlData("Login_PasswdErr"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_041(self):
    #     '''登录页面：输入错误的验证码'''
    #     self.driver.refresh()
    #     self.login("17722527464","han920929","1231")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_CodeErr"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_042(self):
    #     '''登录页面：输入不足4位的验证码'''
    #     self.driver.refresh()
    #     self.login("17722527464","han920929","12")
    #     try:
    #         self.assertEqual(self.getXmlData("Login_CodeRule"),self.inputBoxMsg()[0].text)
    #         self.assertEqual(self.getXmlData("Login_CodeRule"),self.toastText())
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_043(self):
    #     '''登录页面：输入超过4位的验证码'''
    #     self.driver.refresh()
    #     self.login("17722527464","han920929","1234567")
    #     try:
    #         self.assertEqual("1234",self.inputBox()[2].get_attribute('value'))
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)
    #
    # def test_LoginPage_044(self):
    #     '''登录页面：验证码输入框输入字符'''
    #     self.driver.refresh()
    #     self.login("17722527464","han920929","abcd")
    #     try:
    #         self.assertEqual("",self.inputBox()[2].get_attribute('value'))
    #     except Exception as e:
    #         self.log.error(e)
    #         self.assertTrue(False,msg=e)

    def test_LoginPage_045(self):
        '''大陆手机号登录'''
        self.driver.refresh()
        self.login("17722527464","666666")
        try:
            self.assertEqual("",self.inputBox()[2].get_attribute('value'))
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)