#1.定义函数 返回对应的等级
# def fun_level(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
#
# test_scores_1 = [95, 80, 65, 50, 90, 75, 60, 59, 100, 0]
# for s in test_scores_1:
#     print(f"分数: {s:>4} -> 等级: {fun_level(s)}")
#
# print()


#2.判断回文串，返回bool值
# def palindrome_str(str)->bool:
#     if str[::-1] == str:
#         return True
#     else:
#         return False
#
# test_strs = ["level", "radar", "黄山落叶松叶落山黄", "hello", "abcba", "ab", ""]
# for s in test_strs:
#     print(f"'{s}' 是回文串吗? {palindrome_str(s)}")
#
# print()

#3.完成时间转换功能
# def time_fun(time):
#     hour = time // 3600
#     minute = time % 3600 // 60
#     second = time % 60 % 60
#     return hour, minute, second
# test_seconds = [0, 59, 60, 61, 3600, 3661, 7322, 86400, 90061]
# for t in test_seconds:
#     h, m, s = time_fun(t)
#     print(f"{t:>6} 秒 = {h} 小时 {m} 分钟 {s} 秒")
#
# print()

#4.判断三角形的类型
# def triangle_type(a,b,c):
#     if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
#         print("不能构成三角形")
#         return False
#     else:
#         if a == b == c:
#             print("这是等边三角形")
#         elif a==b or b==c or c==a:
#             print("这是等腰三角形")
#         else:
#             print("这是普通三角形")
#         return True
#
# test_triangles = [
#     (3, 3, 3),    # 等边
#     (3, 3, 5),    # 等腰
#     (3, 4, 5),    # 普通
#     (1, 2, 3),    # 不能构成（1+2 = 3）
#     (5, 1, 1),    # 不能构成（1+1 < 5）
#     (0, 1, 1),    # 边长为 0
#     (-1, 2, 2),   # 边长为负数
#     (7, 7, 7),    # 等边
#     (5, 5, 8),    # 等腰
# ]
# for a, b, c in test_triangles:
#     print(f"三边: ({a}, {b}, {c}) -> {triangle_type(a, b, c)}")

#5.商品系统计算总金额
#三个参数 信息 优惠 运费信息
def count_cost(*args,points=0,coupon=0,fee=0):
    price = [items[1] * items[2] for items in args]
    total_price = sum(price)

    if total_price >= 5000 and coupon <= total_price:
        total_price -= coupon

    if total_price >= 5000:
        total_price -= points//100

    total_price += fee
    return total_price

total = count_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1))
print(total)






