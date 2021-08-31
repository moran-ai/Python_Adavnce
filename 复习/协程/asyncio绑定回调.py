import asyncio
from functools import partial

"""
回调的最后一个参数是future对象，通过这个对象可以获取协程的返回值，如果回调函数需要传递多个参数，可以使用偏函数
"""


async def func(x):
    for i in range(3):
        print(f'work is {x}')
    return f'work finished {x}'


coroutine = func(1)

# 创建事件循环
loop = asyncio.get_event_loop()
# 创建task对象
task = asyncio.ensure_future(coroutine)
# task对象添加回调函数
# 事件循环执行
loop.run_until_complete(task)  # 返回后的结果
print(task.result())
