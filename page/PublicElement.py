# -*- coding: utf-8 -*-
# @Time    : 2020/6/17
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : PublicElement.py
# @Software: PyCharm

from base.basePage import *
from selenium.webdriver.common.by import By

class PublicElement(WebDriver):
    '''页面公用的元素和操作'''
    # 用例失败文案
    error_msg = "用例执行失败：{}"
    # 时间输入框
    calendar_input = (By.CLASS_NAME, 'ant-calendar-input')
    # 输入框的元素
    input_box = (By.CLASS_NAME, 'ant-input')
    # 下拉框按钮的元素
    select_box = (By.CLASS_NAME, 'ant-select-arrow')
    # 输入框标题
    input_title = (By.CLASS_NAME, 'ant-form-item-label')
    # 查询、重置等按钮
    button = (By.CLASS_NAME, 'ant-btn')
    # 列表字段
    table_column = (By.CLASS_NAME, 'ant-table-column-title')
    # 列表数据
    table_tbody = (By.CLASS_NAME, 'ant-table-tbody')
    # toast弹窗文案
    toast_text = (By.CLASS_NAME, 'md-toast-text')
    # 页面提示文案
    text = (By.CLASS_NAME, 'text')
    # 输入框下方的提示文案的元素
    input_box_msg = (By.CLASS_NAME, 'md-input-item-msg')
    # 页面右上角按钮的元素
    right_btn = (By.CLASS_NAME, 'right-title')
    # 页面左上角按钮的元素
    left_btn = (By.CLASS_NAME, 'svg-icon')
    # 顶部提示语
    top_tip = (By.CLASS_NAME, 'tip')
    # 二级功能菜单卡片
    function_card = (By.CLASS_NAME, 'account-card-list')
    # 弹窗按钮的元素
    dialog_btn = (By.CLASS_NAME, 'md-dialog-btn')
    # 弹窗标题
    dialog_title = (By.CLASS_NAME, 'md-dialog-title')

    def getTableDatas(self, table):
        '''获取页面列表中的数据'''
        pax = []
        # 通过标签名获取表格的所有行
        table_tr_list = table.find_elements_by_tag_name("tr")

        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        for tr in table_tr_list:

            att = (tr.text).split("  ")
            pax.append(att)

        return pax

    def getLists(self,pax):
        att = []
        # 循环列表中的元素列表
        for i in range(len(pax)):
            # 获取每个元素列表中的第一个元素
            ta = pax[i][0]
            att.append(ta)

        return att

    def titleText(self):
        '''返回标题的文案'''
        return self.findElement(*self.title_text).text

    def inputBox(self):
        '''将输入框的元素放入到标题中'''
        return self.findElements(*self.input_box)

    def selectBox(self):
        '''将下拉框的元素放入到标题中'''
        return self.findElements(*self.select_box)

    def inputBoxTitle(self):
        '''将输入框标题的元素放到列表中'''
        return self.findElements(*self.input_title)

    def toastText(self):
        '''返回 toast 弹窗的文案'''
        return self.findElement(*self.toast_text).text

    def Button(self):
        '''登录、提交申请等按钮的元素'''
        return self.findElements(*self.button)

    def Text(self):
        '''页面提示文案'''
        return self.findElement(*self.text).text

    def inputBoxMsg(self):
        '''
        返回输入框下方的提示文案的元素
        [0]手机号码输入框下方提示文案
        [1]密码输入框下方提示文案
        [2]验证码输入框下方提示文案
        '''
        return self.findElements(*self.input_box_msg)

    def rightBtn(self):
        '''返回页面右上角按钮的元素'''
        return self.findElement(*self.right_btn)

    def leftBtn(self):
        '''返回页面右上角按钮的元素'''
        return self.findElement(*self.left_btn)

    def topTip(self):
        '''返回页面顶部提示的元素'''
        return self.findElement(*self.top_tip)

    def functionCards(self):
        '''返回二级功能菜单卡片的元素列表'''
        return self.findElements(*self.function_card)

    def dialogBtn(self):
        '''弹窗的按钮，如：取消、同意并继续等按钮'''
        return self.findElements(*self.dialog_btn)

    def dialogTitle(self):
        '''弹窗的标题文案'''
        return self.findElements(*self.dialog_title).text