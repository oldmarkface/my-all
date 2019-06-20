# 爬取女朋友的微博
import json

import requests
from urllib.parse import urlencode
from pyquery import PyQuery

base_url = 'https://m.weibo.cn/api/container/getIndex?'
uid='3098454065'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/'+uid,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
def get_page(page):
    params = {
        'type': 'uid',
        'value': uid,
        'containerid': '107603'+uid,
        'page': page
    }
    url=base_url+urlencode(params)
    print(url)
    result = requests.get(url, headers=headers)
    if result.status_code==200:
        return result.json()

def parse_json(json):
    if json:
        cards=json.get('data').get('cards')
        print(cards)
        for card in cards:
            mblog=card.get('mblog')
            weibo={}
            weibo['text']=PyQuery(mblog.get('text')).text()
            weibo['created_at']=mblog.get('created_at')
            yield weibo

def write_2_text(weibo):
    with open('face.txt','a') as file:
        file.write(json.dumps(weibo,indent=2,ensure_ascii=False))
        file.write('\n')




if __name__ == '__main__':
    for index in range(12):
        result = get_page(index)
        print(result)
        for x in parse_json(result):
            write_2_text(x)
