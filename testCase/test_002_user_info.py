# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 1:48
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : test_002_user_info.py
# @Software: PyCharm

from page.UserInfo import *
from page.Init import *
from time import sleep

class UserInfo(InitWeb, UserInfo):
    '''个人中心首页'''
    log = Logger("debug")
    def home(self):
        self.driver.get("https://operation-center-web-sz-delevop.eddid.com.cn:1443/user-search/user-info")

    def login(self):
        self.driver.execute_script('localStorage.setItem("accessToken", "{0}");'.format(self.access_token))
        self.driver.refresh()

    def logout(self):
        self.driver.execute_script('localStorage.setItem("accessToken", "{0}");'.format("asdfsdfjksdggfgjkh"))
        self.driver.refresh()

    def test_AccountCenter_001(self):
        '''个人中心：检查个人中心页面(未登录)'''
        self.login()
        print(self.getUserDatas())
        print(self.getPhones())

    def test_AccountCenter_002(self):
        '''个人中心：检查个人中心页面(已登录)'''
        self.login()
        try:
            self.assertEqual("个人中心",self.accountTitle())
            self.assertEqual("存款", self.firstFunList()[0].text)
            self.assertEqual("取款", self.firstFunList()[1].text)
            self.assertEqual("内部转账", self.firstFunList()[2].text)
            self.assertEqual("换汇", self.firstFunList()[3].text)
            self.assertEqual("子账户申请", self.secondFunLeft().text)
            self.assertEqual("业务申请", self.secondFunRight().text)
            self.assertEqual("账户信息", self.functionList()[0].text)
            self.assertEqual("资金记录", self.functionList()[1].text)
            self.assertEqual("账户设置", self.functionList()[2].text)
            self.assertEqual("联系客服", self.functionList()[3].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)


if __name__ == '__main__':
    unittest.main(verbosity=2)