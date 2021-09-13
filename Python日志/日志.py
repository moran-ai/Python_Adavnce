"""
@Author:hu
@Time:2021/9/10 19:37 
@File:日志.py
@Software: PyCharm
"""
import logging

# print(logging.getLevelName(10))
# print(logging.getLevelName(logging.DEBUG))
#
# print(logging.getLevelName(40))
# print(logging.getLevelName(logging.ERROR))
# logging.shutdown()
# # 日志打印到屏幕
# print(logging.info('info'))
# print(logging.debug('debug'))
# print(logging.warning('警告'))
# print(logging.error('错误'))

"""
asctime:日志时间
name:当前文件的__name__属性值
levelname:日志名字
message:日志信息
filename:输出日志到指定的文件
filemode:文件模式。默认为a,可以进行修改w
"""
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', filename='a.txt')
logger = logging.getLogger(__name__)
logger.info('start print log')
logger.debug('do something')
logger.warning('something maybe fail')
logger.error('finsh')
