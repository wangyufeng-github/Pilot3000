# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/5/8 14:55
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : roadmap_mode.py
# @Software : PyCharm

from behave import *
@then(u'开始检查')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then 开始检查')


@given(u'切换视野{fov}')
def step_impl(context,fov):
    raise NotImplementedError(u'STEP: Given 切换视野15cm*15cm')


@given(u'切换RoadMap采集模式')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given 切换RoadMap采集模式')


@when(u'踩下脚踏，持续{first_press_time}秒,提示注射造影剂,松开脚踏')
def step_impl(context,first_press_time):
    raise NotImplementedError(u'STEP: When 踩下脚踏，持续10秒,提示注射造影剂,松开脚踏')


@when(u'再次踩下脚踏,持续{second_press_time}秒, 松开脚踏')
def step_impl(context,second_press_time):
    raise NotImplementedError(u'STEP: When 再次踩下脚踏,持续10, 松开脚踏')

