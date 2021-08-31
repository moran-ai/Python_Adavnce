"""
使用async关键字定义一个协程对象
await用于挂起阻塞的异步调用接口
"""
import asyncio


async def fun():
    for i in range(10):
        print(f'this is {i}')
        await asyncio.sleep(1)


coroutine = fun()  # 协程对象
if __name__ == '__main__':
    # 方式一
    loop = asyncio.get_event_loop()  # 创建事件循环
    loop.run_until_complete(coroutine)  # 将协程对象加入到事件循环中，并执行

    # 方式二  这是Python3.7以后的协程调用
    asyncio.run(coroutine)  # 创建一个新的事件循环，以coroutine为程序的入口，执行完毕后关闭事件循环
