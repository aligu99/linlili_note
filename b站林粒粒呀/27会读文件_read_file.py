# 相对路径
# 1、读取文件方法1
file = open('./27data.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()

# 1、读取文件方法2
with open('./27data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 2、逐行读取一行内容
with open('./27data.txt', 'r', encoding='utf-8') as file:
    print(file.readline())
    print(file.readline())

# 3、逐行读取所有内容
with open('./27data.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())

# 4、读取每行所有内容
with open('./27data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
