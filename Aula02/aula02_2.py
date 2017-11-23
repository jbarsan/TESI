from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html5lib')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link3'))
'''
for link in soup.find_all('a'):
    print(link.get('href'))
'''

head_tag = soup.head
#print(head_tag)
#print(head_tag.contents)

title_tag = head_tag.contents[0]
#print(title_tag)
#print(len(title_tag.contents))
#print(soup.contents[0].name)

#text = title_tag.contents[0]
#print(text.contents)
'''
for child in title_tag.children:
    print(child)
'''

# print(head_tag.contents)

for child in head_tag.descendants:
    print(child)