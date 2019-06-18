import urllib.error
import urllib.request
import socket

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time Out')
