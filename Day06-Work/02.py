#电影信息管理系统
class Movie:
    def __init__(self,name,director,actor,price,score):
        self.name = name
        self.director = director
        self.actor = actor
        self.price = price
        self.score = score
    def __repr__(self):
        return f"电影名:{self.name} | 导演:{self.director} | 主演:{self.actor} | 票价:{self.price} | 评分:{self.score}"

class MovieSystem:
    SYSTEM_NAME = "电影信息管理系统"
    SYSTEM_VERSION = "1.0.0"
    def __init__(self):
        self.movie_dict = {}

    def add_movie(self):
        movie_name = input("请输入你要添加的电影名:")
        if movie_name in self.movie_dict:
            print("你输入的电影已经存在,请重新输入")
            return

        movie_director = input("请输入电影的导演:")
        movie_actor = input("请输入电影的主演:")
        movie_price = float(input("请输入电影的票价:"))
        movie_score = float(input("请输入电影的评分:"))
        if movie_price > 0 and 0 <= movie_score <= 10:
            self.movie_dict[movie_name] = Movie(movie_name,movie_director,movie_actor,movie_price,movie_score)
            print("添加成功!!!")
        else:
            print("你输入的票价或评分不符合要求!!!")
            return
    def update_movie(self):
        movie_name = input("请输入要修改的电影名:")
        movie = self.movie_dict.get(movie_name)
        if movie is None:
            print("未找到该电影")
            return
        print(f"当前信息:{movie}")
        movie_director = input("请输入要修改的电影导演:")
        movie_actor = input("请输入要修改的电影主演:")
        movie_price = float(input("请输入要修改的电影票价:"))
        movie_score = float(input("请输入要修改的电影评分:"))
        if movie_price > 0 and 0 <= movie_score <= 10:
            movie.director = movie_director
            movie.actor = movie_actor
            movie.price = movie_price
            movie.score = movie_score
            print("电影信息修改成功")
        else:
            print("你输入的票价或评分不符合要求")
            return

    def delete_movie(self):
        movie_name = input("请输入你要删除的电影名:")
        if movie_name not in self.movie_dict:
            print("未找到该电影")
            return
        else:
            del self.movie_dict[movie_name]
            print("删除成功")

    def query_movie(self):
        movie_name = input("请输入你要查询的电影名:")
        movie = self.movie_dict.get(movie_name)
        if movie is None:
            print("未找到该电影")
            return
        print(f"电影信息:{movie}")

    def list_movie(self):
        if len(self.movie_dict) == 0:
            print("该系统中没有电影信息")
            return
        for m in self.movie_dict.values():
            print(m)

    def top_rated_movie(self):
        if len(self.movie_dict) == 0:
            print("系统中没有电影信息,查询不到评分最高的电影")
            return
        max_movie = [m.score for m in self.movie_dict.values()]
        max_score = max(max_movie)
        max_movie_info = [key for key, value in self.movie_dict.items() if value.score == max_score]
        print(f"评分最高的电影有:{len(max_movie_info)}部,最高的评分是:{max_score}")
        for m in max_movie_info:
            print(f"最高分的电影名:{m}")

    def run(self):
        print(f"# # # # # #{self.SYSTEM_NAME} # # # # # #")
        while True:
            print()
            print("1. 添加电影   2. 修改电影   3. 删除电影  4. 查询指定电影  5. 查询所有电影  6. 查询评分最高电影  7. 退出系统")
            print()
            choice = input("请输入你要进行的操作(1~7):")
            match choice:
                case "1":
                    self.add_movie()
                case "2":
                    self.update_movie()
                case "3":
                    self.delete_movie()
                case "4":
                    self.query_movie()
                case "5":
                    self.list_movie()
                case "6":
                    self.top_rated_movie()
                case "7":
                    print("退出系统")
                    break
                case _:
                    print("该系统没有此项操作")


if __name__ == "__main__":
    movie_system = MovieSystem()
    movie_system.run()


