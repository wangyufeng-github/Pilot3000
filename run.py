# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/4/8 9:42
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : run.py
# @Software : PyCharm
# import glob
# from behave.__main__ import main as behave_main
# import datetime
# import os
# import shutil
# if __name__ == '__main__':
#     # 设置执行命令和保存路径
#     code_path = os.path.dirname(os.path.realpath(__file__))
#     os.chdir(code_path)
#     result_folder = "report/"+datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
#     run_cmd = ["-f allure_behave.formatter:AllureFormatter", "-o" + "allure-results"]
#     # 定位feature文件
#     ff = glob.glob(code_path + '/features/{feature_name}.feature'.format(feature_name="flu"))
#     run_cmd.extend(ff)
#     # 通过Behave源码接执行脚本并将结果保存为json文件到allure-results目录下
#     behave_main(run_cmd)
#     # 将json结果转换为html
#     os.system("allure generate --report-dir {folder}/html/ {result} ".format(folder=code_path + "/" + result_folder,result="allure-results"))
#     # 递归删除生成结果目录
#     shutil.rmtree("allure-results")


import os
import subprocess
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.run("pip install -r requirements.txt")


def execute_behave_in_loop(total_execution_time):
    # 获取当前文件所在路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)  # 切换至当前文件路径

    start_time = time.time()

    while (time.time() - start_time) < total_execution_time:
        print("执行中:")

        try:
            subprocess.run(['behave'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"执行 behave 时出错: {e}")
            break

        print("执行完成\n")

    print("执行时间已满，结束执行")


# 调用函数并指定执行时间
execute_behave_in_loop(total_execution_time=300)  # 5分钟
