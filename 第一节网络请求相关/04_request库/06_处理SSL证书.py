'''
对于一些不信任的的网站也就是没有SSL
在request中添加verify=True即可
'''

import requests
response =  requests.get('http://www.baidu.com',verify=True) # <-----设置为True
print(response.text)

