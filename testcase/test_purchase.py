# -*- coding: utf-8 -*-
import os
import random
from BeautifulReport import BeautifulReport
import time
import unittest

from selenium.webdriver.common.keys import Keys

from common import object_erp_ui
from common.businesslib import ERP, Business
from common.extend_lib import VariableLib
from frameworklib.corelib import SeleniumLib


class Purchase(unittest.TestCase):
    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # os.path.abspath(r"D:\PythonScript\report-demo\img")截图存放路径
        self.bl.driver.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(r"D:\PythonScript\framework-test\runner\img"), img_name))

    @classmethod
    def setUpClass(cls):
        bl = ERP()
        cls.bl = bl
        cls.bl.framework_setup()
        cls.bl.login("ck3", "123456")

    @classmethod
    def tearDownClass(cls):
        cls.bl.framework_teardown()

    @BeautifulReport.add_test_img("test_1_big_cargo_purchase")
    def test_1_big_cargo(self):
        """采购入库单"""
        self.bl.locator_click(object_erp_ui.wh_warehouse_manage)
        self.bl.locator_click(object_erp_ui.wh_warehousing_manage)
        self.bl.locator_click(object_erp_ui.wh_create_purchase)
        Business(self.bl).purchase(2, 2)
        try:
            self.assertIn(
                "成功", self.bl.new_find_element(object_erp_ui.erp_success).text)
        except Exception as e:
            print(e)
        time.sleep(2)

    @BeautifulReport.add_test_img("test_2_bulk")
    def test_2_bulk(self):
        """新建散剪采购入库"""
        # self.bl.locator_click(object_erp_ui.wh_warehouse_manage)
        # self.bl.locator_click(object_erp_ui.wh_warehousing_manage)
        self.bl.locator_click(object_erp_ui.wh_create_purchase)
        # 更换入库类型
        self.bl.locator_click(object_erp_ui.wh_click_change_type)
        self.bl.locator_click(object_erp_ui.wh_choice_type_1)
        Business(self.bl).purchase(2, 2)
        try:
            self.assertIn(
                "成功", self.bl.new_find_element(object_erp_ui.erp_success).text)
        except Exception as e:
            print(e)
        time.sleep(2)

    @BeautifulReport.add_test_img("test_3_bigcargo_to_sortingcentre")
    def test_3_bigcargo_to_sortingcentre(self):
        """采购入库到分拣中心"""
        # self.bl.locator_click(object_erp_ui.wh_warehouse_manage)
        # self.bl.locator_click(object_erp_ui.wh_warehousing_manage)
        self.bl.locator_click(object_erp_ui.wh_create_purchase)
        # 选择分拣中心
        self.bl.locator_click(object_erp_ui.wh_choice_sortingcentre)
        self.bl.locator_click(object_erp_ui.wh_click_choose)
        self.bl.locator_click(object_erp_ui.wh_choosing_sortingcentre1)
        Business(self.bl).purchase(2, 2)
        try:
            self.assertIn(
                "成功", self.bl.new_find_element(object_erp_ui.erp_success).text)
        except Exception as e:
            print(e)
        time.sleep(2)
        # 确认入库
        self.bl.locator_click(object_erp_ui.wh_determine_warehousing)
        self.bl.locator_click(object_erp_ui.wh_determine_warehousing_again)
        try:
            self.assertIn(
                "成功", self.bl.new_find_element(object_erp_ui.erp_success).text)
        except Exception as e:
            print(e)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
