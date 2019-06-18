import urllib.error
import urllib.request,urllib.parse
import socket
import http.cookiejar


filename='cookies.txt'
cookie=http.cookiejar.LWPCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)



