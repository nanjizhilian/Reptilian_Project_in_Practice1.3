import json
# 将python转换成json数据格式
pacts = [
    {
        'username':"占三",
        'age':19,
        'nikname':"xiaochengba"
    },
    {
      'username':'xiaolingr',
      'age':23,
      'nikname':"xiaobaic"
    }
]
with open('acts.json','w') as fp:
    json.dump(pacts,fp)


# ret = json.dumps(pacts)
# print(type(ret))
# print(ret)
# # 结果：
# # <class 'str'>
# # [{"username": "\u5360\u4e09", "nikname": "xiaochengba", "age": 19}, {"username": "xiaolingr", "nikname": "xiaobaic", "age": 23}]




with open('acts.json','w') as fp:
    json.dump(pacts,fp)







