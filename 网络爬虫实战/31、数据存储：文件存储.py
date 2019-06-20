import requests
from pyquery import PyQuery as pq

url='https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html=requests.get(url=url,headers=headers).text
# print(html)
doc=pq(html)
items=doc('.explore-feed.feed-item').items()
for item in items:
    question=item.find('.question_link').text()
    author=item.find('.author-link').text()
    answer=pq(item.find('.content').html()).text()
    print(question)
    print(author)
    print(answer)

    with open('explore.txt','a',encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n'+'='*50+'\n')


