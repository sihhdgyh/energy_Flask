import smtplib
import random

import email.utils
from email.mime.text import MIMEText

def sendSMS(mail):
    content=''
    i = 0
    while (i < 6):
        i += 1
        content = content+str(random.randint(0, 9))

    print(content)
    message = MIMEText(content)
    # message['To'] = email.utils.formataddr(('接收者显示的姓名', 'liyuanjinglyj@163.com'))
    message['From'] = email.utils.formataddr(('韶音', '2083978036@qq.com'))
    message['Subject'] = '验证码'
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login('2083978036@qq.com', 'eajqygodkpjnbcdd')
    server.set_debuglevel(True)
    try:
        server.sendmail('2083978036@qq.com', [mail], msg=message.as_string())
    finally:
        server.quit()

    return content
