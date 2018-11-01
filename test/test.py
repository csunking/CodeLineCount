import urllib.request

url = 'http://www.ip138.com'
#proxy_support = urllib.request.ProxyHandler({'http':'10.33.168.111:80'})
opener = urllib.request.build_opener() # urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('GBK')
print(html)