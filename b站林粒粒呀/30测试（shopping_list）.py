# unittest常用的python单元测试库，对软件中的最小可测试单元进行测试验证
# 比如验证某函数某方面表现是否符合预期
# 代码分开，
# 实现代码为my_calculator.py文件


# def my_adder(x, y):
#     return x + y
#
# 测试代码test_my_calculator.py文件
#
#
# import unittest
# from my_calculator import my_adder
#
#
# class TestMyAdder(unittest.TestCase):
#     def test_positive_with_positive(self):
#         self.assertEqual(my_adder(5, 3), 8)
#
#     def test_negative_with_positive(self):
#         self.assertEqual(my_adder(-5, 3), -2)

# 在终端输入：python -m unittest 运行

# shopping_list.py文件
class ShoppingList:
    """初始化购物清单，shopping_List是字典类型，包含商品名和对应价格
    例子：{'牙刷': 5, '沐浴露': 15, '电池': 7}"""
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    """返回购物清单上有多少项商品"""
    def get_item_count(self):
        return len(self.shopping_list)

    """返回购物清单商品价格总额数字"""
    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price


# test_shopping_list.py文件

import unittest
from shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({'纸巾': 8, '帽子': 30, '拖鞋': 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 53)

# 在终端输入：python -m unittest 运行
# 结果：
# PS D:\Pycharm-beginner\pythonProject> python -m unittest
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
# PS D:\Pycharm-beginner\pythonProject>

# 把53改成55后的测试结果：
# .F
# ======================================================================
# FAIL: test_get_total_price (test_shopping_list.TestShoppingList.test_get_total_price)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "D:\Pycharm-beginner\pythonProject\test_shopping_list.py", line 13, in test_get_total_price
#     self.assertEqual(self.shopping_list.get_total_price(), 55)
# AssertionError: 53 != 55
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# FAILED (failures=1)
