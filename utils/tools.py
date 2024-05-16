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
import uiautomation as auto


class Tools(object):
    def __init__(self):
        pass

    def get_handle_by_title(self,title):
        # 用于根据窗口标题获取窗口句柄的函数
        window = auto.WindowControl(searchDepth=1, Name=title)
        if window.Exists(0, 0):
            return window.NativeWindowHandle
        else:
            raise ValueError(f"窗口 '{title}' 未找到")


if __name__ == '__main__':
    pass
