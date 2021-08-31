"""
找出满足a+b+c=1000，并且a^2+b^2=c^2的所有组合
方法一：
    使用枚举法
"""
import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(f'组合{a},{b},{c}满足条件')

print(f'程序结束时间为{time.time() - start_time}')
