import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pypinyin import pinyin, Style
import re

pwd_path = os.path.abspath(os.path.dirname(__file__))


class EmailUtil():
    def __init__(self, file_path, mail_host='', mail_user='', mail_pass='', sender=''):
        self.file_path = os.path.join(pwd_path, file_path)
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender

    def get_pinyin(self, filename):
        name_pinyins = pinyin(filename, style=Style.NORMAL)
        name_pinyin = ''
        for np in name_pinyins:
            name_pinyin += ''.join(np) + '_'
        name_pinyin = name_pinyin[:-1]
        name_pinyin = re.sub('[^a-zA-Z0-9_.]', '', name_pinyin)
        return name_pinyin

    def send_email(self, receivers, subject, content, filename=None):
        message = MIMEMultipart()
        att1 = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message.attach(att1)
        if filename != None:
            att2 = MIMEText(open(os.path.join(self.file_path, filename), 'rb').read(), 'base64', 'utf-8')
            att2["Content-Type"] = 'application/octet-stream'
            att2["Content-Disposition"] = 'attachment; filename=%s' % self.get_pinyin(filename)
            message.attach(att2) 
        message['From'] = "{}".format(self.sender)
        message['To'] = ",".join(receivers)
        message['Subject'] = subject
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证
            smtpObj.sendmail(self.sender, receivers, message.as_string())  # 发送
            smtpObj.quit()
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)


if __name__ == '__main__':
    mail_host = "smtp.163.com"  # SMTP服务器
    # mail_user = "13600048767@163.com"  # 用户名
    # mail_pass = "1995911LQFZB"  # 授权密码，非登录密码
    # sender = '13600048767@163.com'  # 发件人邮箱(最好写全, 不然会失败)
    mail_user = "h_shihai@163.com"  # 用户名
    mail_pass = "Hsh960405"  # 授权密码，非登录密码
    sender = 'h_shihai@163.com'  # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['13600048767@kindle.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    emailUtil = EmailUtil('data\\', mail_host, mail_user, mail_pass, sender)
    emailUtil.send_email(receivers, "当尼采哭泣 欧文·亚隆系列", '当尼采哭泣 欧文·亚隆系列', '当尼采哭泣(欧文_亚隆系列).mobi')
