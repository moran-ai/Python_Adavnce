import time
import re
import asyncio
import aiohttp
import os
import aiofiles
from fake_useragent import UserAgent
from tqdm import tqdm

"""
pip install aiofiles 用来异步执行文件保存操作 with  async with aiofiles.open() as f: await f.write()
pip install aiohttp  Python异步请求库，是由asyncio编程的http框架,用来发送异步请求
使用asyncio异步爬取小说
使用async定义一个协程对象
使用await用来中断协程或者启动协程

启动协程的方式：
    ① 通过asyncio直接进行run
        asyncio,.run(func)
    ② 通过task+事件循环+对象
    ③ 事件循环+run_until_complete
"""
headers = {
    'UserAgent': str(UserAgent().random)
}
path = '小说'
if not os.path.exists(path):
    os.mkdir(path)


async def get_response(url):
    """
    获取首页的内容
    :param url:
    :return:
    """
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url, headers=headers) as response:
            code = response.status
            assert code == 200, '状态码不为200'  # 使用assert进行断言，如果为True则继续向下执行，否则抛出自定义的异常
            html = await response.text(encoding='utf-8')  # await用来获取返回值，等待一个协程执行完毕
            return html


async def get_detial_data():
    """
    获取小说详情页和详情页url
    :return:
    """
    url = 'http://www.ptshu.com/9940/'
    html = await get_response(url)
    # 获取章节标题
    # titles = re.findall('<dd>.*?<a.*?>(.*?)</a>.*?</dd>', html, re.S)

    # 获取章节链接
    urls = re.findall('<dd>.*?<a.*?href="(.*?)".*?>.*?</dd>', html, re.S)
    for u in urls:
        async with aiohttp.ClientSession() as session:
            async with await session.get(url='http://www.ptshu.com' + u, headers=headers) as response:
                assert response.status == 200, '详情code不为200'
                response_content = await response.text(encoding='utf-8')
                # 获取内容
                contents = re.findall('<div.*?class="readcontent".*?>(.*?)</div>', response_content, re.S)
                # 获取标题
                titles = re.search('<h1.*?class="pt10">(.*?)</h1>', response_content)
                title = titles.groups()[0].replace('（1 / 2）', '').replace('（1 / 1）', '').replace(' ', '').replace('?',
                                                                                                                  '')
                start_time = time.time()
                print(f'正在爬取----->{title}')
                for content in contents:
                    c = content.replace('</p>', '').replace('<p>', '').replace('<a style="font-size:18px;"',
                                                                               '').replace('href="javascript:$',
                                                                                           '').replace(
                        "('body,html').animate({scrollTop:0},100);", '').replace('">↑返回顶部↑</a>', '')
                    async with aiofiles.open(path + f'/{title}.txt', 'w', encoding='utf-8') as file:
                        await file.write(title + '\n' + c)
                        print(f'{title}爬取完成')
                finsh_time = time.time() - start_time
    print(f'最终完成时间是{finsh_time}')


if __name__ == '__main__':
    asyncio.run(get_detial_data())
