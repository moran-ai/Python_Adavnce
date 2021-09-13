"""
@Author:hu
@Time:2021/9/11 20:40 
@File:捕获异常.py
@Software: PyCharm
"""
import logging
from logging.handlers import RotatingFileHandler

"""
捕获异常是用try except的结构
"""

'https://blog.csdn.net/pansaky/article/details/90710751'

# 创建一个logger对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建一个日志回滚处理器
r_logger = RotatingFileHandler(filename='log2.txt', maxBytes=3 * 1024, backupCount=3, encoding='utf-8')
r_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -- %(levelname)s -- %(name)s -- %(message)s')
r_logger.setFormatter(formatter)

# 创建一个打印到控制台的处理器
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# 日志添加处理器
logger.addHandler(r_logger)
logger.addHandler(console)

# 输出信息
logger.info('start')
logger.debug('do')
logger.warning('something')

# 捕获异常
try:
    open('test.txt', 'r')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    # exc_info=True 输出异常信息 stack_info=True 输出对应的堆栈信息
    # logger.error('Faild to open test.txt from logger.error', exc_info=True)
    logger.exception('Faild to open test.txt from logger.exception', stack_info=True)
logger.info('finish')
