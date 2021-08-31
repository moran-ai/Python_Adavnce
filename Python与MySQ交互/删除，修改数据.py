from pymysql import *

# 创建数据库连接
conn = Connect(host='localhost', user='root', port=3306, password='itcast', db='mytestdb')
# print(conn)
# 打开游标
cue = conn.cursor()
try:
    # 执行sql语句
    # sql = 'delete from student_ where id="%s"'
    sql = 'update  student_ set name=%s where id = %s'
    params = ('李梅', 6)
    rowcount = cue.execute(sql, params)
    conn.commit()
except Exception as e:
    raise e
print(f'数据更新成功,已更新{rowcount}条数据')
# 关闭游标
cue.close()

# 关闭连接
conn.close()
