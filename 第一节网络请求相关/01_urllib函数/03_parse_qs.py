from urllib import parse

p = {'name':'le','age':19}
ret = parse.urlencode(p)
print(ret)

res = parse.parse_qs(p) # 解码
print(res)






