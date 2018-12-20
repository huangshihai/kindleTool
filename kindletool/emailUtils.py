# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pypinyin import pinyin, Style
import re
from .config import mail_host, mail_user, mail_pass, sender, book_path

pwd_path = os.path.abspath(os.path.dirname(__file__))


def __get_pinyin__(filename):
    name_pinyins = pinyin(filename, style=Style.NORMAL)
    name_pinyin = ''
    for np in name_pinyins:
        name_pinyin += ''.join(np) + '_'
    name_pinyin = name_pinyin[:-1]
    name_pinyin = re.sub('[^a-zA-Z0-9_.]', '', name_pinyin)
    return name_pinyin


def push_book(receivers, filename):
    send_email(receivers, filename, filename, filename)


def send_email(receivers, subject, content, filename=None):
    message = MIMEMultipart()
    att1 = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message.attach(att1)
    if filename != None:
        att2 = MIMEText(open(os.path.join(book_path, filename), 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename=%s' % __get_pinyin__(filename)
        message.attach(att2)
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = subject
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        smtpObj.quit()
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
