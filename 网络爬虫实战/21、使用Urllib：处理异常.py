from urllib import request,error



try:
    response=request.urlopen('http://www.mark.com/mark')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')



