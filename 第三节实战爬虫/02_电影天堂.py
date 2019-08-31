from lxml import etree
import requests

'''
获取每个电影中的url
'''

URL = 'https://www.dy2018.com'
# 电影天堂
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def get_dateil_url(url):
    response = requests.get(url,headers=HEADERS)

    # 注意每个网页选择的编码方式不一样，所以要查看网页源代码查看编码方式
    # print(response.text)    # requests库会自己猜测解码方式，然后存储到text中，我们还是选择其他的解码方式,
    text = response.text
    html = etree.HTML(text)  # 解析text
    dateil_urls = html.xpath('//table[@class="tbspan"]//a/@href')
    dateil_urls = map(lambda url:URL+url,url,dateil_urls)
    return dateil_urls


def bans_url(url):
    response = requests.get(url,headers=HEADERS)
    text = response.encoding('utf-8').decode('gbk')
    html = etree.HTML(text)
    title = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    print(title)

def prider():
    basn_url = 'https://www.xiaopian.com/html/gndy/dyzz/index_().html'
    for x in range(1,8):    # 第一个for循环中是定义一共有7页
        wede = basn_url.format(x)
        movie = get_dateil_url(wede)
        for dateil_url in movie:    # 第二页for循环中是遍历每页电影详情中的url
            movies = get_dateil_url(dateil_url)
            break
        break


if __name__ == '__main__':

    prider()










