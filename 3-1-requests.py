import requests

# get请求
param = {"wd": "莫烦Python"}
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)

# post请求
data = {'firstname': 'zhang', 'lastname': 'zhou'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)