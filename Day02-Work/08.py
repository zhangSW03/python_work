#循环语句
#1.打印等腰三角形
# n = int(input("输入直角边边长："))
#
# if n<=0 or n<=1:
#     print("构不成三角形")
# else:
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="\t")
#         print( )


#2.打印对应数字的金字塔
# n = int(input())
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#3.打印国际象棋棋盘
# 奇数行黑色在前 偶数行白色在前 8个格子 4个黑4个白
# 奇数列黑色在前 偶数列白色在前
for i in range(1,9):
    for j in range(1,9):
        if (j+i)%2==0:
            print("■",end=" ")
        else:
            print("□",end=" ")
    print()
