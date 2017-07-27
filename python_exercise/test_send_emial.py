'SMTP协议发送邮件'

from email.mime.text import MIMEText  # 文本邮件
from email.mime.multipart import MIMEMultipart, MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
# 发送邮件
import smtplib


def sendEmailOne():
    message = MIMEText('Hi,Man!\r send by Leland……', 'plain', 'utf-8')

    # 输入Emial地址和密码
    from_addr = input('From:')
    password = input('Password:')
    # 输入收件人地址
    to_addr = input('To:')
    # 输入SMTP服务器地址
    smtp_server = input('SMTP server:')

    # 设置服务器地址和端口号
    server = smtplib.SMTP(smtp_server, 25)
    # 设置调试等级
    server.set_debuglevel(1)
    # 登录
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, [to_addr], message.as_string())
    # 关闭服务器
    server.quit()


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendEmailTwo():
    # from_addr = input('From:')
    # password = input('Password:')
    # to_addr = input('To:')
    # smtp_server = input('SMTP server:')
    from_addr = '985892962@qq.com'
    password = 'ACDreamer'
    to_addr = 'Cql_liliang@163.com'
    smtp_server = 'smtp.qq.com'
    message = MIMEMultipart()
    message.attach(MIMEText('hello , send by Python...', 'plain', 'utf-8'))
    message['From'] = format_addr('Python爱好者 <%s>' % format_addr)
    message['To'] = format_addr('管理员 <%s>' % to_addr)
    message['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    # 添加附件
    with open('test_zippng.png', 'rb') as f:
        # 设置附件的MIME和文件名
        mime = MIMEBase('image', 'png', filename='test_zippng.png')
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment',
                        filename='test_zippng.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment_Id', '0')
        # 把附件的内容读进来
        mime.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mime)
        # 添加到MIMeMultipart
        message.attach(mime)
    try:
        server = smtplib.SMTP(smtp_server, 465)
        server.starttls()
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], message.as_string())
        server.quit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # sendEmailOne()
    sendEmailTwo()
