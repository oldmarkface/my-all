import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def test_easy():
    r.delete('key')

    # sadd key-name item [item ...]
    # 将一个或多个元素添加到集合里面，并返回被添加元素当中原本并不存在于集合里面的元素数量
    print(r.sadd('key', '1'))
    print(r.sadd('key', '2'))
    print(r.sadd('key', '1', '2', '3', '4'))

    # smembers key-name
    # 返回集合包含的所有元素
    print(r.smembers('key'))

    # srem key-name item [item ...]
    # 从集合里面移除一个或多个元素，并返回被移除元素的数量
    print(r.srem('key', '1', '3'))

    # smembers key-name
    # 返回集合包含的所有元素
    print(r.smembers('key'))

    # sismember key-name item
    # 检查元素item是否存在于集合key-name里
    print(r.sismember('key', '1'))
    print(r.sismember('key', '4'))

    # scard key-name
    # 返回集合包含的元素的数量
    print(r.scard('key'))

    # srandmember key-name [count]
    # 从集合里面随机地返回一个或多个元素。当count为正数时，命令返回的随机元素不会重复；
    # 当count为负数时，命令返回的随机元素可能会出现重复。
    print(r.sadd('key', '1', '2', '3', '4'))
    print(r.srandmember('key', 2))
    print(r.srandmember('key', -1))

    # spop key-name
    # 随机地移除集合中的一个元素，并返回被移除的元素。
    print(r.spop('key'))

    # smembers key-name
    # 返回集合包含的所有元素
    print(r.smembers('key'))

    # smove source-key dest-key item
    # 如果集合source-key包含元素item，那么从集合source-key里面移除元素item，
    # 并将元素item添加到集合dest-key中；如果item被成功移除，那么命令返回1，否则返回0

    print(r.delete('key'))
    print(r.delete('key2'))

    print(r.sadd('key', '1', '2', '3'))
    print(r.smove('key', 'key2', '2'))

    print(r.smembers('key'))
    print(r.smembers('key2'))


def test_others():
    r.delete('key')
    r.delete('key2')
    r.delete('key3')

    r.sadd('key', '1', '2', '3', '4')
    r.sadd('key2', '2', '3','5')

    # sdiff key-name [key-name ...]
    # 返回那些存在于第一个集合、但不存在于其它集合中的元素（数学上的差集运算）
    print(r.sdiff('key', 'key2'))

    # sdiffstore dest-key key-name [key-name ...]
    # 将那些存在于第一个集合但不存在于其他集合中的元素（数学上的差集运算）存储到dest-key键里面
    print(r.sdiffstore('key3','key','key2'))
    print('key',r.smembers('key'))
    print('key2',r.smembers('key2'))
    print('key3',r.smembers('key3'))

    # sinter key-name [key-name ...]
    # 返回那些同时存在于所有集合中的元素（数学上的交集运算）
    print(r.sinter('key','key2'))

    r.delete('key3')
    #sinterstore dest-key key-name [key-name ...]
    #将那些同时存在于所有集合的元素（数学上的交集运算）存储到dest-key键里面
    print(r.sinterstore('key3','key','key2'))
    print('key', r.smembers('key'))
    print('key2', r.smembers('key2'))
    print('key3', r.smembers('key3'))

    # sunion key-name [key-name ...]
    # 返回那些至少存在于一个集合中的元素（数学上的并集计算）
    print(r.sunion('key','key2'))

    # sunionstore dest-key key-name [key-name ...]
    # 将那些至少存在于一个集合中的元素（数学上的并集计算）存储到dest-key键里面
    r.delete('key3')
    print(r.sunionstore('key3','key','key2'))

    print('key', r.smembers('key'))
    print('key2', r.smembers('key2'))
    print('key3', r.smembers('key3'))






    pass


if __name__ == '__main__':
    test_easy()
    test_others()
