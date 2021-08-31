import requests
import pprint
import parsel
import openpyxl
import concurrent.futures  # 池子模块, 内置模块
import time
import threading

workbook = openpyxl.Workbook()
sheet = workbook.create_sheet('小说内容', 0)
sheet.append(['评论', '用户名', '点赞数'])


def get_data(url, count=None):
    # page_url ='https://read.qidian.com/chapter/TtxVU3dYVW81/hk--Zu49t5cex0RJOkJclQ2/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        , 'referer': url
    }
    page_html = requests.get(url=url, headers=headers).text
    # print(page_html)
    selector = parsel.Selector(page_html)
    next_page = selector.css('#j_chapterNext::attr(href)').get()
    chapterId = selector.css('.main-text-wrap .book-mark::attr(data-cid)').get()
    # print(chapterId)
    for segmentId in range(-1, 70):
        for i in range(1, 91):
            comment_url = 'https://read.qidian.com/ajax/chapterReview/reviewList?_csrfToken=wrs224fgbti32t1vkS9ZwcbZxPHyHrfgYgrkSCTW&bookId=1887208&chapterId={}&segmentId={}&type=2&page={}&pageSize=20'.format(
                chapterId, segmentId, i)
            comment_data = requests.get(url=comment_url, headers=headers).json()
            # print(comment_data)
            if comment_data['msg'] == 'success' and comment_data['data'].get('list'):
                comment_naval = comment_data['data']['list']
                for i in comment_naval:
                    comment = i['content']
                    nick_name = i['nickName']
                    like_count = i['likeCount']
                    print(comment, nick_name, like_count)
                    sheet.append([comment, nick_name, like_count])
    # print(next_page)
    while count < 2:
        count += 1
        if next_page:
            next_url = 'https:' + next_page
            print(count, next_url)
            return get_data(next_url, count)


# start_time = time.time()
# get_thread = threading.Thread(target=get_data,
#                      args=('https://read.qidian.com/chapter/TtxVU3dYVW81/hk--Zu49t5cex0RJOkJclQ2/',),
#                      kwargs={'count': 0}
#                      )
# get_thread.start()
# print(threading.enumerate())

# a=get_data('https://read.qidian.com/chapter/TtxVU3dYVW81/hk--Zu49t5cex0RJOkJclQ2/',0)
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     executor.submit(get_data, 'https://read.qidian.com/chapter/TtxVU3dYVW81/hk--Zu49t5cex0RJOkJclQ2/', count=0)
# # print('总共花费时间',start_time-time.time())
# print(start_time)
# workbook.save('起点中文网小说评论内容0000.xlsx')
# print('总共花费时间', time.time() - start_time)

a = [1]
b = [1]
print(id(a))
print(id(b))
