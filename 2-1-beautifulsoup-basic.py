from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://www.tencent.com/zh-cn") \
    .read().decode('utf-8')
print(html)

# BeautifulSoup将获取到的html转化soup对象
soup = BeautifulSoup(html, features='lxml')  # 解析方法选用lxml
# 选择标签即可  注意这里返回的是带标签的
print(soup.h1)
print('\n', soup.p)

# 这里返回的是一个列表，也是带标签的
all_href = soup.find_all('a')
print(all_href)
# 去标签，相当于在大标签下根据小标签，找小标签对应的内容
all_href = [i.get('href') for i in all_href]
print(all_href)
