# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : httpclient.py
# @Software: PyCharm

from requests.cookies import RequestsCookieJar
from base.codec import *
import requests
import urllib3
import json

class HttpClient(object):
    # 解决请求的时候添加 verify=False 时的报错
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    def __init__(self):
        self.cookies = RequestsCookieJar()
        self.access_token = ""
        self.verify = False

    def get(self, url, header=None, param=None):
        res = None
        if header is not None:
            res = requests.get(url=url, headers=header, verify=self.verify, params=param)
        else:
            res = requests.get(url=url, verify=self.verify, params=param)

        if isJson(res.text):
            return [res.status_code, json.loads(res.text)]
        else:
            return [res.status_code, res.text]

    def post(self, url, data=None, header=None):
        res = None
        if header is not None:
            if  'application/json' == header['Content-Type']:
                if type(data) == 'list':
                    pass
                else:
                    data = json.dumps(data)
            res = requests.post(url=url, data=data, headers=header, verify=self.verify)
        else:
            res = requests.post(url=url, data=data, verify=self.verify)

        if isJson(res.text):
            return [res.status_code, json.loads(res.text)]

        else:
            return [res.status_code, res.text]

    def delete(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.delete(url=url, data=data, headers=header)
        else:
            res = requests.delete(url=url, data=data)

        if isJson(res.text):
            return [res.status_code, json.loads(res.text)]
        else:
            return [res.status_code, res.text]

if '__main__' == __name__:
    http = HttpClient()
    pass