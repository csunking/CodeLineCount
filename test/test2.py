# coding=utf-8
from io import BytesIO
import gzip
import urllib.request

url = ('http://wthrcdn.etouch.cn/weather_mini?city=%E4%B8%8A%E6%B5%B7')
resp = urllib.request.urlopen(url)
content = resp.read() # content是压缩过的数据

buff = BytesIO(content) # 把content转为文件对象
f = gzip.GzipFile(fileobj=buff)
res = f.read().decode('utf-8')
print(res)