import asyncio


async def func(x, y):
    resutl = await fun(x, y)  # 让下一个协程进行计算
    print(f'{x}+{y}的值是：{resutl}')


async def fun(x, y):
    print(f'开始计算：{x} + {y}')
    await asyncio.sleep(1)
    return x + y


loop = asyncio.get_event_loop()
loop.run_until_complete(func(1, 2))
loop.close()
