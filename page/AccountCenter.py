# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 1:47
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : AccountCenter.py
# @Software: PyCharm

from page.Login import *

class AccountCenter(Login):
    '''个人中心首页的元素和操作'''
    # 标题
    account_title = (By.CLASS_NAME, 'title')
    # 用户头像
    user_icon = (By.CLASS_NAME,'img')
    # 用户名
    user_name = (By.CLASS_NAME, 'username')
    # 第一列功能列表
    user_tabs = (By.CLASS_NAME, 'tabs-name')
    # 第二列功能列表左边按钮
    second_fun_left = (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[1]/div[2]/span[1]')
    # 第二列功能列表右边按钮
    second_fun_right = (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2]/span[1]')
    # 功能列表的所有元素
    user_card_list = (By.CLASS_NAME, 'user-card-list')
    # 登录按钮
    login_btn = (By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div')
    # 注册按钮
    regist_btn = (By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div')
    # 提醒登录弹窗的元素，分别是：标题、提示语、左边按钮、右边按钮、打叉按钮
    login_tip_title = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div/h2')
    login_tip_text = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div')
    login_tip_btn_left = (By.XPATH,'/html/body/div[2]/div/div[2]/div/footer/a[1]')
    login_tip_btn_right = (By.XPATH,'/html/body/div[2]/div/div[2]/div/footer/a[2]')
    login_tip_btn_close = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div/a')
    # 联系客服弹窗
    customer_dialog = (By.XPATH,'/html/body/div[4]/div/div[2]/div')
    # 联系客服的我知道了按钮
    i_know_btn = (By.XPATH,'/html/body/div[3]/div/div[2]/div/footer/a')

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