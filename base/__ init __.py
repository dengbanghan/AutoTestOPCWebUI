# -*- coding: utf-8 -*-
# @Time    : 2022/3/10
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : __ init __.py
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