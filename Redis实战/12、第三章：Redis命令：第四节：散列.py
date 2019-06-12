import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def test_easy():
    r.delete('key')
    # hmset key-name key value [key value ...]
    # 为散列里面的一个或多个键设置值
    print(r.hmset('key',{'name':'mark','age':18}))


    # hmget key-name key [key ...]
    # 从散列里面获取一个或多个键的值
    print(r.hmget('key','name'))

    # hdel key-name key [key ...]
    # 删除散列里面的一个或多个键值对，返回成功找到并删除的键值对数量。
    print(r.hdel('key','name'))

    # hlen key-name
    # 返回散列包含的键值对数量。
    print(r.hlen('key'))

def test_other():
    r.delete('key')

    print(r.hmset('key',{'name':'mark','age':18}))

    # hexists key-name key
    # 检查给定键是否存在于散列中
    print(r.hexists('key','name'))

    # hkeys key-name
    # 获取散列包含的所有键
    print(r.hkeys('key'))

    # hvals key-name
    # 获取散列包含的所有值
    print(r.hvals('key'))

    # hgetall key-name
    # 获取散列包含的所有键值对
    print(r.hgetall('key'))

    # hincrby key-name key increment
    # 将键key存储的值加上整数increment
    print(r.hincrby('key','age',2))
    print(r.hgetall('key'))

    # hincrbyfloat key-name key increment
    # 将键key存储的值加上浮点数increment
    print(r.hincrbyfloat('key','age',3.1))
    print(r.hgetall('key'))







if __name__ == '__main__':
    test_easy()

    test_other()
