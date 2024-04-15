# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/4/11 14:30
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : tools.py
# @Software : PyCharm
import win32con
import win32gui


class Tools(object):
    def __init__(self):
        pass

    def activate_window(window_title):
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 将窗口还原（如果最小化）
            win32gui.SetForegroundWindow(hwnd)  # 设置窗口为前台窗口（激活窗口）
        else:
            print(f"Window with title '{window_title}' not found.")


if __name__ == '__main__':
    # 调用函数获取所有窗口句柄
    window_handles = Tools().get_all_window_handles()
    # 遍历所有窗口句柄，并打印窗口标题
    for window_handle in window_handles:
        window_title = win32gui.GetWindowText(window_handle)
        print(window_title)
