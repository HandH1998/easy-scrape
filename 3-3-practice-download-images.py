import requests
from bs4 import BeautifulSoup

url = 'http://www.ngchina.com.cn/photography/photocontest/2019'
# .text 获得html文档
html = requests.get(url).text
soup = BeautifulSoup(html, features='lxml')
ul = soup.find_all('ul', {'id': 'indexPicList'})
for i in ul:
    images = i.find_all('img')
    for j in images:
        url = j.get('src')
        image_name = url.split('/')[-1]
        r = requests.get(url, stream=True)
        with open('./img/' + image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)
        print('Saved :', image_name)
