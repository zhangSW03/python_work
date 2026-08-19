#1.求梯形面积
# high = float(input("请输入梯形的高："))
# a = float(input("请输入梯形的上底"))
# b = float(input("请输入梯形的下底"))
# #对输入进行判断
# if a<0 or b<0:
#     raise ValueError("上底、下底不能为负数")
# elif high<=0:
#     raise ValueError("高必须大于0")
# elif a ==0 and b==0:
#      raise ValueError("上底和下底不能同时为0，构不成图形")
#
# area = (a+b) * high/2
# print("梯形的面积是：",area)
#
#2.求圆的面积和周长
# import math
#
# r = float(input("请输入圆的半径："))
#
# perimeter = 2 * math.pi * r
# area = math.pi * r**2
#
# print("圆的周长是：",f'{perimeter:.2f}')
# print("圆的面积是：",f'{area:.2f}')

#3.求身体质量BMI
# height = float(input("请输入你的身高(m)"))
# weight = float(input("请输入你的体重(kg)"))
#
# if height==0 or weight==0:
#     raise ValueError("请输入正确的身高与体重")
#
# bmi = weight / (height ** 2)
# print("你的身体质量BMI是：",f'{bmi:.1f}')

#4.时间转化
time = int(input("请你输入一个秒数（s）："))
if time<0:
    raise ValueError("时间不能为负数")
else:
    h = time // 3600
    remain_s = time % 3600
    m = remain_s // 60
    s = remain_s % 60

    print(h,"小时",m,"分钟",s,"秒")

#5.输出苹果单价、重量、总价

# price = float(input("请输入苹果的单价(元)："))
# height=float(input("请输入购买重量(斤)："))
# sum = float(input("请输入计算的总价(元):"))
#
# print(f"苹果单价{price}元,购买{height}斤,总价{sum}元.")

#6.计算成绩总分和平均分
# chinese = float(input("请输入你的语文成绩："))
# math = float(input("请输入你的数学成绩："))
# english = float(input("请输入你的英语成绩："))
#
# if chinese<0 or math<0 or english<0:
#     print("成绩不应该为负数")
# else:
#     sum_score = chinese+math+english
#     avg_score = (chinese+math+english) / 3
#     print(f"你的总成绩为{sum_score}分,你的平均分是{avg_score}分。")

#7.判断整数
# a = int(input("请你输入一个整数:"))
#
# if a>10 and a<50:
#     print(True)
# else:
#     print(False)

#8.接受整数进行判断
# a = int(input("请你输入一个整数："))
#
# if a<=10 or a>=50:
#     print(True)
# else:
#     print(False)

#9.输入成绩进行判断
# chinese = float(input("请输入你的语文成绩："))
# math = float(input("请输入你的数学成绩："))
#
# if chinese<0 or math<0:
#     raise ValueError("请正确输入成绩，不该为负数")
# elif chinese>90 or math>90:
#     print(True)
# else:
#     print(False)

#10.模拟成绩统计与评优
name = input("请输入你的姓名：")
chinese = float(input("请输入你的语文成绩："))
english = float(input("请输入你的英语成绩："))

avg_score = (chinese +english) / 2
sum_score = chinese + english

if chinese<0 or english<0:
    print("请输入正确成绩，成绩不该为负数")
elif chinese>85 and english>85 or sum_score>180:
    print(f"姓名:{name},总分:{sum_score},平均分:{avg_score},是否评为优秀:True")
