from urllib import request,error



try:
    response=request.urlopen('http://www.mark.com/mark')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('请求成功')



