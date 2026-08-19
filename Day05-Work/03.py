#成绩统计分析器

def analyze_scores(*args:float, **kwargs:int)->dict[str,int|str]:
    stu_info = {}
    stu_sore = list(args)
    round_ndigits:int = kwargs.get("round_ndigits", 1)
    show_detail:bool = kwargs.get("show_detail", False)
    pass_line:float = kwargs.get("pass_line", 60)

    if not args:
        return {"count": 0, "max_score": 0, "min_score": 0, "avg_score": 0, "pass_rate": "0%"}

    count:int = len(stu_sore)
    max_score:float = max(stu_sore)
    min_score:float = min(stu_sore)
    avg_score:float = round(sum(stu_sore)/count, round_ndigits)
    pass_stu:int = 0

    for scor in stu_sore:
        if scor >= pass_line:
            pass_stu += 1

    pass_rate:str=f"{round(pass_stu/count * 100,round_ndigits)}%"

    stu_info={"count":count,"max_score":max_score,"min_score":min_score,"avg_score":avg_score,"pass_rate":pass_rate}

    if show_detail:
        print("=======成绩统计=======")
        print(f"总人数是:{stu_info['count']},最高分是:{stu_info['max_score']},最低分:{stu_info['min_score']},平均分是:{stu_info['avg_score']},及格率是:{stu_info['pass_rate']}")

    return stu_info

analyze_scores(85,92,78,89,95,88,76,90, round_ndigits=2, show_detail=True)
res=analyze_scores(45,55,38,62,70,59, pass_line=60, round_ndigits=1)
print(res)