# -*- coding: utf-8 -*-
# @Time    : 2020/6/11
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : getToken.py
# @Software: PyCharm

import sys
import os

# 当前文件夹的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)
sys.path.append(basedir)
# 父目录
sys.path.append("..")
# 父目录下的某个文件夹
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))  + "/base")

from tools.logger import Logger
import tools.config
from base.utils import Library
from base.getSmsCode import getCode


class GetToken():
    def __init__(self):
        self.u = Library()
        self.log = Logger("debug")
        self.login_info = tools.config.config('loginInfo.ini', 'login')
        self.DomainNnameL = self.login_info['host_web'].lstrip('https://')
        self.DomainNname = self.DomainNnameL.rstrip(':1443/')
        self.api_send = 'sign/sms/send'
        self.api_login = 'sign/login'
        pass

    def send_code(self,PhoneNum,AreaNum):
        '''发送短信验证码'''
        host = self.login_info['host_api'] + self.api_send

        request_data = {'phone':PhoneNum,'area':AreaNum,'host':self.DomainNname}
        json_request_data=self.u.jsonDumps(request_data)

        HEADER = {
            "Content-Type": "application/json; charset=UTF-8",
            # "Authorization": "{}".format("Basic dGVzdGFwcDI6YWJjZA==")
        }

        self.log.info("Request Url：\n{}".format(host))
        self.log.info("Request Body：\n{}".format(json_request_data))
        self.log.info("Request Header：\n{}".format(self.u.jsonDumps(HEADER)))

        try:
            res = self.u.http_post(host, json_request_data, HEADER)

        finally:
            if res[0] == 200:
                msg = self.u.jsonDumps(res)
                self.log.info("发送验证码成功：\n{}".format(msg))
            else:
                msg = self.u.jsonDumps(res)
                self.log.error("发送验证码失败：\n{}".format(msg))


    def get_token(self,PhoneNum,AreaNum,SmsCode=None):
        ''''接口登录 OPC 并获取 token '''
        host = self.login_info['host_api'] + self.api_login

        if SmsCode == None:
            SmsCode = self.login_info['default_code']
        else:
            self.send_code(PhoneNum,AreaNum)


        request_data = {'phone': PhoneNum, 'area': AreaNum, 'sms':SmsCode,'host': self.DomainNname}
        json_request_data = self.u.jsonDumps(request_data)

        HEADER = {
            "Content-Type": "application/json; charset=UTF-8",
            # "Authorization": "{}".format("Basic dGVzdGFwcDI6YWJjZA==")
        }

        self.log.info("Request Url：\n{}".format(host))
        self.log.info("Request Body：\n{}".format(json_request_data))
        self.log.info("Request Header：\n{}".format(self.u.jsonDumps(HEADER)))

        try:
            res = self.u.http_post(host, json_request_data, HEADER)
            dict_res = res[1]
            data = self.u.searchDicKV(dict_res, "data")
            token = self.u.searchDicKV(data, "token")

            if token == None:
                return self.login_info['default_token']
            else:
                return token

        finally:
            if res[0] == 200:
                msg = self.u.jsonDumps(res)
                self.log.info("获取 [token] 成功：\n{}".format(token))
            else:
                msg = self.u.jsonDumps(res)
                self.log.error("获取 [token] 失败：\n{}".format(msg))

if __name__ == '__main__':
    gt = GetToken()
    gt.get_token('17722527464','+86')