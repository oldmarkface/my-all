import requests
from urllib.parse import urlencode
import os
from hashlib import md5
headers = {
    'Host': 'www.toutiao.com',
    'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'tt_webid=6704808321848215043; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16b77e85ac24d7-006d237c790a88-4a5568-1fa400-16b77e85ac344b; CNZZDATA1259612802=1104480020-1561079689-%7C1561079689; __tasessionId=n39mykl9q1561084844772; tt_webid=6704808321848215043; csrftoken=dcd1d465bc7441c32e8f77a18e4dcb62; s_v_web_id=bfc941bbb6430551a71c9f370afd2c71TE: Trailers'
}
def get_page(offset):
    params={
        'aid':24,
        'app_name':'web_search',
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':20,
        'en_qc':1,
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':'1561085020266',
        'offset':offset
    }
    url='https://www.toutiao.com/api/search/content/?'+urlencode(params)
    print(url)
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.json()
    return None

def get_image(page):
    if page.get('data'):
        for item in page.get('data'):
            title=item.get('title',None)
            image_list=item.get('image_list',[])
            if title:
                yield {
                    'title':title,
                    'image_list':image_list
                }

def save_image(item):
    if not os.path.exists('toutiao/'+item.get('title')):
        os.mkdir('toutiao/'+item.get('title'))

    for img in item.get('image_list'):
        print(img.get('url'))
        response=requests.get(img.get('url'))
        if response.status_code==200:
            file_path='toutiao/{0}/{1}.{2}'.format(item.get('title'),
                                           md5(response.content).hexdigest(),
                                           'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('已经下载了')
        else:
            print(response.reason)



if __name__ == '__main__':
    x=get_page(0)
    for y in get_image(x):
        save_image(y)
    print(x)