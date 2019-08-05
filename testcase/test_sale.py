# -*- coding: utf-8 -*-
import os
import random

import time
import unittest

from BeautifulReport import BeautifulReport
from selenium.webdriver.common.keys import Keys

from common import object_erp_ui
from common.businesslib import ERP, Business
from frameworklib.corelib import SeleniumLib


class Sale(unittest.TestCase):
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
        bl = ERP()  # 如果使用run_teacher,实例的名称必须是bl
        cls.bl = bl
        cls.bl.framework_setup()
        cls.bl.login("xs2", "123456")

    @classmethod
    def tearDownClass(cls):
        cls.bl.framework_teardown()

    @unittest.skip("保留仓库大货开单脚本源码")
    def test_create_big_cargo_for_warehouse(self):
        """新建仓库大货订单"""
        self.bl.locator_click(object_erp_ui.sale_manage)
        self.bl.locator_click(object_erp_ui.sale_create_order)
        self.bl.locator_click(object_erp_ui.sale_create_big_cargo)
        # 选择客户
        self.bl.locator_send_keys(object_erp_ui.sale_input_customer, "金")
        self.bl.locator_send_keys(object_erp_ui.sale_input_customer, Keys.ARROW_DOWN)
        self.bl.locator_send_keys(object_erp_ui.sale_input_customer, Keys.ENTER)
        # 输入面料编号并选择
        fabric = "58"
        self.bl.locator_send_keys(object_erp_ui.sale_input_fabric, fabric)
        self.bl.locator_send_keys(object_erp_ui.sale_input_fabric, "0")
        self.bl.locator_click(f"xpath=//li[contains(text(),'{fabric}')]")
        # 输入色号并回车
        self.bl.locator_send_keys(object_erp_ui.sale_input_color, "1")
        self.bl.locator_send_keys(object_erp_ui.sale_input_color, Keys.ENTER)
        # 输入销售数量
        self.bl.locator_send_keys(object_erp_ui.sale_input_quantities, "1")
        # 输入销售单价
        price = float('%.2f' % random.uniform(15, 60))
        self.bl.new_find_element(object_erp_ui.sale_input_prices).send_keys(Keys.CONTROL, 'a')
        self.bl.new_find_element(object_erp_ui.sale_input_prices).send_keys(Keys.BACK_SPACE)
        self.bl.locator_send_keys(object_erp_ui.sale_input_prices, f"{price}")
        # 提交订单
        self.bl.locator_click(object_erp_ui.sale_determine_sub)
        # 验证
        try:
            self.assertIn(
                "成功", self.bl.new_find_element(object_erp_ui.erp_success).text)
        except Exception as e:
            print(e)
        time.sleep(2)
        # 取消订单
        self.bl.locator_click(object_erp_ui.sale_cancel_order)
        self.bl.locator_click(object_erp_ui.sale_determine_cancel)

    # @BeautifulReport.stop
    @BeautifulReport.add_test_img("test_1_create_big_cargo_for_warehouse")
    def test_1_create_big_cargo_for_warehouse(self):
        """新建仓库大货订单"""
        self.bl.locator_click(object_erp_ui.sale_manage)
        self.bl.locator_click(object_erp_ui.sale_create_order)
        self.bl.locator_click(object_erp_ui.sale_create_big_cargo)
        Business(self.bl).sale_big_cargo(fabric_no=1, color_no=2, sale_number=2)
        # 验证
        try:
            self.assertIn(
                "成功", self.bl.new_find_element(object_erp_ui.erp_success).text)
        except Exception as e:
            print(e)
        time.sleep(2)
        # 取消订单
        self.bl.locator_click(object_erp_ui.sale_cancel_order)
        self.bl.locator_click(object_erp_ui.sale_determine_cancel)


if __name__ == '__main__':
    unittest.main()
