
# 设置代理
from urllib import request

url = 'http://httpbin.org/ip'
headers = request.ProxyHandler({'http':'180.118.247.244:9000'})
ret = request.build_opener(headers)
ss = ret.open(url)
print(ss.read())




