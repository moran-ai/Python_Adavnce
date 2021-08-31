from pymysql import *

# 创建数据库连接
conn = Connect(host='localhost', user='root', port=3306, password='itcast', db='mytestdb')
# print(conn)
# 打开游标
cue = conn.cursor()
try:
    # 执行sql语句
    sql = 'insert into student_ values (%s,%s,%s,%s,%s,%s)'
    params = (5, 'kk', '123456', '男', '2021-03-24', 20)
    rowcount = cue.execute(sql, params)
    conn.commit()
except:
    conn.rollback()
print('添加成功')
# 关闭游标
cue.close()

# 关闭连接
conn.close()
