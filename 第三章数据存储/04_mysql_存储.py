import pymysql

# python 代码 链接数据库
conn = pymysql.connect(host='localhost',user='root',password='Lw199795',database='Reptile',port=3306)
corsor = conn.cursor()  # 创建游标
corsor.execute('select 1')  # 查询1
reslut = corsor.fetchall()
print(reslut)
conn.close()    # 关闭链接


