import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database


def insert():
    """创建测试"""
    post = {
        "title": "My Blog Post",
        "content": "Here's my blog post.",
        "date": datetime.datetime.now()
    }
    # 下面的x为数据插入后的ObjectId
    x = db.blog.insert_one(post)
    print(type(x))


def find():
    """查询所有"""
    result = db.blog.find()
    for item in result:
        print(item)


def find_one():
    """查询单条数据"""
    result = db.blog.find_one()
    print("find_one:", result)


def update_many():
    db.blog.update_many({'title': 'My Blog Post'}, {'$set': {'content': 'updated'}})
    result = db.blog.find()
    for item in result:
        print('更新后：', item)


def delete_one():
    db.blog.delete_one({'title': 'My Blog Post'})
    result = db.blog.find()
    for item in result:
        print('删除后：', item)


if __name__ == '__main__':
    # 插入测试
    insert()
    insert()
    # 查询所有
    find()
    # 查询单个
    find_one()
    # 更新
    update_many()
    # 删除一个
    delete_one()
