'''

使用cookie模拟登录
人人网 ：3478525849
lw123456
'''

# 不设置cookie进行登录

from urllib import request

url = 'http://www.renren.com/SysHome.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

}
response = request.Request(url=url,headers=headers)
ret = request.urlopen(response)
with open('rrwang.html','w') as fp:
    fp.write(ret.read().decode('utf-8'))







