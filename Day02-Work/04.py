#购物车折扣计算

price = float(input("请输入商品价格"))

if price < 0 :
    print("价格有误")
elif price >= 500:
    price = price * 0.8
    print(f'你的物品打折后的价格是{price:.2f}')
elif 300 <= price < 500 :
    price = price * 0.9
    print(f'你的物品打折后的价格是{price:.2f}')
elif 100 <= price < 300 :
    price = price * 0.95
    print(f'你的物品打折后的价格是{price:.2f}')
else:
    print(f"商品无折扣，价格为{price}")