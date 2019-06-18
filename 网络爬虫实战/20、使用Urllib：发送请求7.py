import urllib.error
import urllib.request,urllib.parse
import socket

url='http://httpbin.org/post'

headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host':'httpbin.org'
}
data={
    'name':'mark'
}
data=bytes(urllib.parse.urlencode(data),encoding='utf-8')
request=urllib.request.Request(url,data=data,headers=headers,method='post')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
