#学生管理系统模拟
students = (
    ("S001", "王林", {"语文", "数学", "英语", "历史"}),
    ("S002", "李慕婉", {"数学", "物理"}),
    ("S003", "司徒南", {"语文", "英语", "历史"}),
    ("S004", "柳眉", {"数学", "英语", "物理"}),
    ("S005", "周佚", {"语文", "数学", "化学", "历史"}),
    ("S006", "清水仙君", {"语文", "数学", "AI", "日语"}),
    ("S007", "红蝶", {"英语", "数学", "日语"}),
    ("S008", "徐立国", {"语文", "英语", "历史"}),
    ("S009", "许立国", {"语文", "历史", "AI"}),
    ("S010", "藤化元", {"语文", "英语", "化学", "韩语"})
)
hot_courses = {"数学", "英语", "物理"}

# 1
for stu in students:
    id = stu[0]
    name = stu[1]
    class_name = stu[2]
    print(f"学生的学号：{id},姓名：{name},所选的课程有{class_name}")

# 2
all_courses = set()
for stu in students:
    class_name = stu[2]
    all_courses.update(class_name)
print(all_courses)

# 3
for stu in students:
    name = stu[1]
    class_name = stu[2]
    print(f"{name}同学选修了{class_name}课程，总学分是{len(class_name) * 3}")

# 4
for stu in students:
    class_name = stu[2]
    name = stu[1]
    select = class_name&hot_courses
    if len(select) >= 2:
        print(name)
print("====================================")
# 5
for stu in students:
    name = stu[1]
    class_name = stu[2]
    if "数学" in class_name and "物理" not in class_name:
        print(name)

