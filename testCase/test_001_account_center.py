# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 1:48
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : test_001_account_center.py
# @Software: PyCharm

from page.AccountCenter import *
from page.init import *
from time import sleep

class AccountCenter(InitWeb,AccountCenter):
    '''个人中心首页'''
    log = Logger("debug")
    def home(self):
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/personal-center")

    def login(self):
        self.driver.execute_script('localStorage.setItem("accessToken", "{0}");'.format(self.access_token))
        self.driver.refresh()

    def logout(self):
        self.driver.execute_script('localStorage.setItem("accessToken", "{0}");'.format("asdfsdfjksdggfgjkh"))
        self.driver.refresh()

    def test_AccountCenter_001(self):
        '''个人中心：检查个人中心页面(未登录)'''
        self.logout()
        try:
            self.assertEqual("个人中心",self.accountTitle())
            self.assertEqual("登录",self.toLogin().text)
            self.assertEqual("注册",self.registBtn().text)
            self.assertEqual("存款",self.firstFunList()[0].text)
            self.assertEqual("取款",self.firstFunList()[1].text)
            self.assertEqual("内部转账",self.firstFunList()[2].text)
            self.assertEqual("换汇",self.firstFunList()[3].text)
            self.assertEqual("子账户申请",self.secondFunLeft().text)
            self.assertEqual("业务申请",self.secondFunRight().text)
            self.assertEqual("账户信息",self.functionList()[1].text)
            self.assertEqual("资金记录",self.functionList()[2].text)
            self.assertEqual("账户设置",self.functionList()[3].text)
            self.assertEqual("联系客服",self.functionList()[4].text)
        except Exception as e:
                    self.log.error(e)
                    self.assertTrue(False,msg=e)

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

    def test_AccountCenter_003(self):
        '''个人中心：点击“登录”按钮'''
        self.logout()
        self.driver.refresh()
        self.toLogin().click()
        try:
            self.assertEqual("登录",self.Button()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_004(self):
        '''个人中心：点击“注册”按钮'''
        self.logout()
        self.home()
        self.driver.refresh()
        self.registBtn().click()
        try:
            self.assertEqual("注册",self.registPageBtn())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_005(self):
        '''个人中心：点击存款（未登录）'''
        self.logout()
        self.firstFunList()[0].click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_006(self):
        '''个人中心：点击取款（未登录）'''
        self.logout()
        self.firstFunList()[1].click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_007(self):
        '''个人中心：点击内部转账（未登录）'''
        self.logout()
        self.firstFunList()[2].click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_008(self):
        '''个人中心：点击换汇（未登录）'''
        self.logout()
        self.firstFunList()[3].click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_009(self):
        '''个人中心：点击子账户申请（未登录）'''
        self.logout()
        self.secondFunLeft().click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_010(self):
        '''个人中心：点击业务申请（未登录）'''
        self.logout()
        self.secondFunRight().click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_011(self):
        '''个人中心：点击账户信息（未登录）'''
        self.logout()
        self.functionList()[0].click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_012(self):
        '''个人中心：点击资金记录（未登录）'''
        self.logout()
        self.functionList()[1].click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_013(self):
        '''个人中心：点击账户设置（未登录）'''
        self.logout()
        self.functionList()[2].click()
        try:
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_014(self):
        '''个人中心：检查登录提示弹窗的内容'''
        self.logout()
        self.firstFunList()[0].click()
        try:
            self.assertEqual("请先登录", self.loginTip()[0].text)
            self.assertEqual("您还没登录，请先登录",self.loginTip()[1].text)
            self.assertEqual("下次再说", self.loginTip()[2].text)
            self.assertEqual("登录", self.loginTip()[3].text)
        except Exception as e:
                    self.log.error(e)
                    self.assertTrue(False,msg=e)

    def test_AccountCenter_015(self):
        '''个人中心：点击“x”按钮'''
        self.logout()
        self.firstFunList()[0].click()
        self.hover(self.loginTip()[4])
        self.loginTip()[4].click()

    def test_AccountCenter_016(self):
        '''个人中心：点击“下次再说”按钮'''
        self.logout()
        self.firstFunList()[0].click()
        self.loginTip()[2].click()

    def test_AccountCenter_017(self):
        '''个人中心：点击“登录”按钮'''
        self.logout()
        self.firstFunList()[0].click()
        self.loginTip()[3].click()
        try:
            self.assertEqual("登录", self.Button()[1].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_018(self):
        '''个人中心：点击用户头像（已登录）'''
        self.home()
        self.login()
        self.driver.refresh()
        self.clickUserIcon()

    def test_AccountCenter_019(self):
        '''个人中心：点击欢迎词（已登录）'''
        self.home()
        self.userName().click()

    def test_AccountCenter_020(self):
        '''个人中心：点击存款（已登录）'''
        self.home()
        self.firstFunList()[0].click()
        try:
            self.assertEqual("存款",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_021(self):
        '''个人中心：点击取款（已登录）'''
        self.home()
        self.firstFunList()[1].click()
        try:
            self.assertEqual("取款",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_022(self):
        '''个人中心：点击内部转账（已登录）'''
        self.home()
        self.firstFunList()[2].click()
        try:
            self.assertEqual("内部转账",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_023(self):
        '''个人中心：点击换汇（已登录）'''
        self.home()
        self.firstFunList()[3].click()
        try:
            self.assertEqual("换汇",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_024(self):
        '''个人中心：点击子账户申请（已登录）'''
        self.home()
        self.secondFunLeft().click()
        try:
            self.assertEqual("银行子账户",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_025(self):
        '''个人中心：点击业务申请（已登录）'''
        self.home()
        self.secondFunRight().click()
        try:
            self.assertEqual("业务申请",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_026(self):
        '''个人中心：点击账户信息（已登录）'''
        self.home()
        self.functionList()[0].click()
        try:
            self.assertEqual("账户信息",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_027(self):
        '''个人中心：点击资金记录（已登录）'''
        self.home()
        self.functionList()[1].click()
        try:
            self.assertEqual("资金记录",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_028(self):
        '''个人中心：点击账户设置（已登录）'''
        self.home()
        self.functionList()[2].click()
        try:
            self.assertEqual("账户设置",self.accountTitle())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_AccountCenter_029(self):
        '''个人中心：点击联系客服（已登录）'''
        self.home()
        self.functionList()[3].click()
        try:
            self.assertEqual("我知道了",self.iKnowBtn().text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

if __name__ == '__main__':
    unittest.main(verbosity=2)