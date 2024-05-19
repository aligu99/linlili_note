# 在Python中，def 是用于定义函数的关键字。通过 def 关键字，你可以创建一个函数并指定其名称、参数和代码块。函数是一段可复用的代码，
# 它接受输入参数（如果有的话），执行一些特定的任务，并返回一个结果（如果有的话）。
# 以下是一个简单的函数定义的例子：
def greet(name):
    print(f"Hello, {name}!")


# 调用函数
greet("Alice")

# 在这个例子中，def 用于定义一个名为 greet 的函数，它接受一个参数 name，然后打印出相应的问候语。之后，通过 greet("Alice") 的调用，
# 我们传递参数 "Alice" 并执行函数。
# 函数定义的一般形式如下：


def function_name(parameters):
    # 函数体（代码块）
    # ...
    return result
# 可选，如果函数需要返回值的话
# function_name 是函数的名称。
# parameters 是函数的参数列表，可以包含零个或多个参数。
# 函数体包含了执行具体任务的代码块。
# return 语句（可选）用于返回函数的结果。

