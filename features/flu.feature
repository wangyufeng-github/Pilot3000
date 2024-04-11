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

    Scenario Outline: 透视低剂量曝光
        Given 打开设置界面
        Then 点击低剂量
        And 关闭设置界面
        Given 选择透视<fps>,<fov>
        When 踩下脚踏
        Then 曝光开始
        When 持续<press_time>秒,松开脚踏
        Then 曝光结束
        And 自动保存序列
        Examples:
            | fps   | fov       | press_time |
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10

    Scenario Outline: 透视高剂量曝光
        Given 打开设置界面
        Then 点击高剂量
        And 关闭设置界面
        Given 选择透视<fps>,<fov>
        When 踩下脚踏
        Then 曝光开始
        When 持续<press_time>秒,松开脚踏
        Then 曝光结束
        And 自动保存序列
        Examples:
            | fps   | fov       | press_time |
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10
            | 4 fps | 30cm*30cm | 10

    Scenario: Roadmap曝光采集
        Given 切换Roadmap采集模式
        When 踩下脚踏
        Then 曝光开始
        When 持续<press_time>秒,松开脚踏
        Then 曝光结束
        And 自动保存序列