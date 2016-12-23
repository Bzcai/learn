# /Library/Frameworks/Python.framework/Versions/3.5/bin
# -*- coding: UTF-8 -*- #
import re
import time
import requests


def getip():
    '''send ip from mynas'''
    try:
        result = requests.get("http://ddns.oray.com/checkip")
        ip = re.search('\d+\.\d+\.\d+\.\d+', result.text).group(0)
    except:
        print('获取ip失败')
        pass
    return ip

if __name__ == '__main__':
    getip()
