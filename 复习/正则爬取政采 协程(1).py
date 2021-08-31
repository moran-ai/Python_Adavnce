import requests
import re
from lxml import etree
from openpyxl import load_workbook
import asyncio

'''code_list=[201,203]
for num in code_list:
    print('当前id号为:%d'%num)'''


async def get_page_url(count):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
    url = 'http://www.zhengcaimall.com/list?categoryId={}&brandId=&attrval=&price=&sort=0&page={}'.format(167, count)
    resp = requests.get(url, headers=headers)
    return resp.text


async def get_detail_url(num):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
    url_detail = 'http://www.zhengcaimall.com' + num
    data = requests.get(url_detail, headers=headers)
    return data


async def main1():
    count = 1
    for i in range(2):
        # try:
        print('当前页数为:%d' % count)
        html_content = await get_page_url(count)
        count += 1
        pattern = re.compile(r'<a class="sellPoint" title=""\s*href="(.*?)"\s*target="_blank">', re.S)  # 设定正则规则
        result_list = pattern.findall(html_content.replace('\r\n', ''))  # 获得了所有id号 例/detail/10201810020545
        infomation_list = []
        for i in result_list:
            data = await get_detail_url(i)
            response = etree.HTML(data.content.decode('utf-8'))
            try:
                # detail = response.xpath("//p[@class='m-detail-right-title']/text()")[0]
                price = response.xpath("//span[@class='m-detail-right-line-coin sys_item_price']/text()")[0]
                brand = response.xpath("//p[@class='m-detail-right-line'][1]/text()")[1]
                first = response.xpath("//div[@class='w'][1]//a[2]//text()")[1]
                second = response.xpath("//div[@class='w'][1]//a[3]//text()")[1]
                third = response.xpath("//div[@class='w'][1]//a[4]//text()")[1]
                # infomation_list.append([detail, price, brand, first, second, third])
                print(price)
            except:
                continue


async def main2():
    count = 101
    for i in range(3):
        # try:
        print('当前页数为:%d' % count)
        html_content = await get_page_url(count)
        count += 1
        pattern = re.compile(r'<a class="sellPoint" title=""\s*href="(.*?)"\s*target="_blank">', re.S)  # 设定正则规则
        result_list = pattern.findall(html_content.replace('\r\n', ''))  # 获得了所有id号 例/detail/10201810020545
        infomation_list = []
        for i in result_list:
            data = await get_detail_url(i)
            response = etree.HTML(data.content.decode('utf-8'))
            try:
                detail = response.xpath("//p[@class='m-detail-right-title']/text()")[0]
                # price = response.xpath("//span[@class='m-detail-right-line-coin sys_item_price']/text()")[0]
                # brand = response.xpath("//p[@class='m-detail-right-line'][1]/text()")[1]
                # first = response.xpath("//div[@class='w'][1]//a[2]//text()")[1]
                # second = response.xpath("//div[@class='w'][1]//a[3]//text()")[1]
                # third = response.xpath("//div[@class='w'][1]//a[4]//text()")[1]
                # infomation_list.append([detail, price, brand, first, second, third])
                print(detail)
            except:
                continue


loop = asyncio.get_event_loop()
# lst = [main1(), main2()]
loop.run_until_complete(asyncio.gather(main2(), main1()))
loop.close()
