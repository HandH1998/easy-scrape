from urllib.parse import quote
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re
import random

base_url = "https://baike.baidu.com"
his = []
# urllib中的quote方法可以实现中文的url编码，unquote可以实现解码
his.append(quote("/item/中世纪/1191766"))

for i in range(100):
    url = base_url + his[-1]
    try:
        html = urlopen(url).read().decode('utf-8')
    except:
        print("can't get access to:", url)
        his.pop()
        continue
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', url)
    sub_urls = soup.find_all('a', {'target': '_blank', 'href': re.compile(r'/item/(%.{2})+$')})
    # pprint(sub_urls)
    if len(sub_urls) != 0:
        # random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改
        his.append(random.sample(sub_urls, 1)[0].get('href'))
        # pprint(his)
    else:
        his.pop()
