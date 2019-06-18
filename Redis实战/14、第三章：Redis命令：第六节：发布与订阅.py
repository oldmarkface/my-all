import redis
import time, threading

r = redis.StrictRedis(host='localhost', port=6379, db=0)


# psubscribe pattern [pattern ...]
# 订阅与给定模式相匹配的所有频道

# punsunscribe [pattern [pattern ...]]
# 退订给定的模式，如果执行时没有给定任何模式，那么退订所有模式。


def publisher(n):
    # 函数在开始执行时会先休眠，让订阅者有足够的时间来连接服务器并监听消息
    time.sleep(1)

    for i in range(n):
        # 向给定频道发送消息
        # publish channel message
        r.publish('key', i)

        # 在发送消息之后进行短暂的休眠，让消息可以一条接一条地出现
        time.sleep(1)


def pubsuber():
    # 创建订阅对象，并向它订阅给定的频道
    pubsub = r.pubsub()
    # subscribe channel [channel ...]
    # 订阅给定的一个或多个频道
    pubsub.subscribe(['key'])
    count = 0
    # 通过遍历函数pubsub.listen()的执行结果来监听订阅信息
    for item in pubsub.listen():
        print(item)
        count += 1
        if count == 10:
            # unsubscribe [channnel channel ...]
            # 退订给定的一个或多个频道，如果执行时没有给定任何频道，那么退订所有频道
            pubsub.unsubscribe()
        if count == 11:
            break


if __name__ == '__main__':
    # 启动发送者线程，并让它发送三条消息
    threading.Thread(target=publisher, args=(30,)).start()
    pubsuber()
