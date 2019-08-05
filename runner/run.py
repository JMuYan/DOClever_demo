# -*- coding: utf-8 -*-
import unittest
import HtmlTestRunner


# discover=unittest.defaultTestLoader.discover('D://lesson//pl0//lesson//Project//py190721//auto_demo',pattern='unittest_demo*.py')
discover = unittest.defaultTestLoader.discover(
    r'D:\PythonScript\framework-test\testcase', pattern='test*.py')
runner = HtmlTestRunner.HTMLTestRunner(output='report')
runner.run(discover)
