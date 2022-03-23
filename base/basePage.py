# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:32
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : basePage.py
# @Software: PyCharm

from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class WebDriver(object):
    def __init__(self,driver):
        self.driver=driver

    def findElement(self,*loc):
        '''单个定位元素的方法'''
        try:
            return WebDriverWait(self.driver,15).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findElements(self,*loc):
        '''多个定位元素的方法'''
        try:
            return WebDriverWait(self.driver,15).until(lambda x:x.find_elements(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def isElementExist(self,*loc):
        '''判断元素是否存在，存在返回True，否则返回False'''
        try:
            self.findElement(*loc)
            return True
        except:
            return False

    def hover(self, element):
        '''鼠标悬停'''
        ActionChains(self.driver).move_to_element(element).perform()
