import redis
import time,threading

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def sort_test():
    #  	soft source-key [by pattern] [limit offset count] \
    # [get pattern get pattern ...]] [asc/desc] [alph] [store dest-key]
    # 根据给定的选项，对输入列表、集合或者有序集合进行排序，然后返回或者存储排序的结果。

    r.delete('key')

    # 将一些数据放到列表里面
    print(r.rpush('key',23,25,110,7))
    # 根据数字大小排序
    print(r.sort('key'))
    # 根据字幕顺序排序
    print(r.sort('key',alpha=True))

    # 添加一些用于执行排序操作和获取操作的附加数据
    print(r.hset('d-23','field',9))
    print(r.hset('d-25','field',1))
    print(r.hset('d-110','field',3))
    print(r.hset('d-7','field',5))

    # 将散列的域（field）用作权重，对列表进行排序
    print(r.sort('key',by='d-*->field'))

    # 获取外部数据，并将它们用作命令的返回值，而不是返回被排序的数据
    print(r.sort('key',by='d-*->field',get='d-*->field'))

def no_multi_exec():
    # 对'number:'计数器执行自增操作并打印操作的执行结果
    print(r.incr('number:'))
    #等待100毫秒
    time.sleep(.1)
    #对'number:'执行自减操作
    print(r.decr('number:'))
    pass

def test1():
    r.delete('number:')
    # 不使用事务
    #启动三个线程执行没有被事务包裹的自增、休眠和自减操作
    for i in range(3):
        threading.Thread(target=no_multi_exec).start()



def multi_exec():
    # 使用事务
    # 创建一个事务型流水线对象
    pipeliner=r.pipeline()
    pipeliner.incr('number:')
    time.sleep(.1)
    pipeliner.incr('number:',-1)
    print(pipeliner.execute()[0])

def test2():
    r.delete('number:')
    for i in range(3):
        threading.Thread(target=multi_exec).start()

def time_to_live():
    # 过期时间测试

    r.delete('key')

    print(r.set('key','mark'))
    print(r.get('key'))

    # expire key-name seconds
    # 让给定键再指定的秒数之后过期
    print(r.expire('key',3))

    time.sleep(1)

    # ttl key-name
    # 查看给定键距离过期还有多少秒
    print(r.ttl('key'))

    time.sleep(3)

    print(r.get('key'))




    # persist key-name
    # 移除键的过期时间





    # expireat key-name timestamp
    # 将给定键的过期时间设置为给定的UNIX时间戳。

    # pttl key-name
    # 查看给定键距离过期时间还有多少毫秒，这个命令在Redis2.6或以上版本可用，

    # pexpire key-name milliseconds
    # 让给定键再指定的毫秒之后过期。这个命令在Redis2.6或以上版本可用。

    # pexpireat key-name timestamp-milliseconds
    # 将一个毫秒级精确的UNIX时间戳设置为给定键的过期时间，这个命令在Redis2.6或以上版本可用。

    pass


if __name__ == '__main__':
    # sort_test()
    test1()
    # 等待500毫秒，让操作有足够的时间完成
    time.sleep(.5)
    print('*'*30)
    test2()
    time.sleep(1)
    print('*' * 30)
    time_to_live()