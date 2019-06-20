from bs4 import BeautifulSoup
soup=BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)

print('*'*30)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.title.name)
print(soup.head)
print(soup.p)
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p.attrs['class'])
print(soup.p['class'])
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

print(soup.p.contents)
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(child)

print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(child)
