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