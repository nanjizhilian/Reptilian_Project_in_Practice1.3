import re
# # 1,匹配某个字符串
# ret = "holl word"
# res = re.match('ho',ret)    # 在ret里匹配ho，从开头匹配如果ho前面加一个a（aho）则会报错
# print(res.group())


# [.]匹配任意字符
# ret = "\n"
# res = re.match(".",ret) # .不会匹配到\n，会报错
# print(res.group())
# # 报错如下：AttributeError: 'NoneType' object has no attribute 'group'
# # 因为没有匹配到，所以res是None,None类型是没有group()



# \d匹配任意的数字0到9
# ret = "32312"
# res = re.match('\d',ret)
# print(res.group())



# \D匹配任意的非数字
# ret = "12+=$3"
# res = re.match('\D',ret)
# print(res.group())




# # \s可以匹配任意的空白字符
# # 可以匹配（空格，\n,\r,\t）
# ret = '\n'
# res = re.match('\s',ret)
# print(res.group())




# # \w匹配的是a-z,A-Z,数字以及下划线
# ret = "_"
# res = re.match('\w',ret)
# print(res.group())
#




# # \W和\w相反
# ret = '+'
# res = re.match('\W',ret)
# print(res.group())




# 组合匹配，满足中扩号中的条件
# ret = "0710-99001000askjd"
# res = re.match('[\d\-]+',ret)# d后面的\是将-转意，因为-是特殊字符，中括号后面的加号是至少匹配一个或多个字符，现在中括号里的条件只匹配数字所以后面的英文撇不到
# print(res.group())




# 中括号形式代替\d
# ret = '023456789'
# res = re.match('[0-9]',ret) # 匹配0-9任意字符，只匹配一个
# ree = re.match('[0-9]+',ret) # 匹配0-9任意字符，匹配多个
# print(res.group())  # 结果：0
# print(ree.group())  # 结果：023456789



#
# # 中括号代替\D
# ret = 'sadjkhajksd'
# res = re.match('[a-z]',ret) # 匹配一个任意非数字
# ress = re.match('[a-z]+',ret) # 匹配多个任意非数字
# print(res.group())  # 结果：0
# print(ress.group()) # 结果：sadjkhajksd



# 中括号代替\w
# ret = '_123'
# res = re.match('[a-zA-Z0-9_]',ret)  # 匹配一个任意的a-z以及A-Z以及0-9以及_
# ress = re.match('[a-zA-Z0-9_]+',ret)  # 匹配一个任意的a-z以及A-Z以及0-9以及_
# print(res.group())  # 结果_
# print(ress.group()) # 结果_123



# # 中括号代替\W
# ret = '0_eqe1231'
# res = re.match('[a-zA-Z0-9_]',ret)  # 匹配一个
# print(res.group())



# ret = 'hello word'
# res = re.match('^h',ret)    # 匹配已什么开头
# print(res.group())
