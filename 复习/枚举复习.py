from enum import Enum

month = Enum('', ('一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'))
print(month.__class__.__class__)
print(month.__members__)  # 获取所有的数据
print(month['一'].value)  # 通过键获取值
print(month(3).name)  # 通过值获取键


# 通过继承Enum的方式创建
class M(Enum):
    red = 1
    orange = 4


m = M(4)
print(m)
