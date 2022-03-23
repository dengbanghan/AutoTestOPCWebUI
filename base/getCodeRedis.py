# -*- coding: utf-8 -*-
# @Time    : 2022/3/10
# @Author  : Administrator
# @Email   : dengbanghan@gmail.com
# @File    : getCodeRedis.py
# @Software: PyCharm



import json
import redis
# from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

import tools.config

class getCode():
    # server = Server("F:\AutoTest\AutoTestWebUI\\base\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
    # server.start()
    # proxy = server.create_proxy()

    chrome_driver = r"D:\Program Files\Anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
    chrome_options = Options()
    # chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
    # 要访问的地址
    base_url = "https://eddid-auth-center-uat.eddid.com.cn:1443/login.html"
    # proxy.new_har("ht_list2", options={'captureContent': True})
    driver.maximize_window()
    driver.get(base_url)

    def getId(self):
        # result = self.proxy.har
        for entry in result['log']['entries']:
            _url = entry['request']['url']
            # 根据URL找到数据接口,这里要找的是 http://git.liuyanlin.cn/get_ht_list 这个接口
            if "https://eddid-auth-center-uat.eddid.com.cn:1443/v2/captcha" in _url:
                _response = entry['response']
                _content = _response['content']
                _text = json.loads(_content['text'])
                return _text['data']['id']
        server.stop()

    def getCode(self):
        redisServer = tools.config.config('redisInfo.ini', 'auth')
        print(redisServer)
        redis_host = redisServer['redis_host']
        redis_port = redisServer['redis_port']
        redis_passwd = redisServer['redis_passwd']
        db = redisServer['db']
        # redis_host = 'r-wz9af3qz5xen9mi4j8pd.redis.rds.aliyuncs.com'
        # redis_port = '6379'
        # redis_passwd = 'admin@321'
        # db = 1
        r = redis.Redis(host=redis_host, port=redis_port, password=redis_passwd,db=db,decode_responses=True)
        gc = getCode()
        return r.get("{eac}:captcha:"+gc.getId())

if __name__ == '__main__':
    gc = getCode()
    print(gc.getCode())