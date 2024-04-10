Feature: flu-mode
    Background: 启动软件
        Given 启动软件
        And 开始检查

    Scenario Outline: 透视中剂量曝光
        Given 选择透视<fps>,<fov>
        When 踩下脚踏
        Then 曝光开始
        When 持续<press_time>秒,松开脚踏
        Then 曝光结束
        And 自动保存序列
    Examples:
        | fps    | fov    | press_time    |
        | 4 fps     | 30cm*30cm  | 10            |
        | 4 fps     | 20cm*20cm  | 10            |
        | 4 fps     | 15cm*15cm  | 10            |
        | 8 fps      | 30cm*30cm  | 10            |
        | 8 fps      | 20cm*20cm  | 10            |
        | 8 fps      | 15cm*15cm  | 10            |
        | 15 fps     | 30cm*30cm  | 10            |
        | 15 fps     | 20cm*20cm  | 10            |
        | 15 fps     | 15cm*15cm  | 10            |

#    Scenario Outline: 摄影曝光
#        Given 选择摄影<fps>，<fov>
#        When 按下手闸
#        Then 曝光开始
#        When 持续<press_time>秒,松开手闸
#        Then 曝光结束
#    Examples:
#        | fps    | fov    | press_time    |
#        | 8      | 30cm*30cm  | 10            |
#        | 15     | 30cm*30cm  | 10            |
#        | 30     | 30cm*30cm  | 10            |


