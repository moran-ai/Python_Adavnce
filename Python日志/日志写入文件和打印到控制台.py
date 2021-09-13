"""
@Author:hu
@Time:2021/9/10 22:50 
@File:日志写入文件和打印到控制台.py
@Software: PyCharm
"""
import logging

"""
需要写入到文件，并打印到控制台
写入文件使用FileHandler处理器
打印到控制台使用StreamHandler处理器
需要分别创建两个对象，logger对象需要添加这个两个对象
"""
# 创建Logger对象
logger = logging.getLogger(__name__)
# 设置日志级别
logger.setLevel(logging.DEBUG)

# 创建handler对象，用于输出到文件中
handler = logging.FileHandler('log1.txt')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
handler.setFormatter(formatter)

# 创建console对象，用于将日志输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# logger添加handler和console对象
logger.addHandler(handler)
logger.addHandler(console)

# 输入信息
logger.info('start')
logger.debug('do')
logger.warning('something')
logger.error('finish')
