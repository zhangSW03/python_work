#判断等级根据输入分数
score = int(input("请输入你的成绩："))

if score<0 or score>100:
    print("分数有误")
elif 90 <= score <= 100:
    print("成绩优秀")
elif 80 <= score < 90:
    print("成绩良好")
elif 70 <= score < 80:
    print("成绩中等")
elif 60 <= score < 70:
    print("成绩及格")
else:
    print("成绩不及格")
