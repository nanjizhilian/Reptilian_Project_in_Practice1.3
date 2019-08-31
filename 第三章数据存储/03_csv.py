import csv

# headers = ['username','age','heigut']
# values = [
#     ('张三',32,180),
#     ('里斯',23,18),
#     ('王五',25,169)
# ]
# # newline是写入文件是会默认在每行后面加上\n，所以在这里指定为空
# with open('classroom.csv','w',encoding='utf-8',newline='') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(headers)    # writerow一次性可以写入多行
#     writer.writerow(values)
#


def writer_csv_demo1():
    headers = ['username','age','heigut']
    values = [
        ('张大炮',34,180),
        ('二狗',26,179),
        ('有云来',35,160),
    ]
    with open('classroom02.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writernow(headers)
        writer.writernow(values)



def writer_csv_demo02():
    headers = ['username','age','heigut']
    values = [
        {'username':'张宇唱','age':24,'heigut':180},
        {'username':'好汉','age':35,'heigut':189},
        {'username':'美工','age':42,'heigut':176},
        {'username':'唱个','age':23,'heigut':174},
    ]
    with open('classroom03.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.DictWriter(fp,headers)  # 以字典写入数据时，调用DictWriter方法
        # 写入表头数据的时候，一定要调用writeheader方法
        writer.writeheader()
        writer.writerows(values)    # writerows 可以写入多个数据

if __name__ == '__main__':
    writer_csv_demo02()




