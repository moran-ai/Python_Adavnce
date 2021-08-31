import aiohttp
import aiofiles
import re
import os
import asyncio
from fake_useragent import UserAgent
from tqdm import tqdm

headers = {
    'User-Agent': str(UserAgent().random)
}

# 存储图片的位置
path = '图片'
if not os.path.exists(path):
    os.makedirs(path)

path_name = '美女图片'
if not os.path.exists(path_name):
    os.mkdir(path_name)

path_name_ = '美女图片1'
if not os.path.exists(path_name_):
    os.mkdir(path_name_)


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
    # print(names)
    return urls


async def get_image_page():
    """
    获取详情页的图片，返回详情页的所有url
    :return:
    """
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
                    image_page = re.findall(pattern, img_url)  # 分页
                    for im_page in image_page:
                        # 对url进行处理，获取分页的url
                        im = im_page.split('_')[1]  # https://www.ku66.net/r/5/list_5_3.html
                        img_pa = im_page.split('_')[2]
                        # 分页的url  进行分页的url的拼接
                        im_url = f'https://www.ku66.net/r/{im}/list_{im}_{img_pa}'
                        async with await session.get(url=im_url, headers=headers) as response_1:
                            assert response_1.status == 200, '详情页图片状态码不为200'
                            html = await response_1.text(encoding='gbk')
                            # 获取详情页的url
                            url_list = re.findall('<a.*?href="(.*?)".*?class="TypeBigPics".*?>', html)
                            # 对详情页发送请求
                            for url_ in url_list:
                                async with await session.get(url=url_, headers=headers) as response_2:
                                    assert response_2.status == 200, '详情页状态码不为200'
                                    html_ = await response_2.text(encoding='gbk')
                                    page_urls = re.findall(
                                        '<div.*?class="NewPages">.*?<ul>(.*?)</ul>.*?</div>',
                                        html_, re.S)
                                    for page_url in page_urls:
                                        page_url_list = re.findall("<li>.*?<a.*?href='(.*?)'>.*?</a>.*?</li>", page_url,
                                                                   re.S)
                                        for page_url_ in page_url_list:
                                            # print(page_url)
                                            # print(url_.split('/')[-1].split('.')[0])
                                            if page_url_ == '#':
                                                page_url_ = page_url_.replace('#',
                                                                              url_.split('/')[-1].split('.')[
                                                                                  0] + '.html')
                                            # 进行详情页分页url的处理
                                            page_url_1 = url_.replace(url_.split('/')[-1], page_url_)
                                            # print(page_url_1)
                                            async with await session.get(page_url_1) as response_3:
                                                assert response_3.status == 200, '图片下载状态码不为200'
                                                html_1 = await response_3.text(encoding='gbk')
                                                # 爬取到的图片链接地址
                                                images_list = re.findall(
                                                    '<img.*?src="(.*?)".*?class="tupian_img".*?>',
                                                    html_1)
                                                # name_list = re.search('<img.*?alt="(.*?)".*?class="tupian_img".*?>',
                                                #                        html_1)
                                                flag = 1
                                                # print(name_list.groups())
                                                # for name_ in name_list:
                                                #
                                                #     # print(images_list)
                                                # name = re.search(
                                                #     '<div.*?class="ArticleTitle">.*?<strong>(.*?)</strong>.*?</div>',
                                                #     html_1, re.S)
                                                # print(name)
                                                name = re.findall(
                                                    '<div.*?class="ArticleTitle">.*?<strong>(.*?)</strong>.*?</div>',
                                                    html_1, re.S)
                                                #     # print(name)
                                                name_ = re.search(
                                                    '<div.*?class="ArticleTitle">.*?<strong>(.*?)</strong>.*?</div>',
                                                    html_1, re.S)
                                                # print(name.groups()[0])
                                                #     # image_name_ = name.groups()[0].replace(' ', '')
                                                alist = name
                                                # print(alist)
                                                bar = tqdm(alist)
                                                for leeter in bar:
                                                    # print(leeter)
                                                    bar.set_description(f'正在爬取--->{leeter}')
                                                # print(f'正在爬取--->{image_name_}')
                                                # for n in name:
                                                #     # print(n)
                                                #     # print(f'正在爬取{image_name_}')
                                                for image_url in images_list:
                                                    n = f'{name_.groups()[0].replace(" ", "")}{flag}.jpg'
                                                    # print(n)
                                                    flag += 1
                                                    image_name = image_url.split('/')[-1]
                                                    # 对图片链接发送请求
                                                    async with session.get(url=image_url,
                                                                           headers=headers) as response_4:
                                                        assert response_4.status == 200, '下载图片状态码不为200'
                                                        # 下载图片
                                                        content = await response_4.read()
                                                        # path_ = f"{path}/{n}"
                                                        # if not os.path.exists(path_):
                                                        #     os.makedirs(path_)
                                                        # async with aiofiles.open(path + f'/{n}/{image_name}',
                                                        #                          'wb') as file:
                                                        #     await file.write(content)
                                                        async with aiofiles.open(
                                                                path_name_ + f'/{n}',
                                                                'wb') as file:
                                                            await file.write(content)
                                                            print(f'{n}爬取完成')


if __name__ == '__main__':
    asyncio.run(get_image_page())
    asyncio.run(get_category())
