from bs4 import BeautifulSoup
import requests


def pares_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Referer': 'http://www.nmc.cn/'
    }

    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    sopu = BeautifulSoup(text,'lxml')

    divs = sopu.find('div',class_="rank")
    tr = divs.find_all('li')
    for i in tr:
        trs = i.find_all('li')[1:]
        for a in trs:
            tds = a.find_all('span')
            city_da = tds[1]
            city = list(city_da.stripped_strings)[0]
            fourst_td = a[-1]
            func = list(fourst_td.stripped_strings)[0]
            print({'city':city,'func':func})

        break


def main():
    url = 'http://www.nmc.cn/f/rest/province'
    pares_page(url)


if __name__ == '__main__':
    main()













