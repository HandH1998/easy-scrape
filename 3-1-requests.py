import requests

# get请求
param = {"wd": "莫烦Python"}
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)

# post请求
# post提交数据
data = {'firstname': 'zhang', 'lastname': 'zhou'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)

# post提交文件
file = {'uploadFile': open('./test.jpg', 'rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
print(r.text)

# post登录
payload = {'username': 'zhang', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
# 登录之后会在本地创建一个cookie，记录登录认证信息，每次请求时都把cookie字段添加到请求头，否则没有认证信息登陆失败
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

# session会话
# 创建session会话对象
session = requests.Session()
payload = {'username': 'zhang', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
# 使用session机制，session会把一些信息存储在服务器中，不用每次都把cookie放进去
# session会话会把多次http请求联系在一起
r=session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(r.text)
