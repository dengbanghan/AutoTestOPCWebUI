# -*- coding: utf-8 -*-
# @Time    : 2020/6/18
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : Deposit.py
# @Software: PyCharm

from base.basePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions

class Deposit(WebDriver):
    '''存款页面的元素和操作'''
    # 上传存款凭证 按钮的元素
    upload_deposit_btn = (By.CLASS_NAME,'btn-theme')
    # 二次弹窗的toast弹窗，由于和其他的弹窗的class不一样，所以在存款页面重新定义
    tips = (By.CLASS_NAME,'tips')
    # 存款相关费用说明 的内容
    explanation_content = (By.CLASS_NAME,'detail-text')
    # 存款金额输入框
    deposit_ibox = (By.CLASS_NAME,'md-input-item-fake')
    # 键盘数字的元素
    keyboard_number = (By.CLASS_NAME,'keyboard-number-item')
    # 键盘删除和确定按钮的元素
    keyboard_operate = (By.CLASS_NAME, 'keyboard-operate-item')

    def depositUpload(self):
        return self.findElement(*self.upload_deposit_btn)

    def tipsText(self):
        return self.findElement(*self.tips).text

    def explanationContent(self):
        return self.findElements(*self.explanation_content)

    def touchAction(self,Num):
        Action = TouchActions(self.driver)
        # Action.flick_element(self.explanationContent()[Num], 0, 500, 500).perform()
        Action.scroll_from_element(self.explanationContent()[0], 0, Num).perform()

    def depositIbox(self):
        return self.findElement(*self.deposit_ibox)

    def keyboardNumber(self):
        return self.findElements(*self.keyboard_number)

    def keyboardOperate(self):
        return self.findElements(*self.keyboard_operate)

    def virtualKeyboard(self,key):
        if key == 1:
            self.keyboardNumber()[12].click()
        if key == 2:
            self.keyboardNumber()[13].click()
        if key == 3:
            self.keyboardNumber()[14].click()
        if key == 4:
            self.keyboardNumber()[15].click()
        if key == 5:
            self.keyboardNumber()[16].click()
        if key == 6:
            self.keyboardNumber()[17].click()
        if key == 7:
            self.keyboardNumber()[18].click()
        if key == 8:
            self.keyboardNumber()[19].click()
        if key == 9:
            self.keyboardNumber()[20].click()
        if key == '.':
            self.keyboardNumber()[21].click()
        if key == 0:
            self.keyboardNumber()[22].click()
        if key == "删除":
            self.keyboardOperate()[0].click()
        if key == "确定":
            self.keyboardOperate()[1].click()