
gpa_dict = {'小明': 3.251, '小花': 3.869, '小李': 2.683, '小张': 3.685}
for name, gpa in gpa_dict.items():
    print('{0}你好，你的当前绩点为： {1}'.format(name, gpa))

# f指定浮点数在格式化时保留几位小数
gpa_dict = {'小明': 3.251, '小花': 3.869, '小李': 2.683, '小张': 3.685}
for name, gpa in gpa_dict.items():
    print('{0}你好，你的当前绩点为： {1:.2f}'.format(name, gpa))

# f字符串表达式
gpa_dict = {'小明': 3.251, '小花': 3.869, '小李': 2.683, '小张': 3.685}
for name, gpa in gpa_dict.items():
    print(f'''{name}你好，你的当前绩点为： {gpa:.2f}''')
