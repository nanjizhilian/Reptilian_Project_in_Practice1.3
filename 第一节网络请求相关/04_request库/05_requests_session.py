import requests

url = 'http://www.renren.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
data = {
    'email': '18019339863',
    'password': 'lw123456'
}
session = requests.Session()
session.post(url,data=data,headers=headers)


# 使用seesion中登录过的信息，在次请求首页
response = session.get('http://www.renren.com/971936400')

with open('rrw.html','w',encoding='utf-8') as fp:
    fp.write(response.text)

