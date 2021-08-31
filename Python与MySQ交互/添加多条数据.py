from pymysql import *

# 创建数据库连接
conn = Connect(host='localhost', user='root', port=3306, password='itcast', db='mytestdb')
# print(conn)
# 打开游标
cue = conn.cursor()
try:
    # 执行sql语句
    sql = 'insert into student_ values (%s,%s,%s,%s,%s,%s)'
    params = [(6, 'kk', '123456', '男', '2021-03-24', 20),
              (7, 'kk1', '123456', '男', '2021-03-24', 20),
              (9, 'kk2', '123456', '男', '2021-03-24', 20)]
    rowcount = cue.executemany(sql, params)
    conn.commit()
    print('添加成功')
except Exception as e:
    # conn.rollback()
    raise e
# 关闭游标
cue.close()

# 关闭连接
conn.close()
