import requests,re
headers = {
    'Referer': 'https://www.iesdouyin.com/share/user/60179369788',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
'authority':'www.iesdouyin.com',
'method': 'GET',
'path': '/share/user/60179369788',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
'cache-control': 'no-cache',
'cookie': '_ga=GA1.2.781166460.1560840786; _gid=GA1.2.480424082.1560840786; '
          '_ba=BA0.2-20190618-5199e-AD8ZK1e4uANGu2d8k5VM',
'pragma': 'no-cache',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'

}

s=requests.session()
re1=s.get('https://www.iesdouyin.com/share/user/60179369788',headers=headers)
#  uid: "60179369788",
#            dytk: 'ab518b74204432b916e63cfc2449ee0d'
print(re1.text)
# text=re1.text
# pattern=re.compile('href="(.*?)"')
# res=re.findall(pattern,text)
# for re in res:
#
#     if not re.endswith(('.png','css','ico')):
#         print('*'*30)
#         print(re)
#         print(s.get('https:'+re).text)


url='https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=60179369788&count=21&max_cursor=0&aid=1128&_signature=6ELmlRAStVVxLYqBRZApmehC5o&dytk=ab518b74204432b916e63cfc2449ee0d'
url='https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=60179369788&count=21&max_cursor=0&aid=1128&_signature=V9XECQAACt25k5tCeFKy11fVxB&dytk=ab518b74204432b916e63cfc2449ee0d'
re2=s.get(url)
print(re2.text)



# cs='_g=GA1.2.182731301.1560839747;_gid=GA1.2.965948451.1560839747'
# jar=requests.cookies.RequestsCookieJar()
# for cookie in cs.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# # url='https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=60179369788&count=21&max_cursor=0&aid=1128&_signature=DGqzMhAcUWeVBd8mnROt8Axqsy&dytk=ab518b74204432b916e63cfc2449ee0d'
# # url='https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=60179369788&count=21&max_cursor=0&aid=1128&_signature=ieLXVxAc1PdnpIgcrnob.Ini10&dytk=ab518b74204432b916e63cfc2449ee0d'
# result=requests.post(url,headers=headers,cookies=jar)
# print(result.text)