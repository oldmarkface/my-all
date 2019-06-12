import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database


def insert():
    """创建测试"""
    post = {
        "name": "joe",
        "friends": 32,
        "enemies": 2
    }
    # 下面的x为数据插入后的ObjectId
    x = db.blog.insert_one(post)
    print(type(x))


def test_update():
    # 创建测试
    insert()
    # 查找数据
    joe = db.blog.find_one({'name': 'joe'})
    print('更新前', joe)
    _id = joe['_id']
    joe['relationships'] = {
        'friends': joe['friends'],
        'enemies': joe['enemies']
    }
    del joe['friends']
    del joe['enemies']

    # 更新数据
    db.blog.update({'_id': _id}, joe)

    # 查找数据
    joe = db.blog.find_one({'name': 'joe'})
    print('更新后', joe)

    # 为了方便多次测试，删除数据
    db.blog.drop()


def test_inc():
    """inc实现网站浏览次数原子更新"""
    web = {
        'url': 'http://www.baidu.com',
    }
    db.web.insert_one(web)
    result = db.web.find_one()
    print('修改前', result)
    db.web.update_one({'url': 'http://www.baidu.com'},
                      {'$inc': {'pageviews': 1}})
    result = db.web.find_one()
    print('修改后(不存在就创建)', result)

    db.web.update_one({'url': 'http://www.baidu.com'},
                      {'$inc': {'pageviews': 1}})
    result = db.web.find_one()
    print('修改后(存在就更新)', result)

    # 为了方便多次测试，删除本次数据
    db.web.drop()


def test_set():
    # "$set"用来指定一个字段的值。如果这个字段不存在，则创建它。
    # 这对更新模式或者增加用户定义的键来说非常方便。
    user = {
        'name': 'mark',
        'home': {
            'city': '北京',
            'door': '101'
        }
    }
    db.test_set.insert_one(user)
    user = db.test_set.find_one()

    print('修改前', user)

    db.test_set.update_one({'name': 'mark'},
                           {'$set':
                                {'books': 'MongoDB'}
                            })
    user = db.test_set.find_one()
    print('修改后(插入)', user)

    db.test_set.update_one({'name': 'mark'},
                           {'$set':
                                {'books': 'Redis'}
                            })
    user = db.test_set.find_one()
    print('修改后(修改内容)', user)

    db.test_set.update_one({'name': 'mark'},
                           {'$set':
                                {'home.door': '102'}
                            })
    user = db.test_set.find_one()
    print('修改后(修改嵌套文本)', user)

    db.test_set.update_one({'name': 'mark'},
                           {'$set':
                                {'books': ['Redis', 'mongodb']}
                            })
    user = db.test_set.find_one()
    print('修改后(修改列席)', user)

    db.test_set.update_one({'name': 'mark'},
                           {'$unset':
                                {'books': 1}
                            })
    user = db.test_set.find_one()
    print('删除修改后', user)

    # 为了方便多次测试，删除本次数据
    db.test_set.drop()


def test_push():
    # 如果数组已经存在，"$push"会向已有的数组末尾加入一个元素，要是没有就创建一个新的数组
    user = {
        'name': 'mark'
    }
    db.test_push.insert_one(user)
    user = db.test_push.find_one()
    print('push前', user)

    db.test_push.update_one({'name': 'mark'},
                            {'$push': {'books': {'title': 'redis', 'price': 1}}})

    user = db.test_push.find_one()
    print('push后（没有就插入）', user)

    db.test_push.update_one({'name': 'mark'},
                            {'$push': {'books': {'title': 'mongodb', 'price': 2}}})
    user = db.test_push.find_one()
    print('push后（有就插入）', user)

    db.test_push.update_one({'name': 'mark'},
                            {'$push':
                                 {'books':
                                      {'$each': [{'title': 'python2', 'price': 3},
                                                 {'title': 'python3', 'price': 4}
                                                 ]}
                                  }
                             })

    user = db.test_push.find_one()
    print('push后（each）', user)

    db.test_push.update_one({'name': 'mark'},
                            {'$push':
                                {'books':
                                    {'$each': [
                                        {'title': 'vue', 'price': 2},
                                        {'title': 'react', 'price': 5}
                                    ],
                                        '$slice': -3
                                    }
                                }
                            })

    user = db.test_push.find_one()
    print('push后（each-slice）', user)

    db.test_push.update_one({'name': 'mark'},
                            {'$push':
                                {'books':
                                    {'$each': [
                                        {'title': 'html', 'price': 2},
                                        {'title': 'css', 'price': 1}
                                    ],
                                        '$slice': -3,
                                        '$sort': {'price': 1}
                                    }
                                }
                            })

    user = db.test_push.find_one()
    print('push后（each-slice-sort）', user)

    # 为了方便多次测试，删除本次数据
    db.test_push.drop()


