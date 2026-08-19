#打印字符串的字符出现次数
n = 'akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd'
count_a = 0
count_k = 0

for i in n:
    if i == "a":
        count_a += 1
    if i == "k":
        count_k += 1
print(f"字符a出现了{count_a}次")
print(f"字符k出现了{count_k}次")