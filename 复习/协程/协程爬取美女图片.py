import aiohttp
import aiofiles
import re
import asyncio
from fake_useragent import UserAgent
from tqdm import tqdm

headers = {
    'User-Agent': str(UserAgent().random)
}


async def get_index():
    """
    获取首页
    首页url: https://www.ku66.net/r/2/index.html
    :return:
    """
    url = 'https://www.ku66.net/r/2/index.html'
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url, headers=headers) as response:
            code = response.status
            assert code == 200, '状态码不为200'
            html = await response.text()
            return html


async def get_category():
    """
    获取图片的类别和类别的url
    :return:
    """
    html = await get_index()
    # # 类别69个
    # # 获取对应的url
    pattern = re.compile('<div.*?class="w850 l oh">(.*?)</div>', re.S)
    data = re.findall(pattern, html)
    urls = []
    names = []
    for d in data:
        name_list = re.findall('<a.*?>(.*?)</a>', d)
        url_list = re.findall("<a.*?href=('.*?')>", d)
        for name in name_list:
            names.append(name)
        for url in url_list:
            urls.append(url.replace("'", ''))
    return urls


async def get_image_page():
    """
    获取详情页的图片，返回详情页的所有url
    :return:
    """
    image_page_urls = []
    urls = await get_category()
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with await session.get(url=url, headers=headers) as response:
                code = response.status
                assert code == 200, '图片状态码不为200'
                html = await response.text(encoding='gbk')

                # 获取分页
                image_url_page = re.findall(
                    '<div.*?class="NewPages">.*?<ul>(.*?)</ul>.*?</div>',
                    html, re.S)
                pattern = re.compile("<a.*?href='(.*?)'.*?>", re.S)
                for img_url in image_url_page:  # 获取所有的分页
                    # print(img_url)
                    image_page = re.findall(pattern, img_url)
                    for im_page in image_page:
                        # 对url进行处理，获取分页的url
                        im = im_page.split('_')[1]  # https://www.ku66.net/r/5/list_5_3.html
                        img_pa = im_page.split('_')[2]
                        # 分页的url
                        im_url = f'https://www.ku66.net/r/{im}/list_{im}_{img_pa}'
                        image_page_urls.append(im_url)
    return image_page_urls


async def get_image():
    """
    获取详情页的所有图片
    :return:
    """
    url = await get_image_page()
    for u in url:
        # print(u)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=u, headers=headers) as response:
                assert response.status == 200, '获取图片状态码不为200'
                html = await response.text()
        # 获取每一个页面的图片url
        image_urls = re.findall('<a.*?href="(.*?)".*?class="TypeBigPics".*?>', html)
        image_names = re.findall('<div.*?class="ListTit".*?>(.*?)</div>', html)


async def get_image_():
    """
    获取所有第一页的详情页的图片
    :return:
    """
    image_url = []
    urls = await get_category()
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with await session.get(url=url, headers=headers) as response:
                code = response.status
                assert code == 200, '图片状态码不为200'
                html = await response.text(encoding='gbk')
                # 获取每一个页面的图片url
                image_urls = re.findall('<a.*?href="(.*?)".*?class="TypeBigPics".*?>', html)
                image_names = re.findall('<div.*?class="ListTit".*?>(.*?)</div>', html)
                image_url.append(image_names)
                # print(image_urls)
    return image_url


async def get_detail_image():
    url = await get_image_()
    print(url)
    # for u in url:
    #     print(u)
    # pass

# if __name__ == '__main__':
#     asyncio.run(get_detail_image())

# -*- encoding: GBK -*-
