import re
import requests

def pares_page(url):
    herader = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    response = requests.get(url,herader)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a .*?>(.*?)</a>',text,re.DOTALL)
    dname = re.findall(r'<p class="source">.*?<a .*?>.*?<a .*?>(.*?)</a>',text,re.DOTALL)
    contents = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)

    contes = []
    for i in contents:
        x = re.sub(r'<.*?>',"",i)   # 替换匹配的hr标签
        contes.append(x.strip())    # 除去匹配到的空格

    paget = []
    for values in zip(titles,dynasties,dname,contents):
        titles,dynasties,dname,contents = values
        poem = {
            'titles':titles,
            'dynasties':dynasties,
            'dname':dname,
            'contents':contents,
        }
        paget.append(poem)

    for i in paget:
        print(i)
        print('='*30)



def main():
    url = 'https://www.gushiwen.org/default_1.aspx'
    for i in range(1,11):
        url = "https://www.gushiwen.org/default_%s.aspx" %i
        pares_page(url)


if __name__ == '__main__':
    main()


