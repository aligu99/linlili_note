# 定义一个学生类
# 要求：
# 1．属性包括学生姓名、学号，以及语数英三个科目的成绩
# 2．能够设置学生某科目的成绩
# 3．能够打印出该学生的所有科目成绩
class Student:
    # 定义属性参数
    def __init__(self, name, student_id):
        # 绑定到对象身上的属性 = 普通属性
        self.name = name
        self.student_id = student_id
        # 定义字典，每个学生的成绩初始值为0
        self.grades = {'语文': 0, '数学': 0, '英语': 0}

    # 定义设置成绩的方法
    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f'学生{self.name} (学号: {self.student_id}) 的成绩为：')
        for course in self.grades:
            print(f'{course}: {self.grades[course]}分')

    # 不懂为什么加这个？
    def set_grades(self, param, param1):
        pass


# 创建学生对象
chen = Student('小陈', '100618')
chen.set_grade('语文', 92)
chen.set_grade('数学', 94)
chen.set_grade('英语', 88)
chen.print_grades()
zeng = Student('小曾', '100622')
# 对象名.属性名
print(chen.name)
zeng.set_grades('数学', 95)
print(zeng.grades)

# 练习 9.1：餐馆
# 创建⼀个名为 Restaurant 的类，为其方法__init__() 设置两个属性：
# restaurant_name 和 cuisine_type。
# 创建⼀个名为 describe_restaurant() 的⽅法和⼀个名为
# open_restaurant() 的⽅法，其中前者打印前述两项信息，⽽后者打印⼀条消息，
# 指出餐馆正在营业。
# 根据这个类创建⼀个名为 restaurant 的实例，分别打印其两个属性，
# 再调⽤前述两个⽅法。


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # 绑定到对象身上的属性 = 普通变量（值通过上述参数传递进来）
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'餐厅名是{self.restaurant_name}')
        print(f'菜系是{self.cuisine_type}')

    def open_restaurant(self):
        print('餐厅正在营业')


taotaoju = Restaurant('陶陶居', '粤菜')
print(taotaoju.restaurant_name)
print(taotaoju.cuisine_type)
taotaoju.describe_restaurant()
taotaoju.open_restaurant()
"""
陶陶居
粤菜
餐厅名是陶陶居
菜系是粤菜
餐厅正在营业
"""

# 练习 9.4：就餐⼈数
# 在为练习 9.1 编写的程序中，添加⼀个名为number_served 的属性，
# 并将其默认值设置为 0。根据这个类创建⼀个名为 restaurant 的实例。
# 打印有多少⼈在这家餐馆就餐过，然后修改这个值并再次打印。
# 添加⼀个名为 set_number_served() 的⽅法，⽤来设置就餐⼈
# 数。调⽤这个⽅法并向它传递新的就餐⼈数，然后再次打印这个值。
# 添加⼀个名为 increment_number_served() 的⽅法，⽤来让就餐⼈数递增。
# 调⽤这个⽅法并向它传递⼀个这样的值：你认为这家餐馆
# 每天可能接待的就餐⼈数。


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # 绑定到对象身上的属性 = 普通变量（值通过上述参数传递进来）
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'餐厅名是{self.restaurant_name}')
        print(f'菜系是{self.cuisine_type}')

    def open_restaurant(self):
        print('餐厅正在营业')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


taotaoju = Restaurant('陶陶居', '粤菜')
print(taotaoju.restaurant_name)
print(taotaoju.cuisine_type)
print(taotaoju.number_served)
taotaoju.describe_restaurant()
taotaoju.open_restaurant()
taotaoju.set_number_served(500)
taotaoju.increment_number_served(20)
print(taotaoju.number_served)
"""
0
餐厅名是陶陶居
菜系是粤菜
餐厅正在营业
520
"""





















