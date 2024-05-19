print('哈喽呀！我是一个求平均值的程序。')
total = 0
count = 0
user_input = input('请输入数字（完成所有数字输入后，请输入q终止程序）：')
while user_input != 'q':
    num = float(user_input)
    total += num
    count += 1
    user_input = input('请输入数字（完成所有数字输入后，请输入q终止程序）：')
if count == 0:
    # 一个等号代表的含义是赋值，将某一数值赋给某个变量，比如a=3，将3这个数值赋予给a。两个等号是判断是否相等，返回True或False，比如1==1。
    result = 0
else:
    result = total / count
print('您输入的数字平均值为' + str(result))
