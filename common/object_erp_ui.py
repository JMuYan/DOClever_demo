# -*- coding: utf-8 -*-
"""
  ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""
erp_success = "xpath=//div[contains(@class,'ivu-message-success')]"

# 登录login
login_name = "xpath=//input[@placeholder='请输入用户名']"
login_pwd = "xpath=//input[@placeholder='请输入密码']"
login_btn = "xpath=//button[@type='button']"

#  销售sale
sale_manage = "xpath=//span[contains(text(), '销售管理' )]"
sale_create_order = "xpath=//span[contains(text(), '柜台开单' )]"
sale_create_big_cargo = "xpath=//span[contains(text(), '新建大货订单' )]"

sale_input_customer = "xpath=//input[contains(@placeholder,'请输入客户')]"
same_path = "//p[contains(text(),'仓库销售')]/../../div/div/div/div[@class='li_table']/div[@class='li-table-body']"
sale_input_fabric = f"xpath={same_path}/div[1]/div[2]//input"
sale_input_color = f"xpath={same_path}/div[1]/div[3]//input[@placeholder='输入色号']"
sale_input_quantities = f"xpath={same_path}/div[1]/div[5]//input"
sale_input_prices = f"xpath={same_path}/div[1]/div[7]//input"

sale_determine_sub = "xpath=//span[text()='确定开单']"
sale_cancel_order = "xpath=//span[contains(text(), '取消订单')]"
sale_determine_cancel = "xpath=//p[text()='取消订单']/../../..//span[contains(text(),'确定')]"
sale_close_details = "xpath=//button[@class='but ivu-btn ivu-btn-ghost']/span[text()='关闭']"

# 仓库 warehouse
wh_warehouse_manage = "xpath=//span[contains(text(), '仓库管理' )]"
wh_warehousing_manage = "xpath=//span[contains(text(), '入库管理' )]"
wh_create_purchase = "xpath=//div[contains(text(), '新建采购入库' )]"

wh_click_change_type = "xpath=//span[contains(text(),'大货')]"
wh_choice_type_1 = "xpath=//li[contains(text(),'散剪')]"
wh_choice_type_2 = "xpath=//li[contains(text(),'大货')]"
wh_choice_sortingcentre = "xpath=//label[text()='分拣中心']//input"
wh_click_choose = "xpath=//span[text()='请选择']"
wh_choosing_sortingcentre1 = "xpath=//li[contains(text(),'分拣中心1')]"
wh_create_fabric = "xpath=//div[@class='li-table-body']/div[1]/div[2]//input"

wh_determine_sub = "xpath=//span/span[text()='确定']"
wh_determine_in = "xpath=//button/span[contains(text(),'入库')]"
wh_determine_warehousing = "xpath=//tr[1]//span[text()='确认入库']"
wh_determine_warehousing_again = "xpath=//span[text()='确定']"





