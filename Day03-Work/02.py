#列表合并去重 列表推导式
class_a = [101, 102, 105, 108, 102, 110, 105, 112, 108]
class_b = [105, 106, 108, 109, 111, 101, 113, 106]
# 1
merged = class_a + class_b
# 2
unique_list = list(set(merged))
# 3
odd_list = [num for num in unique_list if num % 2 != 0]
# 4
new_list = [num+10000 for num in odd_list]

print(merged)
print(unique_list)
print(odd_list)
print(new_list)