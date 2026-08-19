# 每天打开数据
monday    = ("王林", "李慕婉", "司徒南", "柳眉", "周佚", "清水仙君", "红蝶")
tuesday   = ("王林", "司徒南", "柳眉", "清水仙君", "红蝶", "徐立国", "许木")
wednesday = ("王林", "李慕婉", "司徒南", "周佚", "柳眉", "清水仙君", "红蝶", "徐立国")
thursday  = ("王林", "李慕婉", "周佚", "红蝶", "徐立国", "虎咆", "遁天")
friday    = ("司徒南", "柳眉", "清水仙君", "红蝶", "王林", "许木", "虎咆")

# 员工集合
all_employees = {"王林", "李慕婉", "司徒南", "柳眉", "周佚", "清水仙君", "红蝶", "徐立国", "许木", "虎咆", "遁天", "姜老道"}


#1.将元组合并到大列表中 all_records
all_records = [*monday,*tuesday,*wednesday,*thursday,*friday]
print(all_records)

#2.找出全勤员工
employees = set(monday)&set(tuesday)&set(wednesday)&set(thursday)&set(friday)
print(employees)

#3.找出从未到岗的员工
not_employees = all_employees-set(monday)-set(tuesday)-set(wednesday)-set(thursday)-set(friday)
print(not_employees)

#4.统计每位员工的出勤天数
count = {}
for employee in all_records:
    count[employee] = count.get(employee, 0) + 1
for key, value in count.items():
    print(f"{key}一周出勤了:{value}天")

#5.列表推导式找出出勤天数>=4的员工
attendance_list = {key : value for key, value in count.items() if value>=4}
print(attendance_list)

#6.找出只来了两天的员工姓名
attendance_list2 = {key : value for key, value in count.items() if value == 2}
print(attendance_list2)