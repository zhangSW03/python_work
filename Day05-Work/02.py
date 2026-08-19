def filter_data(*args:int,**kwargs: int|bool|str)->list[int]:
    threshold = kwargs.get("threshold")
    top_n = kwargs.get("top_n")
    unique = kwargs.get("unique", False)
    sort_order = kwargs.get("sort_order","asc")

    data_list = list(args)

    if threshold is not None:
        data_list = [i for i in data_list if i>= threshold]

    if unique:
        data_list = list(set(data_list))

    if top_n is not None:
        data_list = data_list[:top_n]

    data_list.sort(reverse = (sort_order == "desc"))

    return data_list


res=filter_data(5,2,9,1,7,3,8,2,9,4, threshold=5, unique=True,sort_order="desc")
print(res)
#       → [9, 8, 7, 5]

