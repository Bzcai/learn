# /Library/Frameworks/Python.framework/Versions/3.5/bin
# -*- coding: UTF-8 -*-
import time
import smtplib
from email.mime.text import MIMEText
import re
import requests



server = smtplib.SMTP_SSL('smtp.qq.com',port=465)
username = 'caiyan730@qq.com'
password = 'pdyndmebywskbgid'
fromaddr = 'caiyan730@qq.com'
toaddr = 'caiyan@chunbo.com'


def getip():
    '''send ip from mynas'''
    try:
        result = requests.get("http://ddns.oray.com/checkip")
        ip = re.search('\d+\.\d+\.\d+\.\d+', result.text).group(0)
    except:
        print('获取ip失败')
        pass
    return ip
# 如果是其他的服务，只需要更改 host 为对应地址，port 对对应端口即可
# server = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
# server.set_debuglevel(1)    # 开启调试，会打印调试信息
#print("--- Need Authentication ---")
def sendip():
    '''get my nas's new ip addr and send it to my email address'''
    oldip = '176.126.72.52'
    while True:
        ip = getip()
        if oldip == ip:
            pass
        else:
            msg = MIMEText('your Nas ip is:{0}'.format(ip), 'plain', 'utf-8')
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = 'Your NAS\'s ip is changed'
            # print(msg.as_string())
            try:
                server.login(username, password)
                server.sendmail(fromaddr, toaddr, msg.as_string())
                print(msg)
            except:
                print('send failed')
            server.quit()
            oldip = ip
    time.sleep(600)



if __name__ == '__main__':
    sendip()
