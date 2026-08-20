
from fastapi import FastAPI
from pydantic import BaseModel

book_management = FastAPI(title="图书信息查询系统",description="一个简单的图书馆图书信息查询API",version="1.0")

class Book(BaseModel):
    id: int
    name: str
    author:str
    price: float
    stock:int

book_list = [
    Book(id = 1,name = "西游记",author="吴承恩",price=19.99,stock=6),
    Book(id = 2,name = "水浒传",author="施耐庵",price=18.90,stock=5),
    Book(id = 3,name = "红楼梦",author="曹雪芹",price=20.00,stock=2),
    Book(id = 4,name = "三国演义",author="罗贯中",price=16.31,stock=10)
]

@book_management.get("/")
def welcome_management():
    print("欢迎使用图书信息查询系统!")
    return {"message":"欢迎使用图书信息查询系统!"}

@book_management.get("/books",summary="获取所有图书列表",response_model=list[Book])
def get_books():
    print("获取图书中...")
    return book_list

@book_management.get("/books/count",summary="获取图书总数")
def total_books():
    print("获取图书总数...")
    return {"total":len(book_list)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(book_management,host="0.0.0.0",port=8000)




