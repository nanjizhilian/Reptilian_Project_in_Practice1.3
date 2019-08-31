
from urllib import request
from urllib import parse



#   4,使用opersn发送人人网登录请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

def cookis():
    from http.cookiejar import CookieJar
    #   1，创建一个cookiejar对象
    CookieJar = CookieJar()
    #   2。使用cookie创建一个Httpcookieprocess对象
    headers = request.HTTPCookieProcessor(CookieJar)
    #   3,使用上一步创建一个opensr
    opener = request.build_opener(headers)
    return opener


def pernet(opener):
    data = {
        'email': '3478525849@qq.com',
        'password':'lw123456',
    }
    log_url = 'http://www.renren.com/SysHome.do'
    ret = request.Request(log_url,headers=headers,data=parse.urlencode(data).encode('utf-8'))
    opener.open(ret)


def index(opener):
# 访问个人主页
    index_url = 'http://www.renren.com/leftmenu/getAllFeedCount'
    rats = request.Request(index_url,headers=headers,data=data)
    reat = opener.open(rats)
    with open('rrw.html','w',encoding='utf-8') as fp:
        fp.write(reat.read().decode('utf-8'))

if __name__ == '__main__':
    pass


