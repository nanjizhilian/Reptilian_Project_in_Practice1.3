import requests
from lxml import etree

# 1,将页面爬取下来
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'https://movie.douban.com/cinema/nowplaying/shanghai/'
}
url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
response = requests.get(url,headers=headers)

# print(response.text)    # 返回的是一个解码的字符串，是str(uicode)类型
# print('>>>>>>>>>>>>>>>>>'*40)
# print(response.content) # 返回的是一个原生的网页源代码，是bytes类型
text = response.text


# 2，将数据提取
html = etree.HTML(text)
ul = html.xpath('//ul[@class="lists"]')[0]      # 获取ul下的所有class标签和lists属性
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))

li = ul.xpath('./li')

movies = []
for i in li:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = i.xpath('@data-title')[0]
    score = i.xpath('@data-score')[0]
    release = i.xpath('@data-release')[0]
    region = i.xpath('@data-region')[0]
    actors = i.xpath('@data-actors')[0]
    img = i.xpath('.//img/@src')[0]

    movie = {
        'title':title,
        'score':score,
        'release':release,
        'region':region,
        'actore':actors,
        'img':img
    }
    movies.append(movie)
print(movies)






















