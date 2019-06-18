from urllib.parse import urlparse,urlunparse,urlsplit,urlunsplit

result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result,sep='\n')

result=urlparse('www.baidu.com/index.html;user?id=5#comment')
print(type(result),result,sep='\n')

result=urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(type(result),result,sep='\n')

result=urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(type(result),result,sep='\n')

result=urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
print(type(result),result,sep='\n')

result=urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
print(type(result),result,sep='\n')


result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme,result[0],result.netloc,result[1],sep='\n')


data=['http','www.baidu.com','/index.html','user','id=5','comment']
print(urlunparse(data))

result=urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

result=urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme,result[0])

data=['http','www.baidu.com','/index.html;user','id=5','comment']
print(urlunsplit(data))
