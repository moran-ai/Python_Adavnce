import re

tel_l = """
aafasdfasdf
13456789123
fgsfgs
13456789156
"""
tel_2 = '13456789156rfafda'
# compile 返回第一个匹配的结果
patttern = re.compile('1[3,9]\d{9}')
result = patttern.search(tel_l)
print(result.group(0))
print(result.span(0))
print(result.pos, result.endpos)

# match从匹配字符串的第一个字符开始
# result2 = patttern.match(tel_2)
# print(result2.group(0))
