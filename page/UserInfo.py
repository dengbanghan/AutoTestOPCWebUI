# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 1:47
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : UserInfo.py
# @Software: PyCharm

from page.Login import *
from page.PublicElement import *

class UserInfo(PublicElement, WebDriver):
    '''用户信息页面的元素和操作'''
    def getUserDatas(self):
        # 定位表格
        sleep(1)
        table = self.findElement(*self.table_tbody)
        return self.getTableDatas(table)

    def getPhones(self):
        return self.getLists(self.getUserDatas())

    def iKnowBtn(self):
        '''联系客服弹窗的 我知道了 按钮'''
        return self.findElement(*self.i_know_btn)

    def loginTip(self):
        '''
        将提醒弹窗的元素放到列表中
        [0]标题
        [1]提示语
        [2]左边按钮
        [3]右边按钮
        '''
        tip = []
        tip.append(self.findElement(*self.login_tip_title))
        tip.append(self.findElement(*self.login_tip_text))
        tip.append(self.findElement(*self.login_tip_btn_left))
        tip.append(self.findElement(*self.login_tip_btn_right))
        tip.append(self.findElement(*self.login_tip_btn_close))
        return tip

    def clickUserIcon(self):
        '''点击用户头像'''
        self.findElement(*self.user_icon).click()

    def registPageBtn(self):
        '''注册页面的注册按钮'''
        return "现在的注册按钮还无法点击"

    def registBtn(self):
        '''个人中心首页未登录状态时的注册按钮的元素'''
        return self.findElement(*self.regist_btn)

    def accountTitle(self):
        '''获取个人中心标题的文案'''
        return self.findElement(*self.account_title).text

    def userName(self):
        '''获取用户名的元素'''
        return self.findElement(*self.user_name)

    def firstFunList(self):
        '''
        获取第一列功能列表的元素
        [0]存款
        [1]取款
        [2]内部转账
        [3]换汇
        '''
        return self.findElements(*self.user_tabs)

    def secondFunLeft(self):
        '''第二列功能列表左边按钮'''
        return self.findElement(*self.second_fun_left)

    def secondFunRight(self):
        '''第二列功能列表右边按钮'''
        return self.findElement(*self.second_fun_right)

    def functionList(self):
        '''
        功能列表
        [0]账户信息
        [1]资金记录
        [2]账户设置
        [3]联系客服
        '''
        return self.findElements(*self.user_card_list)