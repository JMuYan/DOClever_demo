# -*- coding: utf-8 -*-
import configparser
import os
import smtplib
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import datetime
from frameworklib import datastore_log
from frameworklib.debuglog import logger


class IniFile(object):
    @classmethod
    def get_ini_value(cls, p_section, p_key):
        from frameworklib import datastore_configinfo  # 防止交叉引用
        value = None
        ini_file = datastore_log.GLOBAL_VAR_CONFIG_FILE
        config = configparser.ConfigParser()
        if config.read(ini_file).__len__() == 0:
            logger.info('没有找到ini文件 ' + ini_file)
            return value
        else:
            logger.info("成功找到ini文件")
        try:
            value = config.get(p_section, p_key)

        except configparser.NoSectionError:
            logger.info('没有指定的section')
        except configparser.NoOptionError:
            logger.info('没有指定的option')
        finally:
            return value


class SendMail(object):
    smtpserver = 'smtp.126.com'
    user = 'g_test@126.com'
    # port = '25'
    password = 'shouquanma2019'
    sender = 'g_test@126.com'
    receiver = '2076813067@qq.com'
    subject = '自动化测试报告01'
    encode = 'utf-8'
    attachment_path = datastore_log.GLOBAL_VAR_REPORT_PATH
    attachment_displayname = 'report.zip'

    def send_mail(self, p_attachment):
        try:
            f = open(p_attachment, 'rb')
            mail_attchment = f.read()
            f.close()
            msg = MIMEMultipart()
            att = MIMEText(mail_attchment, 'base64', self.encode)
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment; filename='+self.attachment_displayname
            msg.attach(att)
            msg['Subject'] = Header(self.subject, self.encode)
            msg['From'] = self.sender
            msg['TO'] = self.receiver
            smtp = smtplib.SMTP()
            # smtp.starttls()
            smtp.connect(self.smtpserver)
            smtp.login(self.user, self.password)
            smtp.sendmail(self.user, self.receiver, msg.as_string())
            smtp.quit()
            print('发送邮件成功')
        except smtplib.SMTPException as err:
            print('Error: 无法发送邮件。详细信息： '+str(err))

    def find_new_file(self):
        lists=os.listdir(self.attachment_path)
        lists.sort(key=lambda fn:os.path.getmtime(self.attachment_path+'/'+fn))  # 文件的最近修改时间
        file_new=os.path.join(self.attachment_path, lists[-1])
        print('最新修改的文件是： '+file_new)
        return file_new


class ZipReport(object):
    filter = ['.html', '.png']
    report_time = datetime.datetime.now().strftime('%Y%m%d')
    report_name = report_time + 'TestReport.zip'

    zip_file_folder=datastore_log.GLOBAL_VAR_REPORT_PATH
    new_zip_file= datastore_log.GLOBAL_VAR_REPORT_PATH + '/' + report_name

    def get_all_filepath(self, dirname, filter_list=[]):  # 获取需要打包的文件
        result = []  # 所有的文件
        for maindir, subdir, file_name_list in os.walk(dirname):
            # maindir 当前主目录
            # subdir当前主目录下的所有目录
            # file_name_list #当前主目录下的所有文件
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
                if ext in filter_list:
                    result.append(apath)
        return result

    def get_all_dirpath(self, dirname, dir_list=[]):  # 获取需要打包的目录
        result = []  # 所有的文件
        for maindir, subdir, dirs in os.walk(dirname):
            # maindir 当前主目录
            # subdir当前主目录下的所有目录
            # dirs #当前主目录下的所有子目录（不包括文件）
            for dir in dirs:
                apath = os.path.join(maindir, dir)  # 合并成一个完整路径
                ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
                if ext in dir_list:
                    result.append(apath)
        return result

    def zipFile(self):  # 把获取到的需要打包的文件进行打包操作
        f = zipfile.ZipFile(self.new_zip_file, 'w', zipfile.ZIP_DEFLATED)
        dirlist = self.get_all_dirpath(self.zip_file_folder, self.filter)
        for i in range(len(dirlist)):
            # for i in dirlist:
            f.write(dirlist[i])
        f.close()


if __name__ == '__main__':
    zip = ZipReport()
    zip.zipFile()
    sd = SendMail()
    sd.send_mail(sd.find_new_file())

