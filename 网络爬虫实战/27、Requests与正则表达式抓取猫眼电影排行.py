import requests
import re,json
def get_one_page(url):
    response=requests.get(url)
    if response.status_code==200:
        return response.text
    return None
def parse_one_page(html):
    pattern = re.compile('<dd>.*?<i.*?>(\d*)</i>.*?data-src="(.*?)".*?name.*?<a.*?>(.*?)</a>', re.S)
    results = re.findall(pattern, html)
    for result in results:
        yield {
            'index':result[0],
            'images':result[1],
            'title':result[2].strip(),
        }


def write_to_json(context):
    with open('top10.txt','a') as f:
        print(type(json.dumps(context)))
        f.write(json.dumps(context,ensure_ascii=False)+'\n')
if __name__ == '__main__':
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset='+str(i*10)
        html = get_one_page(url)
        print(html)
        items = parse_one_page(html)
        for item in items:
            write_to_json(item)


