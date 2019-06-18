import urllib.request

response=urllib.request.urlopen('http://www.baidu.com')
#<class 'http.client.HTTPResponse'>
print(type(response))
print('*'*30)
print(response.status)
print('*'*30)
print(response.getheader('Server'))
print('*'*30)
print(response.getheaders())
print('*'*30)
print(response.read().decode('utf-8'))