'''
需求：
    将百度的首页保存到本地


知识点：urlretrieve函数（可以将爬取到的文字/图片/视频等保存下来）
'''

from urllib import request

resp = request.urlretrieve('http://www.taobao.com','taobao.html')
print(resp)




# resp = request.urlretrieve('https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word='
#                            'mac%B8%DF%C7%E5%B1%DA%D6%BD%201440%20x%20900&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps='
#                            '111111','mac壁纸.jpg')
# print(resp)





