import re
import requests


def page_get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    response = requests.get(url,headers)
    text = response.text
    text = re.findall(r'<div class="content">.*?<span>(.*?)</span>',text,re.S)
    print(text)



def get_url():
    url = 'https://www.qiushibaike.com/hot/'
    page_get(url)


if __name__ == '__main__':
    get_url()











