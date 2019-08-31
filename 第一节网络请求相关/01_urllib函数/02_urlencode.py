'''
知识点：parse.urlencode编码

'''


from urllib import parse

data = {'name':'alsess','age':10,'basd':1000}
qs = parse.urlencode(data)
print(qs)







