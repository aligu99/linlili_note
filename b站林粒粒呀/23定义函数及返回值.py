# 练习8-2：喜欢的图书
# 编写一个名为favorite_book()的函数，其中包含一个名为title的形参。
# 这个函数打印一条消息，下面是一个例子
# One f my favorite books is Alice in WonderLand
# 调用这个函数，并将一本图书的名称作为实参传递给它。

def favorite_book(title):
    print(f'One f my favorite books is {title}.')


favorite_book('Alice in WonderLand')
favorite_book('三体')


def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f'此扇形的面积为:{sector_area}')


calculate_sector(60, 6)
calculate_sector(90, 19)


# 返回值
def calculate_sector(central_angle, radius):
    # 定义域：函数里定义额变量都是局域变量，出到函数外就访问不到
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f'此扇形的面积为:{sector_area}')
    # 返回变量sector_area的值，同时给了函数之外继续用sector_area这个值的机会
    # 同时return后的代码也不再执行
    return sector_area


sector_area_1 = calculate_sector(60, 6)
sector_area_2 = calculate_sector(90, 19)


# 练习8-6：城市名
# 编写一个名为city_country）的函数，它接受城市的名称及其所属的国家.
# 这个函数应返回一个格式类似于下面的字符串：
# Santiago, Chile”
# 至少使用三个城市国家对来调用这个函数，并打印它返回的值.
def city_country(city, country):
    return f'{city}, {country}'


print(city_country('Santiago', 'Chile'))
print(city_country('Santi', 'Ch'))
print(city_country('深圳', '中国'))


def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Jimi Hendrix
