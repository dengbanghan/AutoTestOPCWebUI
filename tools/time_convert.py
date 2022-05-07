# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 11:11
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : time_convert.py
# @Software: PyCharm

import time
import pytz
import datetime

class TimeConvert():

    # 返回 东八 时间戳
    def get_shanghai_timestamp(self, date_time):
        time_zone = pytz.timezone('Asia/Shanghai')
        timeArray = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        local_dt = timeArray.astimezone(time_zone)
        return int(time.mktime(local_dt.timetuple()))

    # 返回 UTC 时间戳
    def get_utc_timestamp(self, utc_time_str, utc_format=r'%Y-%m-%d %H:%M:%S'):
        local_tz = pytz.timezone('UTC')
        utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
        local_dt = utc_dt.astimezone(local_tz)
        return int(time.mktime(local_dt.timetuple()))

    # 返回东八格式化时间
    # 方式一：
    def get_local_format_time(self, timestamp):
        local_time = time.localtime()
        format_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        return format_time

    # 方式二：
    def local_to_utc(self, local_ts, time_format=r"%Y-%m-%d %H:%M:%S"):
        time_zone = pytz.timezone('Asia/Shanghai')
        time_str = time.strftime(time_format, time.localtime(local_ts))
        dt = datetime.datetime.strptime(time_str, time_format)
        utc_dt = dt.astimezone(time_zone)
        return utc_dt.strftime(time_format)

    # 返回 UTC 格式化时间
    def get_utc_format_time(self, local_ts, time_format=r"%Y-%m-%d %H:%M:%S"):
        time_str = time.strftime(time_format, time.localtime(local_ts))
        dt = datetime.datetime.strptime(time_str, time_format)
        utc_dt = dt.astimezone(pytz.utc)
        return utc_dt.strftime(time_format)


if __name__ == '__main__':
    tc = TimeConvert()
    print(tc.get_shanghai_timestamp('2022-05-07 14:12:48'))
    print(tc.get_utc_timestamp("2022-05-07 14:12:48"))
    print(tc.get_local_format_time(1651903891))
    print(tc.local_to_utc(1651903891))
    print(tc.get_utc_format_time(1651903891))
    print(datetime.datetime.now())