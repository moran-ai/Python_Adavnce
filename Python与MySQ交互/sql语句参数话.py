from pymysql import *

# 创建数据库连接
conn = Connect(host='localhost', user='root', port=3306, password='itcast', db='mytestdb')
print(conn)
# 打开游标
cue = conn.cursor()
# 执行sql语句
name = input('输入用户名：')
passwd = input('输入密码：')
sql = "select * from student_ where name=%s and passwd=%s"
params = (name, passwd)
print(sql)
rowcount = cue.execute(sql, params)
if rowcount != 0:
    print('登录成功')
else:
    print('登陆失败')

# 关闭游标
cue.close()

# 关闭连接
conn.close()
