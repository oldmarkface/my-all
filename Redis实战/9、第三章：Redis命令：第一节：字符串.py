import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.delete('key')

# 尝试获取一个不存在的键将得到一个None值
print(r.get('key'))

# 对不存在的键执行自增操作
print(r.incr('key'))
print(r.incr('key', 19))

# 执行自减操作
print(r.decr('key', 5))

print(r.get('key'))

print(r.set('key', 99))
print(r.incr('key'))

r.delete('key')

# 追加字符串，返回最后字符串长度
print(r.append('key', 'mark'))
# 追加字符串，返回最后字符串长度
print(r.append('key', '-face'))

print(r.get('key'))

# 截取字符串
# 1：表示开始下标
# 3：表示截取数量
print(r.substr('key', 1, 3))

# 替换指定坐标，返回字符串总长度
print(r.setrange('key',1,'A'))
print(r.get('key'))
