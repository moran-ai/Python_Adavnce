import asyncio

"""
协程对象被创建以后不能直接运行，需要注册到事件循环，在注册到事件循环时，也就是将协程对象封装为一个task对象
task对象是Future对象的子类，保留了协程运行后的状态。用于未来获取协程的结果
"""


async def fun():
    for i in range(10):
        print(i)


coroutine = fun()

loop = asyncio.get_event_loop()  # 创建事件循环
task = loop.create_task(coroutine)  # 创建一个task
# task = asyncio.ensure_future(coroutine)  # 这样也可以创建一个task
print('运行前task----->', task)
loop.run_until_complete(task)  # run_until_complete方法接受的是一个task对象或者协程对象,返回finished后的结果
print('运行后task----->', task)

print(isinstance(task, asyncio.Future))  # isinstance()判断一个对象是否是一个已知类型,返回值为boolean
