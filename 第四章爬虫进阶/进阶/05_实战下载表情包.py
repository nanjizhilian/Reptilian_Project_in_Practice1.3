import requests
from lxml import etree
import re
import os
from urllib import request


def page_tu(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    text = response.text
    imag = etree.HTML(text)     # 解析数据
    img = imag.xpath('//div[@class="col-sm-9 center-wrap"]//img[@src!=gif]')
    for y in img:
        img_url = y.get('data-original')
        alt = y.get('alt')  # 获取图片中的文字
        alt = re.sub(r'[\?？\.。!]','',alt)   # 将图片中的文字特殊的符号过滤并替换替换
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        request.urlretrieve(img_url,'Reptilian_Project_in_Practice/'+filename)  # 将图片保存到本地


def main():
    for x in range(1,101):   # 意思是循环1到100次，意思是爬取100页的表情包
        url = 'http://www.doutula.com/article/list/?page=%d' % x
        page_tu(url)
        break


if __name__ == '__main__':
    main()