def test_add_to_set():
    mark = {
        'name': 'mark',
        'books': ['redis']
    }

    db.test_set.insert_one(mark)

    mark = db.test_set.find_one({'name': 'mark'})
    print('修改前:', mark)

    db.test_set.update_one({'books':
                                {'$ne': 'redis'}
                            },
                           {
                               '$push':
                                   {
                                       'books': 'redis'
                                   }
                           }
                           )
    mark = db.test_set.find_one({'name': 'mark'})
    print('修改后(ne):', mark)

    db.test_set.update_one({'name': 'mark'},
                           {
                               '$addToSet': {'books': 'mongodb'}
                           }
                           )
    db.test_set.update_one({'name': 'mark'},
                           {
                               '$addToSet': {'books': 'redis'}
                           }
                           )
    mark = db.test_set.find_one({'name': 'mark'})
    print('修改后(addToSet):', mark)

    db.test_set.update_one({'name': 'mark'},
                           {
                               '$addToSet': {'books':
                                   {
                                       '$each': ['python2', 'python3', 'python2']
                                   }
                               }
                           }
                           )
    mark = db.test_set.find_one({'name': 'mark'})
    print('修改后(addToSet-each):', mark)

    # 为了方便多次测试，删除本次数据
    db.test_set.drop()


def test_pull():
    user = {
        'name': 'mark',
        'books': ['vue', 'react', 'python2', 'python3', 'html', 'python2']
    }
    db.test_set.insert_one(user)

    user = db.test_set.find_one()
    print('修改前', user)

    db.test_set.update_one({'name': 'mark'},
                           {
                               '$pull': {'books': 'python2'}
                           }
                           )
    user = db.test_set.find_one()
    print('修改后', user)

    # 为了方便多次测试，删除本次数据
    db.test_set.drop()


def update_from_location():
    # 若是数组有多个值，而我们只想对其中的一部分进行操作，就需要一些技巧。
    # 有两种方法操作数组中的值：通过位置或者定位操作符（"$"）。
    user = {
        'name': 'mark',
        'books': [
            {'title': 'python2', 'price': 1},
            {'title': 'python3', 'price': 1},
            {'title': 'redis', 'price': 1},
            {'title': 'python3', 'price': 1},

        ]
    }
    db.test_set.insert_one(user)

    user = db.test_set.find_one()
    print('修改前', user)

    db.test_set.update_one({'name': 'mark'},
                           {'$inc': {'books.1.price': 1}
                            }
                           )

    user = db.test_set.find_one()
    print('修改后（根据坐标）', user)

    db.test_set.update_one({'books.title': 'python3'},
                           {'$inc': {'books.$.price': 1}
                            }
                           )

    user = db.test_set.find_one()
    print('修改后（根据$）', user)

    # 为了方便多次测试，删除本次数据
    db.test_set.drop()


def inc_pk_push():
    # inc速度与push速度对比

    user={
        'name':'mark',
        'money':1
    }
    db.test_push.insert_one(user)

    start_time=datetime.datetime.now()
    for i in range(10000):
        db.test_push.update_one({'name':'mark'},
                                {'$inc':{'money':1}}
                                )
    end_time=datetime.datetime.now()
    print('inc耗时',(end_time-start_time).microseconds)

    # 为了方便多次测试，删除本次数据
    db.test_push.drop()

    user = {
        'name': 'mark',
        'number': []
    }
    db.test_push.insert_one(user)
    start_time = datetime.datetime.now()
    for i in range(10000):
        db.test_push.update_one({'name': 'mark'},
                                {'$push': {'number': 1}}
                                )
    end_time = datetime.datetime.now()
    print('push耗时', (end_time - start_time).microseconds)
    # 为了方便多次测试，删除本次数据
    db.test_push.drop()







if __name__ == '__main__':
    # 简单update测试
    test_update()
    # "$inc"修改器用来增加已有键的值，或者该键不存在那就创建一个。
    # 网站浏览次数原子更新
    test_inc()
    # "$set"用来指定一个字段的值。如果这个字段不存在，则创建它。
    # 这对更新模式或者增加用户定义的键来说非常方便。
    test_set()
    # 如果数组已经存在，"$push"会向已有的数组末尾加入一个元素，要是没有就创建一个新的数组
    test_push()

    test_add_to_set()

    test_pull()

    update_from_location()

    # inc_pk_push()

