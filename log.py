#-*- coding: UTF-8 -*-
import logging

'''
日志类：
logger.info("start print log")
logger.debug("Do somerthing")
logger.warning("Something maybe fail.")
logger.info("Finlish")
'''

#生成，日志类
class Logging(object):

    def __init__(self, path):
        self._path = path

    @staticmethod
    def write_logging():
        logging.basicConfig(
            level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
            format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
            datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
            filename="D:/Locust/log/LOG.LOG",  # log文件名
            filemode='w')

        return logging

