import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def test_easy():
    r.delete('key')
    # zadd key-name score memeber [score member ...]
    # 将带有给定分值的成员添加到有序集合里面
    print(r.zadd('key', {'a': 1, 'b': 2, 'c': 3}))

    # zrem key-name member [member ...]
    # 从有序集合里面移除给定的成员，并返回被移除成员的数量
    print(r.zrem('key', 'a'))

    # zcard key-name
    # 返回有序集合包含的成员数量
    print(r.zcard('key'))

    # zincrby key-name increment member
    # 将merber成员的分值加上increment
    # pyredis的Bug，下面name和value顺序反了
    print(r.zincrby('key', 3, 'b'))

    # zcount key-name min max
    # 返回分值介于min和max之间的成员数量
    print(r.zcount('key',4,6))

    # zrank key-name member
    # 返回成员member有序集合中的排名。
    print(r.zrank('key','b'))

    # zsore key-name member
    # 返回成员member的分值
    print(r.zscore('key','b'))

    #zrange key-name start stop [WITHSCORES]
    # 返回有序集合中排名介于start和stop之间的成员，如果给定了可选的WITHSCORES选项，那么命令会将成员的分值也一并返回。
    print(r.zrangebyscore('key',1,4))
    print(r.zrangebyscore('key',1,4,withscores=True))


def test_other():
    r.delete('key')

    print(r.zadd('key',{'a': 1, 'b': 2, 'c': 3}))
    # zrevrank key-name merber
    # 返回有序集合里面成员member的排名，成员按照分值从大到小排列
    print(r.zrevrank('key','a'))

    # zrevrange key-name start stop [WITHSCORES]
    # 返回有序集合给定排名范围内的成员，成员按照分值从大到小排列
    print(r.zrevrange('key',1,2))

    # zrangebyscore by min max [WITHSCORES] [LIMIT offset count]
    # 获取有序集合中分值介于min和max之间的所有成员，并按照分值从大到小的顺序来返回它们。
    print(r.zrevrangebyscore('key',2,1))

    # zremrangebyrank key-name start stop
    # 移除有序集合中排名介于start和stop之间的所有成员。
    print(r.zremrangebyrank('key',1,2))

    # zremrangebyscore key-name min max
    # 移除有序集合中分值介于min和max之间的所有成员。
    print(r.zremrangebyscore('key',1,2))




if __name__ == '__main__':
    test_easy()
