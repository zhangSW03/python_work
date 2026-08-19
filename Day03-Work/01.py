# #01-合并列表 去重排序
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# #合并
# list4 = list(list1 + list2 + list3)
# #去重
# new_list = list(set(list4))
# new_list.sort()
# print(new_list)

# #02-将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# # list2 = []
# # for i in list1:
# #     if i%3==0 and i%5==0:
# #         list2.append(i**2)
# list2 = [num**2 for num in list1 if num%3==0 and num%5==0]
#
# print(list2)

#03-将如下列表中的正数提取出来，封装为一个新的列表。
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
#
# list2 = [num for num in list1 if num > 0]
# list2.sort()
# print(list2)
#

#04-输入一个字符串, 判断该字符串是否是回文(两边对称)
# str = input()
# new_str = str[::-1]
# if str == new_str:
#     print(f'你输入的字符串{str}是回文')

#05-将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容，遍历输出出来
list = []
for a in range(1,11):
    s = input("请输入一个字符:")
    list.append(s[::-1].upper())
print(list)

#06-现有两个变量，分别为：a = 10， b = 20，现需要将这两个变量值交换，然后输出到控制台。
# a = 10
# b = 20
# a,b=b,a
# print(a,b)

#07-现有三个变量，分别为：a=100，b = 200，c = 300，现需要将这三个变量值进行交换，将 a,b,c 的值分别赋值给 c,a,b，并将其输出到控制台。

a = 100
b = 200
c = 300

a , b ,c = b,c, a
print(a, b, c)