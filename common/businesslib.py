# -*- coding: utf-8 -*-
import random
import time

from selenium.webdriver.common.keys import Keys

from common import object_erp_ui
from common.extend_lib import VariableLib
from frameworklib.corelib import SeleniumLib


class ERP(SeleniumLib):
    def __init__(self):
        super().__init__()

    def login(self, p_user, p_pwd):
        self.locator_send_keys(object_erp_ui.login_name, p_user)
        self.locator_send_keys(object_erp_ui.login_pwd, p_pwd)
        self.locator_click(object_erp_ui.login_btn)


class Business(object):
    def __init__(self, bl):
        self.bl = bl

    def purchase(self, color_rows, row_nums):
        # 编号
        self.bl.locator_send_keys(object_erp_ui.wh_create_fabric, "SE1227001")
        self.bl.locator_send_keys(object_erp_ui.wh_create_fabric, Keys.ENTER)
        row = 1  # 第几行
        # color_rows = 2  # rows-1个色号
        # row_nums = 2  # 每个色号几行
        if row_nums * color_rows <= 20:
            for x in range(1, color_rows):
                # 色号
                color_locator = f"xpath=//div[@class='li-table-body']/div[{row}]/div[3]//input"
                # self.bl.locator_click(locator)
                self.bl.locator_send_keys(color_locator, f"{x}")
                self.bl.locator_send_keys(color_locator, Keys.ENTER)
                # 缸号
                dyelot_nums = VariableLib().dyelot_num()
                dy_locator = f"xpath=//div[@class='li-table-body']/div[{row}]/div[10]//input"
                self.bl.locator_send_keys(dy_locator, f"{dyelot_nums}")
                self.bl.locator_send_keys(dy_locator, Keys.ENTER)
                # 数量
                for i in range(row_nums):
                    quantities = float('%.1f' % random.uniform(18, 29))
                    quantities_locator = f"xpath=//div[@class='li-table-body']/div[{i + row}]/div[11]//input"
                    self.bl.locator_send_keys(quantities_locator, f"{quantities}")
                    self.bl.locator_send_keys(quantities_locator, Keys.ENTER)
                row = row + row_nums
            self.bl.locator_click(f"xpath=//div[@class='li-table-body']/div[{row}]/div[13]//i[@title='删除']")
        if row_nums * color_rows > 20:
            pass
        # 提交
        self.bl.locator_click(object_erp_ui.wh_determine_sub)
        self.bl.locator_click(object_erp_ui.wh_determine_in)

    # fabric_no：面料个数、color_no：色号个数、sale_number：销售数量
    # fabric_number：面料编号、warehouse：仓库
    # warehouse_type，用来选择仓库模式：-1表示不对仓库操作，0表示自定义选择，1针对面料SE1227001色号1和2选择的仓库
    def sale_big_cargo(
            self, fabric_no, color_no, sale_number,
            fabric_number=None, warehouse='1号仓', warehouse_type=-1):
        # 选择客户
        self.bl.locator_send_keys(object_erp_ui.sale_input_customer, "金")
        self.bl.locator_send_keys(object_erp_ui.sale_input_customer, Keys.ARROW_DOWN)
        self.bl.locator_send_keys(object_erp_ui.sale_input_customer, Keys.ENTER)
        xpath1 = "xpath=//p[contains(text(),'仓库销售')]/../../div/div/div/div[@class='li_table']" \
                 "/div[@class='li-table-body']"
        xpath2 = "xpath=//p[contains(text(),'仓库销售')]/../../div/div/div/div[@class='li_table']"
        # 输入面料编号并选择
        for n in range(1, fabric_no + 1):
            sale_input_fabric = f"{xpath1}/div[{n}]/div[2]//input"
            if fabric_number is None:
                self.bl.locator_send_keys(sale_input_fabric, f"SE122700{n}")
                self.bl.locator_send_keys(sale_input_fabric, Keys.ENTER)
            else:
                self.bl.locator_send_keys(sale_input_fabric, fabric_number)
                self.bl.locator_send_keys(sale_input_fabric, Keys.ENTER)
            # 输入色号并回车
            sale_input_color = f"{xpath1}/div[{n}]/div[3]//input[@placeholder='输入色号']"
            for i in range(1, color_no + 1):
                self.bl.locator_send_keys(sale_input_color, f"{i}")
                self.bl.locator_send_keys(sale_input_color, Keys.ENTER)
        # 销售数量回车，最后一行回车
        for x in range(1, fabric_no + 1):
            for y in range(1, color_no + 1):
                sale_input_quantities = f"{xpath1}/div[{x}]/div[5]//div[@class='row_list']/div/div[{y}]//input"
                if x + y == fabric_no + color_no:
                    self.bl.locator_send_keys(sale_input_quantities, sale_number)
                    break
                else:
                    self.bl.locator_send_keys(sale_input_quantities, sale_number)
                    self.bl.locator_send_keys(sale_input_quantities, Keys.ENTER)
        # 选择仓库
        if warehouse_type == -1:
            pass
        elif warehouse_type == 0:
            for i in range(1, fabric_no * color_no + 1):
                self.bl.locator_click(f"{xpath1}/div[1]/div[9]/div/div/div[{i}]//span")
                self.bl.locator_click(f"//div[@x-placement='bottom']/ul[2]/li[text()='{warehouse}']")
        elif warehouse_type == 1:
            for n in range(1, fabric_no * color_no + 1):
                self.bl.locator_click(f"{xpath1}/div[1]/div[9]/div/div/div[{n}]//span")
                if n == 2:
                    self.bl.locator_click(f"//div[@x-placement='bottom']/ul[2]/li[text()='W20']")
                else:
                    self.bl.locator_click(f"//div[@x-placement='bottom']/ul[2]/li[text()='1号仓']")

        # 输入销售单价
        price = time.strftime("%S.%M", time.localtime(time.time()))
        for x in range(1, fabric_no + 1):
            for y in range(1, color_no + 1):
                sale_input_price = f"{xpath1}/div[{x}]/div[7]//div[@class='row_list']/div/div[{y}]//input"
                self.bl.new_find_element(sale_input_price).send_keys(Keys.CONTROL, 'a')
                self.bl.new_find_element(sale_input_price).send_keys(Keys.BACK_SPACE)
                self.bl.locator_send_keys(sale_input_price, f"{price}")
        # 提交订单
        self.bl.locator_click("xpath=//span[text()='确定开单']")

