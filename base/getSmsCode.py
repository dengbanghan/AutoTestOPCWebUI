# -*- coding: utf-8 -*-
# @Time    : 2020/6/5
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : getSmsCode.py
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
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")) + "/base")

import tools.config
from tools.py3_mysql import DBReader
from base.utils import Library
from tools.logger import Logger

class getCode():
    def getCode(self,phoneNum):
        db = DBReader()
        u = Library()
        log = Logger("debug")
        eddid = tools.config.config('mySqlInfo.ini', 'eddid')
        databases = tools.config.config('mySqlInfo.ini', 'database')
        host = eddid['host']
        port = int(eddid['port'])
        user = eddid['user']
        password = eddid['passwd']
        database = databases['message_push']

        db.loadDBConfig(host,port,user,password,database)
        selectCodeSql = 'SELECT t.metadata FROM {}.push_message t WHERE t.receiver LIKE "%{}%" ORDER BY last_modified_date DESC LIMIT 1;'.format(database,phoneNum)
        db_res = db.getSQL(sql=selectCodeSql,type='one')
        metadata = u.searchDicKV(db_res, "metadata")
        dict_metadata = u.jsonLoads(metadata)
        templateParam = u.searchDicKV(dict_metadata, "templateParam")
        smsCode = u.searchDicKV(templateParam, "sms_auth_code")
        log.info("查询的手机号：{},获取的验证码：{}".format(phoneNum, smsCode))
        return smsCode


if __name__ == '__main__':
    gc = getCode()
    gc.getCode('17722527464')
