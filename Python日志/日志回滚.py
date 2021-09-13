"""
@Author:hu
@Time:2021/9/11 18:19 
@File:日志回滚.py
@Software: PyCharm
"""
import logging
from logging.handlers import RotatingFileHandler

"""
Python中的日志回滚使用模块RotatingFileHandler
这个模块可以用来设置日志文件的大小和日志文件备份的数量
"""

# 创建一个logger对象
logger = logging.getLogger(__name__)
# 设置logger对象的级别
logger.setLevel(logging.DEBUG)

# 创建日志回滚对象
"""
RotatingFileHandler
"""
r_logger = RotatingFileHandler('log_.txt', maxBytes=2 * 1024, backupCount=3, encoding='utf-8')
r_logger.setLevel(logging.INFO)
# 设置格式
formatter = logging.Formatter('%(asctime)s -- %(levelname)s -- %(name)s -- %(message)s')
# 添加格式
r_logger.setFormatter(formatter)

# 打印到控制台的信息
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# 日志对象添加处理方式
logger.addHandler(r_logger)
logger.addHandler(console)

# 添加信息
logger.info('start')
logger.debug('do')
logger.warning('something')
logger.error('finish')
