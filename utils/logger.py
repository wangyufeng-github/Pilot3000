# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/5/8 15:26
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : logger.py
# @Software : PyCharm
import os
import logging
from datetime import datetime


class Logger:
    def __init__(self, log_dir='logs'):
        self.log_dir = log_dir
        self.setup_logger()

    def setup_logger(self):
        # 创建日志文件夹
        logs_dir = os.path.join(os.path.dirname(os.getcwd()), self.log_dir)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        # print(logs_dir)
        # 获取当前时间并格式化为字符串
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # 设置日志文件路径
        self.filename = f"behave_{current_time}.log"
        self.filepath = os.path.join(logs_dir, self.filename)

        # 设置日志记录器
        logging.basicConfig(filename=self.filepath, level=logging.INFO)

    def log_error(self, message):
        logging.error(message)

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_debug(self, message):
        logging.debug(message)


if __name__ == '__main__':
    log = Logger()
    log.setup_logger()
    print(os.path.dirname(os.getcwd()))
