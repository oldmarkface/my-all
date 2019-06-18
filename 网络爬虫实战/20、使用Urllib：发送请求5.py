import urllib.error
import urllib.request
import socket

request=urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
