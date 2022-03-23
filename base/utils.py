# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : utils.py
# @Software: PyCharm

import random
import string
import sys
import os
# 当前文件夹的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)
sys.path.append(basedir)
# 父目录
sys.path.append("..")
# 父目录下的某个文件夹
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")) + "/base")
from tools.py3_mysql import DBReader
from tools.httpclient import HttpClient
from .codec import *
import re


class Library(object):
    def __init__(self):
        self.res = ''
        self.db = DBReader()
        self.http = HttpClient()
        pass

    def searchDicKV(self, dic, keyword):
        if isinstance(dic, dict):
            for x in range(len(dic)):
                temp_key = list(dic.keys())[x]
                temp_value = dic[temp_key]
                if temp_key == keyword:
                    return_value = temp_value
                    return return_value
                return_value = self.searchDicKV(temp_value, keyword)
                if return_value != None:
                    return return_value

    def getListIndexValue(self, mylist, index):
        if isinstance(mylist, list):
            if len(mylist)==0:
                return 0
            else:
                return mylist[int(index)]

    def getListValue(self,list, string, key):
        '''指定数组中包含的字符串,返回数组中key的value'''
        list_len = len(list)
        for i in range(list_len):
            data = list[i]
            data_str = str(data)
            if string in data_str:
                return data[key]

    def randomPhone(self, prefix=None, size=8, chars="123456789"):
        operator = ['139','138','137','136','135','134','159','158','157','150','151','152','147','188','187','182','183','184','178','130','131','132','156','155','186','185','145','176','133','153','189','180','181','177','173']
        phone_operator = ''.join(random.choice(operator))
        phone = ''.join(random.choice(chars) for _ in range(int(size)))
        if prefix == None:
            return phone_operator + phone
        else:
            return str(prefix) + phone_operator + phone

    def randomName(self, prefix=None, size=6, chars=None, sign=None):
        if sign == None:
            chars = string.ascii_letters + string.digits
        elif sign == 'lower':
            chars = string.ascii_lowercase + string.digits
        elif sign == 'upper':
            chars = string.ascii_uppercase + string.digits

        name = ''.join(random.choice(chars) for _ in range(int(size)))
        if prefix == None:
            return name
        else:
            return str(prefix) + name

    def randomLetter(self, prefix=None, size=6, chars=string.ascii_letters):
        name = ''.join(random.choice(chars) for _ in range(int(size)))
        if prefix == None:
            return name
        else:
            return str(prefix) + name

    def randomBigLetter(self, prefix=None, size=6, chars=string.ascii_uppercase):
        name = ''.join(random.choice(chars) for _ in range(int(size)))
        if prefix == None:
            return name
        else:
            return str(prefix) + name

    def randomSmallLetter(self, prefix=None, size=6, chars=string.ascii_lowercase):
        name = ''.join(random.choice(chars) for _ in range(int(size)))
        if prefix == None:
            return name
        else:
            return str(prefix) + name

    def getCurrentTimeStamp(self):
        return int(time.time())

    def http_get(self, url, data=None, header=None):
        return self.http.get(url, data, header)

    def http_post(self, url, data=None, header=None):
        return self.http.post(url, data, header)

    def http_delete(self, url, data=None, header=None):
        return self.http.delete(url, data, header)

    def parseJson(self, body):
        return parseJson(body)

    def jsonDumps(self, content):
        '''用于将 Python 对象编码成 JSON 字符串'''
        return json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

    def jsonLoads(self,content):
        '''用于解码 JSON 数据。该函数返回 Python 字段的数据类型'''
        return json.loads(content)

    def loadDBConfig(self, host, port, user, password, db):
        self.db.loadDBConfig(host, int(port), user, password, db)

    def getSQL(self, sql,type='one'):
        return self.db.getSQL(sql,type)

    def checkSql(self, sql):
        dic_str = ""
        list = self.db.getSQLCheck(str(sql))
        for x in range(len(list)):
            if list[x] != "":
                temp_value = list[x]
                dic_str = dic_str + str(temp_value) + "|"
        return dic_str

    def checkSqlUnicode(self, sql):
        dic_str = ""
        list = self.db.getSQLCheckUnicode(str(sql))
        for x in range(len(list)):
            if list[x] != "":
                temp_value = list[x]
                dic_str = dic_str + str(temp_value) + "|"
        return dic_str

    def getSqlMutilLine(self, sql):
        return self.db.getSqlMutilLine(sql)

    def getSqlMutilLineOfSingleValue(self, sql):
        return self.db.getSqlMutilLineOfSingleValue(sql)

    def execSQL(self, sql):
        if self.db.execSQL(sql):
            print('SQL execute successfully!')

    def md5(self, message):
        return md5(message)

    def re_find(self, r, origin_str):
        return re.findall(r, origin_str)

    def getSmsCode(self, data, data_field={}):
        '''
        从 MongoDB 中获取短信验证码
        取到数据后根据 id 进行倒序排列
        然后取最上面的一条数据，就是最新的验证码了
        入参：集合，键值对
        '''
        data = self.mongodb.find_many(data, data_field).sort([('_id',-1)]).limit(1)
        for res in data:
            return self.searchDicKV(res,'sms_auth_code')


if '__main__' == __name__:
    pass
