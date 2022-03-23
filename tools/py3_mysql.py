# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : py3_mysql.py
# @Software: PyCharm

import pymysql
from tools.logger import Logger

class DBReader(object):
    def __new__(cls):
        # 单例模式
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBReader, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.log = Logger("debug")
        pass

    def loadDBConfig(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.log.info("sql load config:\nhost:{}\nport:{}\nuser:{}\npassword:{}\ndatabase:{}".format(self.host,self.port,self.user,self.password,self.db))

    def getSQL(self, sql, type):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, db=self.db,
                                    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.log.info("SQL语句:{}".format(sql))
        try:
            with self.conn.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                if type == 'all':
                    result = cursor.fetchall()
                else:
                    result = cursor.fetchone()
                    # print "sql result:", result
                    # result_str=str(result).strip(")")
                    # result_str = str(result_str).strip("(")
                    # result_str = str(result_str).replace("u'","")
                    # result_str = str(result_str).replace("'", "")
                    # result_str = str(result_str).replace(" ", "")
                    # result_str = str(result_str).replace(",", "")
                if len(result) <= 0:
                    self.log.info("sql data is not exist.")
                    result = ""
                return result
        except Exception as e:
            self.log.error("sql exec error: {}".format(e))
        # finally:
        #     self.conn.close()

    def getSQLDic(self, sql):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, db=self.db,
                                    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.log.info("SQL语句:{}".format(sql))
        try:
            with self.conn.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchone()
                print("sql result:", result)
                result_str = str(result).strip(")")
                result_str = str(result_str).strip("(")
                return eval(result_str)
        except Exception as e:
            self.log.error("sql exec error: {}".format(e))
        finally:
            self.conn.close()

    def getSQLCheck(self, sql):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, db=self.db, charset='utf8mb4')
        self.log.info("SQL语句:{}".format(sql))
        try:
            with self.conn.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchone()
                self.log.info("sql result:", result)
                result_str = str(result).strip(")")
                result_str = str(result_str).strip("(")
                result_list = result_str.split(",")
                result_final = []
                for i in range(0, len(result_list)):
                    result_str = result_list[i].replace("u'", "", 1)
                    result_str = str(result_str).replace("'", "")
                    result_str = str(result_str).replace(" ", "")
                    result_final.append(result_str)
                self.log.info("final result:".format(result_final))
                return result_final
        except Exception as e:
            self.log.error("sql exec error: {}".format(e))
        finally:
            self.conn.close()

    def getSQLCheckUnicode(self, sql):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, db=self.db, charset='utf8mb4')
        self.log.info("SQL语句:", sql)
        try:
            with self.conn.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchone()
                self.log.info("sql result:".format(result))
                self.conn.close()
                return result
        except Exception as e:
            self.log.error("sql exec error: {}".format(e))
            self.conn.close()

    def execSQL(self, sql):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, db=self.db,
                                    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.log.info("SQL语句:".format(sql))
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()
                self.conn.close()
                return True
        except Exception as e:
            self.log.error("sql exec error: {}".format(e))
            self.conn.close()
            return False
        finally:
            self.conn.close()

    # 获取数据库多条数据
    def getSqlMutilLine(self, sql):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, db=self.db, charset='utf8mb4')
        self.log.info("SQL语句:", sql)
        resList = []
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                for line in result:
                    line_str = str(line).strip(")")
                    line_str = str(line_str).strip("(")
                    line_list = line_str.split(",")
                    line_final = []
                    for i in range(0, len(line_list)):
                        line_str = line_list[i].replace("u'", "", 1)
                        line_str = str(line_str).replace("'", "")
                        line_str = str(line_str).replace(" ", "")
                        if str(line_str)[:len(line_str) - 1].lstrip('-').isdigit():
                            line_str = str(line_str).replace("L", "")
                        line_final.append(line_str)
                    resList.append(line_final)
                self.conn.close()
                return resList
        except Exception as e:
            self.log.error("sql exec error: {}".format(e))
            self.conn.close()

    # 获取数据库多条数据,每条数据只有一个值，则返回组合后的列表
    def getSqlMutilLineOfSingleValue(self, sql):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        password=self.password, db=self.db, charset='utf8mb4')
        self.log.info("SQL语句:", sql)
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                line_final = []
                for line in result:
                    line_str = str(line).strip(")")
                    line_str = str(line_str).strip("(")
                    line_list = line_str.split(",")
                    for i in range(0, len(line_list) - 1):
                        line_str = line_list[i].replace("u'", "", 1)
                        line_str = str(line_str).replace("'", "")
                        line_str = str(line_str).replace(" ", "")
                        if str(line_str)[:len(line_str) - 1].lstrip('-').isdigit():
                            line_str = str(line_str).replace("L", "")
                        line_final.append(line_str)
                self.conn.close()
                return line_final
        except Exception as e:
            self.log.error("sql exec error: {}".format(e))
            self.conn.close()