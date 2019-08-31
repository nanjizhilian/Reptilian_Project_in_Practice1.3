'''
设置cookie信息
'''
from urllib import request

url = 'http://www.renren.com/leftmenu/getAllFeedCount'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0'
                  '.3809.100 Safari/537.36',
    'Cookie': 'anonymid=jzdhs54g7t8cov; depovince=GW; _r01_=1; JSESSIONID=abcGK5CdV0_qN4n1-pyYw; ick_login=f84f2a53-'
              'b0eb-46a4-8f0a-c66b3e660bb6; ick=d9e57e2a-0b7e-40f2-b4e3-c3ea17144bb8; XNESSESSIONID=d62d60e6ec64; jebe_'
              'key=3a863a71-3520-44cf-9e78-2148e458c2b7%7Cd9214107823c34c0ad7a34703ec3b1b6%7C1565922621887%7'
              'C1%7C1565922623003; jebe_key=3a863a71-3520-44cf-9e78-2148e458c2b7%7Cd9214107823c34c0ad7a34703ec3b1b6%7'
              'C1565922621887%7C1%7C1565922623010; wp=0; jebecookies=a777a45a-68b9-4bc6-98ea-50caab6734e6|||||; _de=0E4'
              '96EB0B4891C9C4F356AE910195131; p=95433726f717210cb070fd844446c6120; first_login_flag=1; ln_uact=18019339'
              '863; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=7bd559b05094d54e2af6932f04a9e3f60; s'
              'ocietyguester=7bd559b05094d54e2af6932f04a9e3f60; id=971936400; xnsid=67aa6966; ver=7.0; loginfrom=null'
              '; wp_fold=0'

}

response = request.Request(url=url,headers=headers)
ret = request.urlopen(response)
with open('设置cookie','w',encoding='utf-8') as fp:
    fp.write(ret.read().decode('utf-8'))











