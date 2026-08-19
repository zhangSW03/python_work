#猜数字
import random

num = random.randint(1,100)

count = 5
for i in range(1,6):
    n = int(input("请输入一个数："))
    recount = count - i
    if n> num:
        if recount > 0:
            print(f"猜大了，你还剩{recount}次")
    elif n<num:
        if recount > 0:
            print(f"猜小了，你还剩{recount}次")
    else:
        print("恭喜!猜中了!")
        break
else:
    print(f"游戏失败，正确数字是{num}")

