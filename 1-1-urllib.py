from urllib.request import urlopen
import re

# 有中文的话，decode()
html = urlopen("https://github.com/MorvanZhou/easy-scraping-tutorial") \
    .read().decode('utf-8')
print(html)
res=re.findall(r"<title>(.+?)")