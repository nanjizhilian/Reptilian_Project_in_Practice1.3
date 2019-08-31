
from urllib import request,parse


url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.'
                  '3809.100 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='


}



data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}

st = request.Request(url,headers=headers,
                     data=parse.urlencode(data).encode('utf8')
                     ,method='POST')
ss = request.urlopen(st)
print(ss.read().decode('utf-8'))





