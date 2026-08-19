#个人信息卡片
def create_profile(name:str = '未填写',age:int = 0,city:str = '未知',job:str = '待业',hobby:str = '无',**kwargs)->dict[str,str|int]:
    # person_info = {
    #     'name':name,
    #     'age':age,
    #     'city':city,
    #     'job':job,
    #     'hobby':hobby,
    # }
    # for key,value in kwargs.items():
    #     person_info.update({key:value})
    # return person_info
    person_list = []
    person_list.append("=====个人信息卡=====")
    person_list.append(f"姓名{name}")
    person_list.append(f"年龄{age}")
    person_list.append(f"城市{city}")
    person_list.append(f"职业{job}")
    person_list.append(f"爱好{hobby}")

    if kwargs:
        person_list.append("-----其他信息-----")
        for k,v in kwargs.items():
            person_list.append(f"{k}:{v}")
    text = "\n".join(person_list)
    return text

card1 = create_profile("张三", 25, "北京", "程序员", "篮球", phone="138xxxx", email="abc@test.com")
print(card1)
card2 = create_profile("李四", city="上海", hobby="摄影")
print(card2)
