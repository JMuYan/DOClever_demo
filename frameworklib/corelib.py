# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import re
from frameworklib import datastore_configinfo
from frameworklib.debuglog import logger


class SeleniumLib(object):
    def __init__(self):
       pass

    def get_driver(self):
        logger.info('获取driver')
        return self.driver

    def launch_browser(self):
        browser = datastore_configinfo.GLOBAL_VAR_BROWSER
        if bool(re.search(browser, 'FireFox', re.IGNORECASE)):
            self.driver = webdriver.Firefox()
            logger.info('启动FireFox浏览器')
        elif bool(re.search(browser, 'Chrome', re.IGNORECASE)):
            self.driver = webdriver.Chrome()
            logger.info('启动Chrome浏览器')
        elif bool(re.search(browser, 'IE', re.IGNORECASE)):
            self.driver = webdriver.Ie()
            logger.info('启动IE浏览器')
        elif bool(re.search(browser, 'Safari', re.IGNORECASE)):
            self.driver = webdriver.Safari()
            logger.info('启动Safari浏览器')
        else:
            self.driver = None
            logger.ERROR('错误的浏览器配置参数，启动浏览器失败')

    def framework_setup(self):
        self.launch_browser()
        time.sleep(5)
        logger.info('driver初始化')
        base_url = datastore_configinfo.GLOBAL_VAR_URL
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        logger.info('框架初始化')

    def framework_teardown(self):
        self.driver.quit()
        logger.info('driver销毁')

    def new_find_element(self, p_obj):
        try:
            para = p_obj.index("=")
        # print(p_obj[:para])
        # print(p_obj[para+1:])
            if p_obj.startswith('id'):
                return self.driver.find_element_by_id(p_obj[para + 1:])
            elif p_obj.startswith('xpath'):
                return self.driver.find_element_by_xpath(p_obj[para + 1:])
            elif p_obj.startswith('link text'):
                return self.driver.find_element_by_link_text(p_obj[para + 1:])
            elif p_obj.startswith('name'):
                return self.driver.find_element_by_name(p_obj[para + 1:])
            elif p_obj.startswith('tag name'):
                return self.driver.find_element_by_class_name(p_obj[para + 1:])
            elif p_obj.startswith('css selector'):
                return self.driver.find_element_by_css_selector(p_obj[para + 1:])
            elif p_obj.startswith('partial link text'):
                return self.driver.find_element_by_partial_link_text(p_obj[para + 1:])
            else:
                logger.info(p_obj+"该元素没有明确是哪种方式定位，无法定位")
                return None
        except BaseException as err:
            logger.info("元素定位"+p_obj+"失败！ 详细信息：" + err)
            return None

    def locator_click(self,p_obj):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MIN_TIME)
        try:
            self.new_find_element(p_obj).click()
            logger.info('点击元素： ' + p_obj)
        except BaseException as err:
            logger.error('点击元素：' + p_obj+'失败！详细信息：'+err)

    def locator_clear(self,p_obj):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MIN_TIME)
        try:
            self.new_find_element(p_obj).clear()
            logger.info('清空输入框：' + p_obj)
        except BaseException as err:
            logger.error('清空输入框：' + p_obj+'失败！详细信息：'+err)

    def locator_send_keys(self, p_obj, p_key):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MID_TIME)
        try:
            self.new_find_element(p_obj).send_keys(p_key)
            # logger.info('向元素：' + p_obj + f' 写入信息：{p_key}')
            if p_key == "\ue007":
                logger.info('向元素：' + p_obj+' 写入信息：回车')
            elif p_key == "\ue015":
                logger.info('向元素：' + p_obj + ' 写入信息：↓')
            else:
                logger.info('向元素：' + p_obj+' 写入信息：' + f"{p_key}")
        except BaseException as err:
            logger.error('向元素：' + p_obj+' 写入信息：'+f"{p_key}"+'失败！详细信息：'+err)

    def locator_select(self, p_obj, p_key):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MIN_TIME)
        try:
            Select(self.new_find_element(p_obj)).select_by_visible_text('')
            logger.info('下拉框：' + p_obj + '选择子项：' + p_key)
        except BaseException as err:
            logger.error('下拉框：' + p_obj + '选择子项：' + p_key+'失败！详细信息：'+err)

    def locator_execute_js(self, p_script):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MIN_TIME)
        try:
            self.driver.execute_script(p_script)
            logger.info('执行java script脚本' + p_script)
        except BaseException as err:
            logger.error('执行java script脚本' + p_script+'失败！详细信息：'+err)

    def locator_switch_to_window(self, p_window_name):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MIN_TIME)
        try:
            current_window = self.driver.current_window_handle
            windows = self.driver.window_handles
            for switch_to_window in windows:
                if switch_to_window != current_window:
                    self.driver.switch_to.window(p_window_name)
            logger.info('执行new_switch_to_window' + p_window_name)
        except BaseException as err:
            logger.error('执行new_switch_to_window失败！详细信息：'+err)

    def locator_is_element_present(self, p_obj):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MIN_TIME)
        try:
            obj=self.new_find_element(p_obj)
            if obj==None:
                logger.info('当前页面不存在元素' + p_obj)
                return False
            else:
                logger.info('当前页面存在元素' + p_obj)
                return True
        except BaseException as err:
            # print('异常信息：' + err)
            logger.error('当前页面查找元素' + p_obj+'异常！详细信息：'+err)
            return False

    def locator_is_text_present(self, p_text):
        time.sleep(datastore_configinfo.GLOBAL_VAR_MIN_TIME)
        istext = '//*[contains(.,\''+p_text+'\')]'
        print (istext)
        try:
            self.driver.find_element_by_xpath(istext)
            logger.info('当前页面查找到文字' + p_text)
            return True
        except BaseException as err:
            # print('异常信息：' + err)
            logger.info('当前页面没有查找到文字' + p_text)
            return False