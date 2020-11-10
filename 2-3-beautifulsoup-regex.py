from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://www.tencent.com/zh-cn") \
    .read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')
# 添加了正则表达式限制
img_url = soup.find_all('img', {'src': re.compile(r'.*?\.jpg')})
pprint(img_url)

for i in img_url:
    print(i.get('src'))
