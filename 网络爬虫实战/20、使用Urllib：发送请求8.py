import urllib.error
import urllib.request,urllib.parse
import socket
import http.cookiejar


cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name+"="+item.value)


