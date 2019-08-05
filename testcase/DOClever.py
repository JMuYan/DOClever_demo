# -*- coding:utf-8 -*-
import os

from BeautifulReport import BeautifulReport
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginCase(unittest.TestCase):
    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # os.path.abspath(r"D:\PythonScript\jenkins-demo\runner\img")截图存放路径
        self.driver.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(r"D:\PythonScript\jenkins-demo\runner\img"), img_name))

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://www.doclever.cn/controller/login/login.html')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        pass

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    @BeautifulReport.add_test_img("test_1_login")
    def test_1_login(self, username="rjBell", password="123456"):
        """登陆"""
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.ENTER)
        name = self.driver.find_element_by_xpath("//div[@class='el-dropdown']//span/span").text
        self.assertIn('rjBell', name)
        self.driver.implicitly_wait(30)

    @BeautifulReport.add_test_img("test_2_create_grouping")
    def test_2_create_grouping(self):
        """在PyautoDemo下创建HomeWork"""
        # 点击目录PyautoDemo
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[text()='PyautoDemo']").click()
        self.driver.implicitly_wait(5)
        # 判断HomeWork是否存在，存在无需创建，不存在先创建
        div1 = self.driver.find_element_by_id("tree")
        divs1 = div1.find_elements_by_xpath('div')
        nums1 = len(divs1)
        # print(nums1)
        judge_content = 0  # 用于判断有没有找到HomeWork，找到的话就不用创建了
        for n1 in range(1, nums1):
            judge = self.driver.find_element_by_xpath(f"//div[@id='tree']/div[{1+n1}]").text
            if "HomeWork" in judge:
                judge_content = 0
                # print("找到了HomeWork")
                break
            else:
                judge_content = -1  # 用于表示没有找到HomeWork
                continue
        if judge_content == -1:
            # 点击+开始创建目录
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//button[@aria-describedby]//i[@class='el-icon-plus']").click()
            self.driver.find_element_by_xpath(
                "//div[@class='el-message-box__input']//input").send_keys("HomeWork")
            self.driver.find_element_by_xpath(
                "//div[@class='el-message-box__btns']//span[contains(text(),'确定')]").click()
            div2 = self.driver.find_element_by_id("tree")
            divs2 = div2.find_elements_by_xpath("div")
            nums2 = len(divs2)
            # print(nums2)
            self.assertEqual(nums1+1, nums2)
        else:
            pass

    @BeautifulReport.add_test_img("test_3_create_interface")
    def test_3_create_interface(self):
        """创建接口demo1"""
        time.sleep(2)
        box = self.driver.find_element_by_xpath("//div[contains(text(),'HomeWork')]")
        ActionChains(self.driver).move_to_element(box).perform()
        self.driver.find_element_by_xpath(
            "//div[contains(text(),'HomeWork')]/..//i[@title='新建接口']").click()
        # 基本信息
        for i1 in range(1, 3):
            self.driver.find_element_by_xpath(
                f"//div[contains(text(),'基本信息')]/../form/div[1]/div[{i1}]//input").send_keys("demo1")
        self.driver.find_element_by_xpath(
            "//div[contains(text(),'基本信息')]/../form/div[3]/div[1]//input[@placeholder='请选择']").click()
        self.driver.find_element_by_xpath("//span[text()='POST']").click()
        self.driver.find_element_by_xpath(
            "//input[@placeholder='请输入接口路径(不包含BaseUrl)']").send_keys("/user/login")
        # 参数Body
        self.driver.find_element_by_xpath(
            "//span[contains(text(),'Key-Value')]/../../..//tr[1]//input[@placeholder='请填写参数名称']"
        ).send_keys("name")
        self.driver.find_element_by_xpath(
            "//span[contains(text(),'Key-Value')]/../../..//tr[1]//span[text()='未填值']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入可能的值']").send_keys("rjBell")
        self.driver.find_element_by_xpath(
            "//div[@class='el-dialog__footer']//span[contains(text(),'保存')]").click()
        self.driver.find_element_by_xpath(
            "//span[contains(text(),'Key-Value')]/../../..//tr[2]//input[@placeholder='请填写参数名称']"
        ).send_keys("password")
        self.driver.find_element_by_xpath(
            "//span[contains(text(),'Key-Value')]/../../..//tr[2]//span[text()='未填值']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入可能的值']").send_keys("123456")
        self.driver.find_element_by_xpath(
            "//div[@class='el-dialog__footer']//span[contains(text(),'保存')]").click()
        # 保存
        self.driver.find_element_by_xpath("//label[@role='checkbox']/..//span[text()='保存']").click()
        # 运行接口
        self.driver.find_element_by_xpath(
            "//label[@role='checkbox']/..//span[contains(text(),'运行')]").click()
        self.driver.find_element_by_xpath(
            "//input[@placeholder='选择或者填入你的BaseUrl']").send_keys("http://www.doclever.cn:8090")
        self.driver.find_element_by_xpath("//button[@title='运行']").click()
        time.sleep(2)
        self.assertTrue(self.is_element_present(By.XPATH, './/*[contains(text(),\'"code":200\')]'))

    @BeautifulReport.add_test_img("test_4_logout")
    def test_4_logout(self):
        """退出登录"""
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(
                "//div[@style]/span[starts-with(@aria-controls,'dropdown-menu')]")).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[text()='退出']").click()
        time.sleep(2)
        self.assertTrue(self.is_element_present(By.XPATH, "//a[text()='登录']"))
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
