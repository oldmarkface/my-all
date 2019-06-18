from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database

def find_null():
    mark={
        'name':'mark',
        'sex':None
    }

    face={
        'name':'face',
    }

    db.find_null.insert_one(mark)
    db.find_null.insert_one(face)

    users=db.find_null.find({'sex':None})
    for user in users:
        print(user)

    print('*'*30)

    users=db.find_null.find({'sex':{'$in':[None],'$exists':True}})
    for user in users:
        print(user)

    #为了方便多次测试，删除本次数据
    db.find_null.drop()

def all_test():
    user1={
        'name':['mark','face','xx']
    }
    user2={
        'name':['mark','aaa','bbb']
    }

    db.find_null.insert_many([user1,user2])
    # 使用正则表达式执行不区分大小写的匹配
    users=db.find_null.find({'name':'mark'})
    for user in users:
        print('-1-',user)

    print('*' * 30)

    users=db.find_null.find({'name':{'$all':['mark','face']}})
    for user in users:
        print('-2-',user)

    print('*' * 30)

    users=db.find_null.find({'name':['mark','face','xx']})
    for user in users:
        print('-3-',user)

    print('*' * 30)

    users = db.find_null.find({'name': ['mark', 'face']})
    for user in users:
        print('-4-', user)

    print('*' * 30)

    users = db.find_null.find({'name': [ 'face','mark', 'xx']})
    for user in users:
        print('-5-', user)

    print('*' * 30)

    users = db.find_null.find({'name.1': 'face'})
    for user in users:
        print('-6-', user)

    # 为了方便多次测试，删除本次数据
    db.find_null.drop()

def slice_test():
    user={
        'name':['mark','face','xx']
    }
    db.find_null.insert_one(user)

    user=db.find_null.find_one({},{'name':{'$slice':2}})
    print(user)
    user = db.find_null.find_one({}, {'name': {'$slice': -2}})
    print(user)
    user = db.find_null.find_one({}, {'name': {'$slice': [1,1]}})
    print(user)

    # 为了方便多次测试，删除本次数据
    db.find_null.drop()


    books={
        'name':'mark',
        'comments':[
            {'value':1,'pageview':11},
            {'value':2,'pageview':12},
            {'value':2,'pageview':13},
            {'value':3,'pageview':14},
        ]
    }
    db.find_null.insert_one(books)

    books=db.find_null.find({'comments.value':2},{'comments.$':1})
    for book in books:
        print(book)

    # 为了方便多次测试，删除本次数据
    db.find_null.drop()

def range_find():
    # 范围查询
    db.find_null.insert_many([
        {'x':1},
        {'x':3},
        {'x':9},
        {'x':[2,5]},
    ])

    results=db.find_null.find({'x':{'$gt':2,'$lt':6}})
    for result in results:
        print('-result1-',result)

    print('*' * 30)

    results = db.find_null.find({'x': {'$elemMatch':{'$gt': 2, '$lt': 6}}})
    for result in results:
        print('-result2-',result)

    print('*' * 30)

    # 为了方便多次测试，删除本次数据
    db.find_null.drop()

def where_test():
    db.find_null.insert_many([
        {'name':'mark','age':19,'love':'face'},
        {'name':'face','age':19,'love':'face'},
    ])
    func="""
    function(){
        for(var current in this){
            for(var other in this){
                if(current!=other && this[current]==this[other]){
                    return true;
                }
            }
        }
        return false;
    };
    """
    results=db.find_null.find({'$where':func})
    for result in results:
        print(result)



    # 为了方便多次测试，删除本次数据
    db.find_null.drop()


if __name__ == '__main__':
    find_null()
    print('*'*40)
    all_test()
    print('*' * 40)
    slice_test()
    print('*' * 40)
    range_find()
    print('*' * 40)
    where_test()