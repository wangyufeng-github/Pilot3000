# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/4/11 14:30
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : tools.py
# @Software : PyCharm
import win32gui


class Tools(object):
    def __init__(self):
        pass

    def get_window_handle(self, window_name):
        """
        获取窗口句柄
        :param window_name:
        :return:
        """
        hwnd = win32gui.FindWindow(None, window_name)
        return hwnd

    def set_window_handle(self, window_handle):
        # 通过句柄将窗口放到最前
        win32gui.SetForegroundWindow(window_handle)

    def get_all_window_handles(self):
        # 定义一个列表，用于存储所有窗口句柄
        window_handles = []
        # 遍历所有打开的窗口，并将窗口句柄添加到列表中
        for window in win32gui.EnumWindows(None):
            window_handles.append(window)
        # 返回所有窗口句柄
        return window_handles


if __name__ == '__main__':
    # 调用函数获取所有窗口句柄
    window_handles = Tools().get_all_window_handles()
    # 遍历所有窗口句柄，并打印窗口标题
    for window_handle in window_handles:
        window_title = win32gui.GetWindowText(window_handle)
        print(window_title)
