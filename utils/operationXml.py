# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:41
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : operationXml.py
# @Software: PyCharm

import os
import xml.dom.minidom

class OperationXml(object):
    def dir_base(self,fileName,filePath='data'):
        '''
        获取 data 文件夹下的文件
        ：param fileName:要读的文件名称
        ：param filePath:要读的文件名对应的文件夹
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filePath,fileName)

    def getXmlData(self,value):
        '''
		获取xm1单节点中的数据
	    ：param value:xml 文件中单节点的名称
		'''
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        return nameValue.firstChild.data

    def getXmlUser(self,parent,child):
        '''
		获取xml子节点中的数据
		：param parent：xml文件中父节点的名称
		：param child:xml 文件中子节点的名称
		'''
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        item = itemlist[0]
        return item.getAttribute(child)