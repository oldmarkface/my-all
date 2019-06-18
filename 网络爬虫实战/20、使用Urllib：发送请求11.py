import urllib.error
import urllib.request,urllib.parse
import socket
import http.cookiejar


filename='cookies.txt'
cookie=http.cookiejar.LWPCookieJar()
cookie.load(filename,ignore_expires=True,ignore_discard=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))



