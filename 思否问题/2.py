import requests
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
url='https://s3.pstatp.com/ies/resource/falcon/douyin_falcon/page/reflow_user/index_869e686.js'

print(requests.get(url,headers=headers).text)