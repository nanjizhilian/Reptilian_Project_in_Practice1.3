from urllib import request


resp = request.urlopen('http://www.baidu.com')
# print(resp.read())  # 获取所有

print(resp.read(30))    # 读取前30行












