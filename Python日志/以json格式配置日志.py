"""
@Author:hu
@Time:021/9/12 11:03
@File:以json格式配置日志.py
@Software: PyCharm
"""
import json
import logging.config

"""
可以通过json文件的格式来配置日志文件
"""

# 读取创建的json文件
with open('log1.json', 'r') as f:
    con = json.load(f)
logging.config.dictConfig(con)

logger = logging.getLogger('my_logger')
logger.info('start')
logger.error('finish')
