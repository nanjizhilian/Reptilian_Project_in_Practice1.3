
import requests

parmas = {
    'wd':'中国 '
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

response = requests.get('http://www.baidu.com/s',params=parmas,headers=headers)

with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)















