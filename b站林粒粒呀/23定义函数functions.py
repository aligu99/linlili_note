# 写一个计算BMI的函数，函数名为 calculate＿BMI。
# 1．可以计算任意体重和身高的BMI值
# 2．执行过程中打印一句话，“您的BMI分类为：xx”
# 3．返回计算出的BMI值

# BMI＝体重／（身高 ＊＊2）
#
# BMI分类
# 偏瘦：BMI ＜＝18.5
# 正常：18.5 < BMI <=25
# 偏胖：25＜BMI ＜＝ 30
# 肥胖：BMI＞30


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        category = '偏瘦'
    elif bmi <= 25:
        category = '正常'
    elif bmi <= 30:
        category = '偏胖'
    else:
        category = '肥胖'
    print(f'您的BMI分类为：{category}')
    # f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
    return bmi


result = calculate_bmi(70, 1.8)
print(result)


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        category = '偏瘦'
    elif bmi <= 25:
        category = '正常'
    elif bmi <= 30:
        category = '偏胖'
    else:
        category = '肥胖'
    print(f'您的BMI分类为：{category}')
    # f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
    return bmi


weight = float(input('请输入您的体重（kg）：'))
height = float(input('请输入您的升高（m）：'))
result = calculate_bmi(weight, height)
print(result)
