from pymysql import *

# 创建数据库连接
conn = Connect(host='localhost', user='root', port=3306, password='itcast', db='mytestdb')
# print(conn)
# 打开游标
cue = conn.cursor()

# 执行sql语句
sql = 'select name,passwd,sex from student_ where age > %s'
params = (19)
cue.execute(sql, params)
# result = cue.fetchone()
# print(result)
# result = cue.fetchmany(4)
result = cue.fetchall()
for row in result:
    print(row)
# 关闭游标
cue.close()

# 关闭连接
conn.close()
