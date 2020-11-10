from urllib.request import urlopen
import re

# 有中文的话，decode()
html = urlopen("https://github.com/MorvanZhou/easy-scraping-tutorial") \
    .read().decode('utf-8')
print(html)
#  重复运算符后加？指定非贪婪匹配
res = re.findall(r"<title>(.+?)</title>", html)
print(res[0])

res = re.findall(r"<p>(.*?)</p>", html)
print(res[0])

res = re.findall(r'href="(.*?)"', html)
print(res[0])