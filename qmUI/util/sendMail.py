import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1916291530@qq.com'
my_pass = 'wfdenebagyofchdh'
her_receive = 'ex1916291530@163.com'

try:
    msg = MIMEText('内容','plain','utf-8')
    msg['From'] = formataddr("萧萧",my_sender)
    msg['To'] = formataddr("eva",her_receive)
    msg['Subject'] = '标题'

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(my_sender, my_pass)
    server.sendmail(my_sender,[her_receive,],msg.as_string())
    server.quit()
except:
    print("发送失败")


# #!/usr/bin/python3
#
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# my_sender = '1916291530@qq.com'  # 发件人邮箱账号
# my_pass = 'wfdenebagyofchdh'  # 发件人邮箱密码
# my_user = 'ex1916291530@163.com'  # 收件人邮箱账号，我这边发送给自己
#
#
# def mail():
#     ret = True
#     try:
#         msg = MIMEText('这是内容呢', 'plain', 'utf-8')
#         # msg['From'] = formataddr(["萧萧", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = formataddr(["肖莹", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "测试标题"  # 邮件的主题，也可以说是标题
#
#         # QQ 邮箱 SMTP 服务器地址：smtp.qq.com，ssl 端口：465。
#         server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret = False
#     return ret
#
#
# ret = mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")