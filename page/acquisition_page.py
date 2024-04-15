# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/4/1 15:51
# @Author : yufeng.wang@we-med.com
# @Site :采集界面控件识别
# @File : acquisition_page.py
# @Software : PyCharm

import uiautomation as auto

auto.uiautomation.DEBUG_SEARCH_TIME = True
auto.uiautomation.SetGlobalSearchTimeout(2)


class Acquisition_page:
    """
    采集界面控件识别
    """

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        # 当前打开的窗口中查找复审窗口
        try:
            self.acquisition_windows = auto.WindowControl(Name="复审", Depth=1)
            # self.acquisition_windows.SetTopmost()
            self.acquisition_windows.SetActive(waitTime=5)
            self.acquisition_windows.Refind()
        except Exception as e:
            print(f"捕获异常:{e}")

    def acquisition_page_fps_combox(self):
        """采集帧频下拉框"""
        try:
            return self.acquisition_windows.ComboBoxControl(AutomationId="FluFpsBox")
        except LookupError as e:
            print(f"控件获取失败：{e}")
        except Exception as e:
            print(f"其他异常:{e}")
            return None

    def acquisition_page_fps(self, fps):
        """根据输入的采集帧频识别对应下拉框选项"""
        try:
            return self.acquisition_windows.ListItemControl(Name=f"{fps}")
        except Exception as e:
            print(f"捕获异常:{e}")
            return None

    def acquisition_page_mode_combox(self):
        """采集模式下拉框"""
        try:
            return self.acquisition_windows.ComboBoxControl(AutomationId="FluModeBox")
        except Exception as e:
            print(f"捕获异常:{e}")
            return None

    def acquisition_page_mode(self, mode):
        """
        设置透视采集模式Normal或RoadMap
        :param mode:
        :return:
        """
        try:
            return self.acquisition_windows.ListItemControl(Name=f"{mode}")
        except LookupError as e:
            print(f"控件获取失败：{e}")
        except Exception as e:
            print(f"其他异常:{e}")
            return None

    def acquisition_page_fov_combox(self):
        """
        视野FOV下拉框
        :return:
        """
        try:
            return self.acquisition_windows.ComboBoxControl(AutomationId="FieldCombox")
        except Exception as e:
            print(f"捕获异常:{e}")
            return None

    def acquisition_page_fov(self, fov):
        """
        从fov下拉框选择对应的视野，30、20、15
        :param fov_num:
        :return:
        """
        try:
            return self.acquisition_windows.ListItemControl(Name=f"{fov}")
        except Exception as e:
            print(f"捕获异常:{e}")
            return None

    def acquisition_page_filtration_combox(self):
        """
        采集滤过下拉框
        :return:
        """
        try:
            return self.acquisition_windows.ComboBoxControl(AutomationId="FluFilterBox")
        except Exception as e:
            print(f"捕获异常:{e}")
            return None

    def acquisition_page_vascular_degree(self):
        """
        血管程度滑动按钮
        :return:
        """
        try:
            return self.acquisition_windows.TextControl(Name="血管程度").GetNextSiblingControl().GetChildren()[2]
        except Exception as e:
            print(f"捕获异常:{e}")
            return None


if __name__ == '__main__':
    window = Acquisition_page()
    print(window.acquisition_page_vascular_degree().ClassName)
    print(window.acquisition_page_vascular_degree().Name)
    print(window.acquisition_page_vascular_degree().GetChildren()[2])
