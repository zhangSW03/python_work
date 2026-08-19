#判断成绩等级
score = int(input("请输入你的成绩："))

if score<0 or score>100:
    print("请输入正确的成绩")
elif score>=85:
    print("你的成绩为优秀")
elif 60<= score <85:
    print("你的成绩为及格")
else:
    print("你的成绩不及格")