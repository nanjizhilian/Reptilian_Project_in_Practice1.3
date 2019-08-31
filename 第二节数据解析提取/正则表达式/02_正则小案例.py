# 正则小案例
import re


# 手机号验证
# text = "18578900980"
# ret = re.match("1[345789]\d(9)",text)
# print(ret.group())



# 匹配邮箱

# ret = 'liuwe123@qq.123com'
# ress = re.match('\w+@[a-z0-9]+\.[a-z0-9]+',ret)
# print(ress.group())



# 验证url
# url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
# ret = re.match('(http|https|ftp)://[^\s]+',url)
# print(ret.group())



# 验证身份证
# ret = '13827394829124x'
# ress = re.match('\d(17)\d[xX]',ret)
# print(ress.group())


# 贪婪模式
# ret = "0123345"
# res = re.match('\d+',ret)   # 尽量的多匹配
# print(res.group())

# 和非贪婪模式
# ret = "0123456"
# res = re.match('\d+?',ret)
# print(res.group())





# 匹配0-100之间的数字
# 可以匹配：1，3，100
# 不可以匹配：101，0




