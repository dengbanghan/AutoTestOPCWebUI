# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : codec.py
# @Software: PyCharm

import base64
import urllib
import time
import os
import json
import hashlib


def md5(string):
    m = hashlib.md5()
    m.update(string.encode(encoding='utf-8'))
    return m.hexdigest()


def base64_encode(string):
    return base64.encodestring(string)

def base64_decode(encode_string):
    return base64.decodestring(encode_string)


def url_encode(url_path):
    if isinstance(url_path, str):
        url_path = url_path.encode('utf-8')
    url_data = {"url": url_path}
    length = len(list[url_data.keys()][0]) + 1
    return urllib.urlencode(url_data)[length:]

def url_decode(url_path):
    return urllib.unquote(url_path)

def imageBase(imagePath=''):
    '''
    :param imagePath: 传入时需要带上转义字符如：C:\\Users\\Public\\Pictures\\Sample Pictures\\1.png
    :return:
    '''
    imagePath = (os.path.dirname(os.path.realpath(__file__)) + "\\test.png")
    f=open(imagePath,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    fileStr = url_encode(ls_f)
    return fileStr

def get_time():
    return float(time.time() * 1000)

def isJson(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def parseJson(body):
    # body_str = str(body)
    # body_str = body_str.replace("u'","'")
    # body_str = body_str.replace("\'","\"")
    # body_str = body_str.replace(" ","")
    # 将boolean值转换
    dic = eval(str(body))
    if dic.has_key("enable"):
        if dic["enable"] == 1 or dic["enable"] == '1':
            dic["enable"] = 'true'
        else:
            dic["enable"] = 'false'

    # if dic.has_key("tradable"):
    #     if dic["tradable"] == 1 or dic["tradable"] == '1':
    #         dic["tradable"] = 'true'
    #     else:
    #         dic["tradable"] = 'false'

    if dic.has_key("close_only"):
        if dic["close_only"] == 1 or dic["close_only"] == '1':
            dic["close_only"] = 'true'
        else:
            dic["close_only"] = 'false'

    dic_final = {}
    for (k, v) in dic.items():
        # print "k:", k
        # print "v:", v
        k_str = str(k).replace("u'", "'", 1)
        v_str = str(v).replace("u'", "'", 1)
        dic_final[k_str] = v_str

    body_str = str(dic_final)
    body_str = body_str.replace("\'", "\"")
    body_str = body_str.replace(" ", "")
    body_str = body_str.replace("\"true\"", "true")
    body_str = body_str.replace("\"false\"", "false")
    print("parseBody:" + body_str)
    return body_str

if '__main__' == __name__:
    pass