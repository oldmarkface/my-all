from urllib.parse import urlencode,urlparse,parse_qs,parse_qsl

params={
    'name':'理想',
    'age':18
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)

query=urlparse(url).query
print(query)
print(parse_qs(query))
print(parse_qsl(query))

