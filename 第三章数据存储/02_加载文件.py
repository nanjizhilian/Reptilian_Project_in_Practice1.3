import json

with open('acts.json','r',encoding='utf-8') as fp:
    ret = json.load(fp)
    print(type(ret))
    for i in ret:
        print(i)
# 结果：
# <class 'list'>
# {'nikname': 'xiaochengba', 'username': '占三', 'age': 19}
# {'nikname': 'xiaobaic', 'username': 'xiaolingr', 'age': 23}








