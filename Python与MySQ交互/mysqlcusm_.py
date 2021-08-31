from Python与MySQ交互.mysql_cusm import *

mysqlcusm = Mysqlhelp(Mysqlhelp.connect_params)
# 插入数据
# sql = 'insert into student_ values (%s,%s,%s,%s,%s,%s)'
# params = [(11, '北京', '986499', '男', '2021-10-12', 345), (12, '上海', '986499', '男', '2021-10-12', 345)]
# rowcont = mysqlcusm.insert_many(sql, params)
# print(f'成功插入{rowcont}条数据')

# 修改数据
# sql = 'update student_ set name=%s where id=%s'
# pararms = ('深圳', 11)
# rowcount = mysqlcusm.update(sql,pararms)
# print(f'成功修改{rowcount}条数据')

# 删除数据
# sql = 'delete from student_ where id=%s'
# params=(9)
# rowcount = mysqlcusm.delete(sql,params)
# print(f'成功删除{rowcount}条数据')

# 查询
sql = 'select name,age,sex from student_ where age>%s'
params = (19)
rowcount = mysqlcusm.get_all(sql, params)
for row in rowcount:
    print(row)
