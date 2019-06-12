import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database


def test_find():
    user = {
        'name': 'mark',
        'age': 18
    }
    db.find.insert_one(user)

    user = db.find.find_one()
    print(user)
    user = db.find.find_one({}, {'age': 0})
    print(user)

    # 为了方便多次测试，删除数据
    db.find.drop()


if __name__ == '__main__':
    test_find()
