"""
@Author:hu
@Time:2021/9/10 22:33 
@File:日志写入文件.py
@Software: PyCharm
"""
import logging

"""
日志写入文件

创建logger对象和handler对象
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 设置logger的日志级别
handler = logging.FileHandler('log.txt')  # 创建处理器handler
handler.setLevel(logging.INFO)  # 设置handler的日志级别
# 日志格式
formatter = logging.Formatter('%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
handler.setFormatter(formatter)  # handler对象添加日志格式
logger.addHandler(handler)  # logger对象添加handler处理器

# 添加信息
logger.info('start print log 开始')
logger.debug('do something')
logger.warning('something')
logger.error('finish')
