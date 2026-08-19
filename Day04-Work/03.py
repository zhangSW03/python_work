#1.判断是否为闰年
# def is_leap_year(year:int)->bool:
#     if year % 400==0 or (year % 4 ==0 and year % 100 != 0):
#         return True
#     else:
#         return False
#
# year = int(input('请输入一个年份(整数):'))
# if is_leap_year(year):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")

#2.接收字典 返回数据
# def find_best_student(students):
#     if not students:
#         return 0
#     max_score = max(students.values())
#     stu = [(name,score) for name,score in students.items() if score == max_score]
#     return stu
#
#
# students = {"小明": 88, "小红": 95, "小刚": 72, "小丽": 92, "小军": 84}
# best = find_best_student(students)
# name, score = best[0]
# print(f"{name}同学成绩最高，成绩为:{score}")

#3.打印大小写
# def count_case(str):
#     upper_str = 0
#     lower_str = 0
#     for ch in str:
#         if ch.isupper():
#             upper_str += 1
#         elif ch.islower():
#             lower_str += 1
#     return upper_str,lower_str
#
# s = 'Hello World! Python3 编程'
# upper,lower = count_case(s)
# print(f"大写字母有{upper}个，小写字母有{lower}个")

def double(x):
    return x*2

res = map(double,[1,2,3])
print(list(res))
