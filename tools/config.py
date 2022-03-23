# -*- coding: utf-8 -*-
# @Time    : 2022/3/10
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : config.py
# @Software: PyCharm

import configparser


def config(filename,items):
    file = rf'../conf/{filename}'

    con = configparser.ConfigParser()
    con.read(file, encoding='utf-8')

    items = con.items(rf'{items}')

    return dict(items)