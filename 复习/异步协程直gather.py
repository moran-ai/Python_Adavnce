import asyncio


async def foo():
    print('这是一个协程')


async def f():
    # await asyncio.sleep(3)
    print('ok')

async def foo1():
    print('这是')

loop = asyncio.get_event_loop()
# lst = [foo(), foo1(), f()]
loop.run_until_complete(asyncio.gather(foo(), f(), foo1()))
