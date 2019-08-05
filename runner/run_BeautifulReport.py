# -*- coding:utf-8 -*-
import time
import unittest
from BeautifulReport import BeautifulReport

from frameworklib.commonlib import ZipReport, SendMail
from frameworklib.email_lib_test import SendEmail

if __name__ == '__main__':
    test_dir = r"D:\PythonScript\framework-test\testcase"
    suite_tests = unittest.defaultTestLoader.discover(test_dir, pattern="test_sale.py", top_level_dir=None)
    now = time.strftime("%Y%m%d")
    filename = now + "TestReport.html"
    report_dir = r"D:\\PythonScript\framework-test\runner\report"
    BeautifulReport(suite_tests).report(filename=filename, description='测试报告', log_path=report_dir)
    """
    # 把生成的htmlreport以及截屏文件打包
    zip = ZipReport()
    zip.zipFile()
    
    # 发送邮件，附件是最新生成的zip打包文件
    mail = SendMail()
    mail.send_mail(mail.find_new_file())
    """
