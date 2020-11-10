from pprint import pprint

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://www.tencent.com/zh-cn") \
    .read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')
# find_all方法中第一个是匹配的标签，同时在后面的字典中加上clas
# 限制条件，是匹配那些class是"tex"的p标签
p = soup.find_all('p', {'class': 'txt'})
pprint(p)

for i in p:
    # 选取每个标签的文字内容 get_text()方法
    print(i.get_text())

# find方法返回一个第一匹配到的对象
ul=soup.find('ul',{'class':'slide_list'})
pprint(ul)
li=ul.find_all('li')
for i in li:
    print(i.get_text())