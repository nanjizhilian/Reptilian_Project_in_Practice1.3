import re

# # $在正则中是有特殊意义的，可以在$前面加上一个\就可以了
# ret = "in or not city $9999"
# des = re.search("\$\d+",ret)    # 解释：resarch是在全局匹配
# print(des.group())


# # 原生字符串解析   方便
# ret = '\\n'
# res = re.match(r'\\n',ret)
# print(res.group())
#


#
# # 分组
# # 需求：将所有数字（钱）提取出来
# ret = "re in froms $900 ret $400"
# res = re.search('.*(\$\d+).*(\$\d+)',ret)   #  \$符号意思是，匹配到$符号，后面的是\d+意思是匹配多个数字（\$\d+）
# print(res.groups()) # 是将所有分组拿出来
# # 结果 ：('$900', '$400')
#




# # 将$符号后面的数字提取出来
# ret = "ajk in not null $90000 find_all $120000"
# res = re.findall('\$\d+',ret)
# print(res)






#  sub函数
# # 将等到的字符串进行替换
# ret = "sadl dweo $900 ajkdk $8000 ksdaj"
# res = re.sub("\$\d+","^",ret)
# print(res)
# # 结果 ：sadl dweo ^ ajkdk ^ ksdaj





# split 函数
# 分割
ret = "holl word ni hao"
res = re.split("[^a-zA-Z]",ret)
print(res)
# 结果 ： ['holl', 'word', 'ni', 'hao']






