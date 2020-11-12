from urllib.request import urlretrieve
import os
import requests

# 前2种方法都是把文件整个先下载到内存，然后写到本地磁盘
# 第3中流式下载可以一边下一边存


# 使用urlretrieve下载
# makedirs可以创建多重目录
# exist_ok：是否在目录存在时触发异常。如果exist_ok为False（默认值），则在目标目录已存在的情况下触发FileExistsError异常；
# 如果exist_ok为True，则在目标目录已存在的情况下不会触发FileExistsError异常。
os.makedirs('./img',exist_ok=True)
img_url="https://img-blog.csdn.net/20141110144121544?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmsybWU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast"
urlretrieve(img_url,'./img/image1.png')

# 使用外部模块requests里的方法下载
r=requests.get(img_url)
# 本地打开文件，写入文件
with open('./img/image2.png','wb') as f:
    f.write(r.content)

# 流式下载
r=requests.get(img_url, stream=True)
with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)




