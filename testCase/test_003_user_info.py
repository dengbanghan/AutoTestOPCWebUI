# -*- coding: utf-8 -*-
# @Time    : 2020/5/28
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : test_003_user_info.py
# @Software: PyCharm

from page.UserInfo import *
from page.PublicElement import *
from page.Init import *

class UserInfo(InitWeb,UserInfo,PublicElement):
    '''用户信息页面'''
    log = Logger("debug")
    def test_UserInfo_001(self):
        '''用户信息页面：检查用户信息页面内容'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo")
        try:
            self.assertEqual("邓 帮涵", self.userInfo()[0])
            self.assertEqual("17722527464", self.userInfo()[1])
            self.assertEqual("深圳南山", self.userInfo()[2])
            self.assertEqual("dengbanghan@edsz9.com",self.userInfo()[3])
            self.assertEqual("银行信息",self.bankCardInfo()[0].text)
            self.assertEqual("添加记录", self.bankCardInfo()[1].text)
            self.assertEqual("添加香港银行卡", self.bankCardInfo()[2].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_002(self):
        '''用户信息页面：跳转到“添加香港银行卡”页面'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo")
        self.bankCardInfo()[2].click()
        try:
            self.assertEqual("添加香港银行卡", self.titleText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_003(self):
        '''用户信息页面：检查添加银行卡页面标题'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo/create")
        try:
            self.assertEqual("添加香港银行卡", self.titleText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_004(self):
        '''用户信息页面：检查添加银行卡页面输入框标题文案'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo/create")
        try:
            self.assertEqual("银行名称", self.inputBoxTitle()[0].text)
            self.assertEqual("银行账号", self.inputBoxTitle()[1].text)
            self.assertEqual("账户持有人姓名/英文", self.inputBoxTitle()[2].text)
            self.assertEqual("账户持有人姓名/中文", self.inputBoxTitle()[3].text)
            self.assertEqual("银行货币", self.inputBoxTitle()[4].text)
            self.assertEqual("请上传银行证明", self.inputBoxTitle()[5].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_005(self):
        '''用户信息页面：检查添加银行卡页面输入框默认显示'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo/create")
        try:
            self.assertEqual("请输入", self.inputBox()[0].get_attribute('placeholder'))
            self.assertEqual("请输入", self.inputBox()[1].get_attribute('placeholder'))
            self.assertEqual("帮涵 邓", self.inputBox()[2].get_attribute('placeholder'))
            self.assertEqual("邓帮涵", self.inputBox()[3].get_attribute('placeholder'))
            self.assertEqual("港币", self.selectBox()[4].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_006(self):
        '''用户信息页面：银行名称为空'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo/create")
        self.Button()[0].click()
        try:
            self.assertEqual("请输入正确的银行名称", self.toastText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_007(self):
        '''用户信息页面：银行账号为空'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo/create")
        self.inputBox()[0].send_keys("中国银行")
        self.Button()[0].click()
        try:
            self.assertEqual("请输入正确的银行账户", self.toastText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_008(self):
        '''用户信息页面：银行证明为空'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo/create")
        self.inputBox()[0].send_keys("中国银行")
        self.inputBox()[1].send_keys("887652004378992")
        self.Button()[0].click()
        try:
            self.assertEqual("请上传银行证明", self.toastText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_009(self):
        '''用户信息页面：跳转到“银行卡添加记录”页面'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo")
        self.bankCardInfo()[1].click()
        try:
            self.assertEqual("银行卡添加记录", self.titleText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_010(self):
        '''用户信息页面：示添加的银行卡的信息'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo")
        self.bankCardInfo()[1].click()
        try:
            self.assertEqual("暂无银行卡添加记录", self.titleText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_UserInfo_011(self):
        '''用户信息页面：没有添加的银行卡的信息'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/accountInfo")
        self.bankCardInfo()[1].click()
        try:
            self.assertEqual("暂无记录", self.Text())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

if __name__ == '__main__':
    unittest.main(verbosity=2)