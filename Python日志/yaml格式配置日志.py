"""
@Author:hu
@Time:2021/9/12 14:54 
@File:yaml格式配置日志.py
@Software: PyCharm
"""
import yaml
import logging.config

"""
使用yaml配置日志
"""

with open('log.yaml', 'r', encoding='utf-8') as f:
    config = yaml.load(f)
logging.config.dictConfig(config)

logger = logging.getLogger('mylogger')
logger.info('start')
