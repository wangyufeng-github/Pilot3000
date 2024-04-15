# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/4/2 11:41
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : flu_mode.py
# @Software : PyCharm
import time

from behave import *

from common.operate_window import OperateWindow
from page.acquisition_page import Acquisition_page


@given(u'启动软件')
def step_impl(context):
    context.review_window = Acquisition_page()
    context.control_window = OperateWindow().recognition_window("运动控制")


@given(u'开始检查')
def step_impl(context):
    pass


@given(u'选择透视{fps},{fov}')
def step_impl(context, fps, fov):
    # 激活窗口
    context.review_window.SetActive(waitTime=0.5)
    # 点击模式下拉框
    context.review_window.acquisition_page_mode_combox().Click(waitTime=0.5)
    # 选择Normal模式
    context.review_window.acquisition_page_mode("Normal").Click(waitTime=0.5)
    # 点击FOV下拉框
    context.review_window.acquisition_page_fov_combox().Click(waitTime=0.5)
    # 选择对应fov
    context.review_window.acquisition_page_fov(fov).Click(waitTime=0.5)
    # 点击fps下拉框
    context.review_window.acquisition_page_fps_combox().Click(waitTime=0.5)
    # 选择对应fps
    context.review_window.acquisition_page_fps(fps).Click(waitTime=0.5)


@when(u'踩下脚踏')
def step_impl(context):
    # 识别控制软件窗口中脚闸按钮
    context.control_window.SetActive(waitTime=0.5)
    footbrake_button = context.control_window.CheckBoxControl(Name="脚闸")
    footbrake_button.Click()


@then(u'曝光开始')
def step_impl(context):
    pass


@when(u'持续{press_time}秒,松开脚踏')
def step_impl(context,press_time):
    context.control_window.SetActive(waitTime=0.5)
    footbrake_button = context.control_window.CheckBoxControl(Name="脚闸")
    # 踩下脚闸延时
    time.sleep(int(press_time))
    # 松开脚闸
    footbrake_button.Click()


@then(u'曝光结束')
def step_impl(context):
    pass


@then(u'自动保存序列')
def step_impl(context):
    pass
