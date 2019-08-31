import pymysql

# conn = pymysql.connect(host='localhost',user='root',password='Lw199795',database='Reptile',port=3306)
# corsor = conn.cursor()    # 创建游标
# sql = """
# insert into reptile(id,username,age,password) values(2,'刘百科',22,123)
# """
# corsor.execute(sql)
# conn.commit()   # 提交
# conn.close()     # 关闭链接


import pymysql
# conn = pymysql.connect(host='localhost',user='root',password='Lw199795',database='Reptile',port=3306)
# corsor = conn.cursor()    # 创建游标
# sql = """
# select id,username,age from reptile where id = 2
# """
# corsor.execute(sql)
# ret = corsor.fetchone()   #  只返回一条数据
# print(ret)
# conn.close()
# # 结果：(2, '刘百科', 22)



# conn = pymysql.connect(host='localhost',user='root',password='Lw199795',database='Reptile',port=3306)
# corsor = conn.cursor()    # 创建游标
# sql = """
# select id,username,age from reptile
# """
# corsor.execute(sql)
# ret = corsor.fetchmany(2)  # 如果填写的2就查找2条，如果不填写，默认返回一条数据
# for i in ret:
#     print(i)
# conn.close()



conn = pymysql.connect(host='localhost',user='root',password='Lw199795',database='Reptile',port=3306)

corsor = conn.cursor()
sql = """
delete from reptile where id = 2
"""
corsor.execute(sql) # 执行sql语句
conn.commit()
conn.close()




