#计算电费
n = float(input("请输入你的用电度数："))

if n<2880:
    price = n*0.4883
    print(f'你的用电费用是{price:.2f}元')
elif 2880 <= n < 4800:
    price = (n-2880)*0.5383 + 2880*0.4883
    print(f'你的用电费用是{price:.2f}元')
elif n >= 4800:
    price = (n-4800)*0.7883+2880*0.4883+ (4800-2880)*0.5383
    print(f'你的用电费用是{price:.2f}元')
