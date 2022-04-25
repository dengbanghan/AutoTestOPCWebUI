# -*- coding: utf-8 -*-
# @Time    : 2020/6/18
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : test_004_deposit.py
# @Software: PyCharm

from page.PublicElement import *
from page.Deposit import *
from page.Init import *
from time import sleep

class Deposit(InitWeb,Deposit,PublicElement):
    log = Logger("debug")
    '''存款页面'''
    def test_Deposit_001(self):
        '''个人中心：检查存款页面内容'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/deposit")
        try:
            self.assertEqual("存款",self.titleText())
            self.assertEqual("最新记录", self.rightBtn().text)
            self.assertEqual("不支持第三方存款",self.topTip().text)
            self.assertEqual("FPS转数快", self.functionCards()[0].text)
            self.assertEqual("网上银行存款", self.functionCards()[1].text)
            self.assertEqual("ATM 转账", self.functionCards()[2].text)
            self.assertEqual("银行柜台转账", self.functionCards()[3].text)
            self.assertEqual("支票存款", self.functionCards()[4].text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_Deposit_002(self):
        '''个人中心：跳转到“FPS转数快”页面'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/deposit")
        self.functionCards()[0].click()
        try:
            self.assertEqual("FPS转数快", self.titleText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_Deposit_003(self):
        '''个人中心：检查“FPS转数快”页面内容'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/depositMatter?title=fps_deposit&name=FPS转数快")
        try:
            self.assertEqual("FPS转数快", self.titleText())
            self.assertEqual("注意事项", self.rightBtn().text)
            self.assertEqual("请阅读存款注意事项，并按以下流程办理汇款申请。", self.topTip().text)
            self.assertEqual("上传存款凭证", self.depositUpload().text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_Deposit_004(self):
        '''个人中心：FPS转数快跳转到上传凭证页面'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/depositMatter?title=fps_deposit&name=FPS转数快")
        self.depositUpload().click()
        self.touchAction(200)
        self.dialogBtn()[1].click()
        self.depositIbox().click()
        sleep(0.5)
        self.virtualKeyboard(1)
        self.virtualKeyboard(0)
        self.virtualKeyboard(0)
        try:
            self.assertEqual("100",self.depositIbox().text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_Deposit_005(self):
        '''个人中心：FPS转数快跳-触发“存款相关费用说明”弹窗'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/depositMatter?title=fps_deposit&name=FPS转数快")
        self.depositUpload().click()
        self.dialogBtn()[1].click()
        try:
            self.assertTrue(self.isElementExist(*self.dialog_title), msg="页面不存在协议确认弹窗")
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_Deposit_006(self):
        '''个人中心：FPS转数快-同意存款相关费用说明-直接点击“同意并继续”按钮'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/depositMatter?title=fps_deposit&name=FPS转数快")
        self.depositUpload().click()
        self.touchAction(0)
        self.dialogBtn()[1].click()
        js = "document.getElementsByClassName('tips')[0].style.display='block';"
        self.driver.execute_script(js)
        try:
            self.assertEqual("请滑动并阅读所有",self.tipsText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)

    def test_Deposit_007(self):
        '''个人中心：FPS转数快-同意存款相关费用说明-将内容滑动到底部再点击“同意并继续”按钮'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/depositMatter?title=fps_deposit&name=FPS转数快")
        self.depositUpload().click()
        self.touchAction(200)
        self.dialogBtn()[1].click()
        self.depositIbox().click()
        sleep(0.5)
        self.virtualKeyboard(1)
        self.virtualKeyboard(0)
        self.virtualKeyboard(0)
        try:
            self.assertEqual("100", self.depositIbox().text)
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False, msg=e)

    def test_Deposit_008(self):
        '''个人中心：FPS转数快-同意存款相关费用说明-将内容滑动到一半的位置再点击“同意并继续”按钮'''
        self.driver.get("http://account-center-h5-uat.eddid.com.cn:180/depositMatter?title=fps_deposit&name=FPS转数快")
        self.depositUpload().click()
        self.touchAction(100)
        self.dialogBtn()[1].click()
        try:
            self.assertEqual("请滑动并阅读所有",self.tipsText())
        except Exception as e:
            self.log.error(e)
            self.assertTrue(False,msg=e)