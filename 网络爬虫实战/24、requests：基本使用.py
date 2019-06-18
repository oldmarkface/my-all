import requests
r=requests.get('http://httpbin.org/get')
print(type(r),r.status_code,type(r.text),r.text,type(r.cookies),r.cookies,sep='\n')