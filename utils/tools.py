# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/4/11 14:30
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : tools.py
# @Software : PyCharm
import win32con
import win32gui
import pygetwindow as gw


class Tools(object):
    def __init__(self):
        pass

    def get_handle_by_title(self,title):
        """
        获取窗口句柄
        :param title: 窗口标题
        :return: 窗口句柄
        """
        try:
            window = gw.getWindowsWithTitle(title)[0]
            return window._hWnd
        except IndexError:
            return None

