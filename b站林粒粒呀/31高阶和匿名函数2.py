def calculate_and_print(num, power):
    if power == 2:
        result = num * num
    elif power == 3:
        result = num * num * num
    else:
        print('只支持计算三次方和二次方')
        return
    print(f'''
    | 数字参数 | {num} |
    | 计算结果 | {result} |''')


calculate_and_print(3, 3)
"""
    | 数字参数 | 3 |
    | 计算结果 | 27 |
"""
# 你的代码存在一个缩进错误，calculate_and_print(3, 3)
# 应该位于函数定义的外部，以确保它是在函数之外被调用。另外，如果你想要在函数之外调用该函数，你应该将调用放在与函数定义相同地缩进级别，或者是它的上一级别。
# 原来calculate_and_print(3, 3)在def定义函数内（缩进4格），有错误。


def calculate_and_print(num, calculator):  # calculator函数作为参数传入新的（高阶）函数
    result = calculator(num)
    print(f'''
    |数字参数|{num}|
    |计算结果|{result}|''')


def calculate_square(num):
    return num * num


def calculate_cube(num):
    return num * num * num


def calculate_plus_10(num):
    return num + 10


# 函数调用
calculate_and_print(3, calculate_cube)
calculate_and_print(3, calculate_plus_10)
calculate_and_print(3, calculate_square)


# 可将格式化函数作为高阶函数的参数进行传入
def calculate_and_print(num, calculator, formatter):
    result = calculator(num)
    formatter(num, result)


def print_with_vertical_bar(num, result):
    print(f'''
    |数字参数|{num}|
    |计算结果|{result}|''')


def calculate_square(num):
    return num * num


def calculate_cube(num):
    return num * num * num


def calculate_plus_10(num):
    return num + 10


def calculate_times_5(num):
    return num * 5


calculate_and_print(3, calculate_cube, print_with_vertical_bar)

# 匿名函数
calculate_and_print(7, lambda num: num * 5, print_with_vertical_bar)


# 匿名函数形式
# def calculate_sum(num1, num2):
#     return num1 + num2
# 缩减为：
# lambda num1, num2: num1 + num2
# 也可被调用

(lambda num1, num2: num1 + num2)(2, 3)
