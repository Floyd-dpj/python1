from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
# print(conn.get_server_info())


# 非查询代码
# cursor = conn.cursor()
# conn.select_db("test")
# cursor.execute("create table test_pymysql(id int,info varchar(255));")

# 查询代码
# cursor = conn.cursor()
# conn.select_db("test1")
# cursor.execute("select * from student where name = '董配军' ")
# results: tuple = cursor.fetchall()
# for r in results:
#     print(r)


# 插入数据代码  --->可能需要提交
# cursor = conn.cursor()
# conn.select_db("py_sql")
# cursor.execute("insert into student  values(4,'苏毛',24)")


cursor = conn.cursor()
conn.select_db("py_sql")
cursor.execute("select * from orders")
results: tuple = cursor.fetchall()
# print(results)
for r in results:
    for a in r:
        f = open('D:/orders.txt', 'a', encoding='UTF-8')
        a = str(a)
        f.write(a)
        f.flush()

conn.close()
f.close()
