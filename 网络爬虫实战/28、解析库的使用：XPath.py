from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html=etree.HTML(text)
result=etree.tostring(html)
print(result.decode('utf-8'))

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=etree.tostring(html)
print(result.decode('utf-8'))

print('*'*30)

all_note=html.xpath('//*')
print(all_note)

print('*'*30)

all_note=html.xpath('//li')
print(all_note)
print(all_note[0])

print('*'*30)

all_note=html.xpath('//li/a')
print(all_note)

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//a[@href="link4.html"]/../@class')
print(result)

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]')
print(result)

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]/text()')
print(result)

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]/a/text()')
print(result)

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]//text()')
print(result)

print('*'*30)

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li/a/@href')
print(result)

print('*'*30)
