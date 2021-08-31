import asyncio


async def fun1():
    for i in range(5):
        print("协程a执行")
        await asyncio.sleep(1)


async def fun2():
    for i in range(5):
        print("协程b执行")
        await asyncio.sleep(2)


# 创建协程事件循环
loop = asyncio.get_event_loop()

# 运行协程
loop.run_until_complete(asyncio.gather(fun1(), fun2()))
loop.close()
