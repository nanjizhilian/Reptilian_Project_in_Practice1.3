'''

lxml和xpath结合使用
'''
from lxml import etree
parser = etree.HTMLParser(encoding='utf-8')

html = etree.parse('tencent.html',parser=parser)

# 1,获取所有的div标签
trs = html.xpath('//div')
for tr in trs:
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))




# # 2，获取div第二个a标签
# trs = html.xpath('//div[1]')[0]
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
# print(trs)



# 3,获取所有div里的class等于user-nav
# trs = html.xpath('//div[@class="user-nav"]')
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))




# # 4，获取所有a标签中的href属性
# # href属性是字符串类型，所有不用tostring
# trs = html.xpath('//a/@href')
# for tr in trs:
#     print(tr)




# 获取所有的职位信息纯文本
