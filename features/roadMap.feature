# Created by WM10266 at 2024/5/8
Feature: Roadmap路径图采集模式
  # Enter feature description here
  Background: 前置条件
    Given 启动软件
    Then 开始检查

  Scenario Outline: 不同视野下的曝光
    Given 切换视野<fov>
    And 切换RoadMap采集模式
    When 踩下脚踏，持续<first_press_time>秒,提示注射造影剂,松开脚踏
    And 再次踩下脚踏,持续<second_press_time>秒, 松开脚踏
    Then 曝光结束
    And 自动保存序列
    Examples:
      |fov|first_press_time|second_press_time|
      |15cm*15cm|10|10|
      |20cm*20cm|10|10|
      |30cm*30cm|10|10|

