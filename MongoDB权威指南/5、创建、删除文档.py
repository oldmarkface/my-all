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


def batch_insert():
    """批量插入"""
    post = [
        {
            "title": "1",
        },
        {
            "title": "1",
        },
    ]
    # 下面的x为数据插入后的ObjectId
    x = db.blog.insert_many(post)
    print(type(x))


def remove():
    """删除所有"""
    result = db.blog.remove()
    print(result)


def remove_some():
    """根据条件删除数据"""
    # 数据格式要对应
    # result = db.blog.remove({'title': 1})
    result = db.blog.remove({'title': '1'})
    print(result)


def drop_pk_remove():
    """drop 与 remove删除所用时间对比"""

    for x in range(10000):
        # 插入一万数据
        db.test_insert.insert({'index': x})

    start_time = datetime.datetime.now()
    db.test_insert.drop()
    end_time = datetime.datetime.now()
    print('drop用时', (end_time - start_time).microseconds)

    for x in range(10000):
        # 插入一万数据
        db.test_insert.insert({'index': x})

    start_time = datetime.datetime.now()
    db.test_insert.remove()
    end_time = datetime.datetime.now()
    print('remove用时', (end_time - start_time).microseconds)


if __name__ == '__main__':
    # 创建测试
    insert()
    # 批量创建
    batch_insert()
    # 清空
    # remove()
    # 按照条件删除
    remove_some()
    # 删除速度测试
    drop_pk_remove()
