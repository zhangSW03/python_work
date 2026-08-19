#集合推导式 多集合操作
# 书法组
calligraphy_set = {"王林", "曾牛", "天运子", "韩立", "厉飞雨", "紫灵", "徐立国"}
# 绘画组
painting_set    = {"张铁", "王林", "曾牛", "王蝉", "韩立", "厉飞雨", "云露", "李化元"}
# 音乐组
music_set       = {"许木", "红蝶", "韩立", "天运子", "厉飞雨", "曾牛", "虎咆"}
# 体育组
sports_set      = {"遁天", "天运子", "韩立", "姜老道", "紫灵", "云露", "虎咆"}

# 1
same_stu = calligraphy_set & painting_set & music_set & sports_set
print(same_stu)
# 02
nosame_stu = calligraphy_set - painting_set - music_set
print(nosame_stu)
# 03
new_set1 = {stu for stu in calligraphy_set if stu in calligraphy_set and stu not in sports_set}
print(new_set1)
# 04
new_set2 = calligraphy_set | painting_set | music_set | sports_set
print(f'参赛的学生名单是：{new_set2}')
print(f'参赛学生共{len(new_set2)}人')
# 05
new_list = [*calligraphy_set, *painting_set, *music_set, *sports_set]
new_set3 = set(new_list)
for stu in new_set3:
    count = new_list.count(stu)
    print(f"   {stu} 参加了 {count} 个小组")