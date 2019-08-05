# -*- coding: utf-8 -*-
import os
import unittest
import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import time


class SendEmail(object):
    # 自动发送邮件
    def send_email(self, new_report):
        # 读取测试报告中的内容作为邮件的内容
        with open(new_report, 'r', encoding='utf8') as f:
            mail_body = f.read()
        # 发件人地址
        from_addr = 'g_test@126.com'
        # 收件人地址
        to_addr = 'rjbell@163.com'
        # 发送邮箱的服务器地址
        mail_server = 'smtp.126.com'
        # 邮件的标题
        subject = 'test01'
        # 发件人的邮箱地址
        username = 'g_test@126.com'
        password = 'shouquanma2019'
        # 邮箱的内容和标题
        message = MIMEText(mail_body, 'html', 'utf8')
        message['Subject'] = Header(subject, charset='utf8')
        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.login(username, password)
        smtp.sendmail(from_addr, to_addr.split(','), message.as_string())
        smtp.quit()

    # 获取最新报告的地址
    def acquire_report_address(self, reports_address):
        # 测试报告文件夹中的所有文件加入到列表
        test_reports_list = os.listdir(reports_address)
        # 按照升序排序生成新的列表
        new_test_reports_list = sorted(test_reports_list)
        # 获取最新的测试报告
        the_last_report = new_test_reports_list[-1]
        # 最新的测试报告的地址
        the_last_report_address = os.path.join(reports_address, the_last_report)
        return the_last_report_address


if __name__ == '__main__':
    # 测试报告文件夹地址
    test_reports_address = r'D:\PythonScript\framework-test\report'
    # 查找最新生成的测试报告地址
    new_report_addr = SendEmail().acquire_report_address(test_reports_address)
    # 自动发送邮件
    SendEmail().send_email(new_report_addr)
