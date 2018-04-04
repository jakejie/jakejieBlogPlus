# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:JakeBlog
FileName = PyCharm
Version:1.0
CreateDay:2018/3/23 16:38
"""
from random import Random
from django.core.mail import send_mail
from JakeBlog.settings import EMAIL_FROM
from users.models import EmailVerifyRecord


# 注册用户/找回密码 发送验证邮件
def sent_register_email(email, sent_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.sent_type = sent_type
    email_record.save()
    # 发送邮件
    email_title = ""
    email_body = ""

    if sent_type == "register":
        email_title = "注册用户在线激活链接"
        email_body = "点击以下链接激活你的账号：http://127.0.0.1:8000/activate/{}".format(code)
        # 主题 内容 发件人 收件人(列表)
        sent_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if sent_status:
            pass
        pass
    elif sent_type == "forget":
        email_title = "密码重置链接"
        email_body = "点击以下链接重置你的密码：http://127.0.0.1:8000/resetpwd/{}".format(code)
        # 主题 内容 发件人 收件人(列表)
        sent_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if sent_status:
            pass
    else:
        pass


# 生成随机字符串
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
