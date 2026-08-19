#计算BMI

weight = float(input("请输入你的体重(kg):"))
height = float(input("请输入你的身高(m):"))

bmi = weight / (height ** 2)

if weight <=0 or height <=0:
    print("输入身高，体重数据有误")
elif bmi < 18.5:
    print(f"你的BMI是{bmi:.2f},属于偏瘦")
elif 18.5 <= bmi < 24:
    print(f"你的BMI是{bmi:.2f},属于正常")
elif 24 <= bmi < 28:
    print(f"你的BMI是{bmi:.2f},属于偏胖")
else:
    print(f"你的BMI是{bmi:.2f},属于肥胖")