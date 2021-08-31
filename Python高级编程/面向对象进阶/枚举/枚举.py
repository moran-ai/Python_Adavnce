from enum import Enum

# 枚举：一个名字对应一个值 类似于字典
# Month是抬头，可以省略
Month = Enum('Month', ('一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'))


# 拿到枚举里的所有数据
print(Month.__members__)  # 枚举中的值从1开始，不会重复

# 通过名字获取值
print(Month['二'].value)
# 通过值获取名字
print(Month(2).name)


# # 自定义一个颜色枚举类
class Color(Enum):
    """
    不允许key和value重复，如果重复根据value取name，只会返回第一个name
    """
    red = 200
    yellow = 100
    orange = 300
    blue = 200


# 枚举成员可以同一性，等值比较，但是不能进行大小比较
print(Color.red is Color.yellow)
print(Color.red == Color.blue)
