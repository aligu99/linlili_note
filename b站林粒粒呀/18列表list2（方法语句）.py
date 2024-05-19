price = [799, 1024, 200, 800]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
# 列表可变，可直接在列表中加元素，无需重新赋值
print(max_price)
print(min_price)
print(sorted_price)

s = 'Hello'
print(s.upper())
s = s.upper()
# 字符串不可变，需要重新赋值
print(s)
