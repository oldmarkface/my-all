import requests
data={
    'name':'mark'
}
r=requests.get('http://httpbin.org/get',params=data)
print(r.text)

print(type(r.text))
print(r.json())
print(type(r.json()))