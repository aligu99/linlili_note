temperature_dict = {'111': 36.4, '112': 38.4, '113': 37.4, '114': 36.9, '115': 39.4, '116': 36.8, '117': 38.4,
                    '118': 38.7, '119': 39.4, '120': 37.4, '121': 36.5, '122': 38.4, '123': 36.4, '124': 39.4}
for staff_id, temperature in temperature_dict.items():
    # 键（staff_id），值（temperature），键值对（items）
    if temperature >= 39:
        print(staff_id, temperature)
# 方法一

temperature_dict = {'111': 36.4, '112': 38.4, '113': 37.4, '114': 36.9, '115': 39.4, '116': 36.8, '117': 38.4,
                    '118': 38.7, '119': 39.4, '120': 37.4, '121': 36.5, '122': 38.4, '123': 36.4, '124': 39.4}
for temperature_tuple in temperature_dict.items():
    staff_id = temperature_tuple[0]
    temperature = temperature_tuple[1]
    if temperature >= 39:
        print(staff_id)

total_sum = 0
for i in range(1, 101, 2):
    # 起始值，终止值，步长
    total_sum = total_sum + i
print(total_sum)
