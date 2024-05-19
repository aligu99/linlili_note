# 高阶函数：把函数作为参数的函数
# 匿名函数：一次性调用
def calculate_and_print(num):
    result = num * num
    print(f'''
    | 数字参数 | {num} |
    | 计算结果 | {result} |''')


# 函数定义结束后调用
calculate_and_print(3)

"""
    | 数字参数 | 3 |
    | 计算结果 | 9 |
"""

