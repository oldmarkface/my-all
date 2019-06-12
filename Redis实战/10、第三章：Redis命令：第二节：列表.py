import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def test_easy():
    r.delete('key')

    print(r.rpush('key', 'mark'))

    print(r.lrange('key', 0, -1))

    print(r.rpush('key', 'face'))

    print(r.lrange('key', 0, -1))

    print(r.lpush('key', 'love'))

    print(r.lrange('key', 0, -1))

    print(r.lpop('key'))

    print(r.rpop('key'))

    print(r.lrange('key', 0, -1))

    # 插入多个值
    print(r.rpush('key', 'love', 'face'))

    print(r.lrange('key', 0, -1))

    print(r.ltrim('key', 1, -1))
    print(r.lrange('key', 0, -1))


def test_pop():
    r.delete('key')
    r.delete('key2')

    print(r.rpush('key', '1', '2', '3'))

    # 从第一个非空列表中弹出位于最左端的元素，或者在timeout秒之内阻塞并等待可弹出的元素出现。
    print(r.blpop('key'))
    print(r.lrange('key', 0, -1))

    # 从第一个非空列表中弹出位于最右端的元素，或者在timeout秒之内阻塞并等待可弹出的元素出现。
    print(r.brpop('key'))
    print(r.lrange('key', 0, -1))

    r.delete('key')
    r.delete('key2')
    print(r.rpush('key', '1', '2', '3'))

    # rpoplpush source-key dest-key
    # 从source-key列表中弹出位于最右端的元素，然后将这个元素推入dest-key列表的最左端，并向用户返回这个元素。
    print(r.rpoplpush('key','key2'))

    print(r.lrange('key',0,-1))
    print(r.lrange('key2',0,-1))

    # brpoplpush source-key dest-key timeout
    # 从source-key列表中弹出位于最右端的元素，然后将这个元素推入dest-key列表的最左端，并向用户返回这个元素；
    # 如果source-key为空，那么在timeout秒之内阻塞并等待可弹出的元素出现。




if __name__ == '__main__':
    test_easy()
    test_pop()
