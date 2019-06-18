from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database

def limit_skip_sort():
    db.limit_skip_sort.insert_many([
        {'name':'n1','age':18},
        {'name':'n2','age':22},
        {'name':'n3','age':19},
        {'name':'n4','age':23},
        {'name':'n5','age':20},
        {'name':'n6','age':27},
        {'name':'n7','age':21},
        {'name':'n8','age':25},
        {'name':'n9','age':26},
        {'name':'n10','age':24},
    ])

    users=db.limit_skip_sort.find().limit(3).skip(3).sort('age',-1)
    for user in users:
        print(user)

    # 为了方便多次测试，删除不用的数据
    db.limit_skip_sort.drop()

if __name__ == '__main__':
    limit_skip_sort()