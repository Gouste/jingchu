# -*- encoding=utf8 -*-
__author__ = "mac"
# liwueiliuwei

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/8e36cb87?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


# 点击swap按钮
touch(Template(r"swap_tab.png", record_pos=(0.004, 0.964), resolution=(1080, 2340)))
sleep(3)

# 断言，界面展示闪兑按钮
assert_exists(Template(r"swap_assert1.png", record_pos=(0.001, 0.048), resolution=(1080, 2340)), "展示闪兑按钮")

# 点击兑换币种
touch(Template(r"swap_receive_frame.png", record_pos=(0.248, -0.625), resolution=(1080, 2340)))

# 断言，弹出兑换币种弹窗
assert_exists(Template(r"swap_assert2.png", record_pos=(0.2, -0.769), resolution=(1080, 2340)), "展示兑换字段")
sleep(2)
# 点击兑换币种
touch(Template(r"swap_receive_token.png", record_pos=(-0.342, -0.558), resolution=(1080, 2340)))
sleep(2)

#点击输入框
touch(Template(r"swap_amount.png", record_pos=(-0.131, -0.308), resolution=(1080, 2340)))
# 输入数量
text("1")

# 断言。界面展示
assert_exists(Template(r"swap_assert3.png", record_pos=(-0.004, 0.046), resolution=(1080, 2340)), "展示闪兑按钮")

# 点击闪兑按钮
touch(Template(r"swap_swapbutton.png", record_pos=(-0.006, 0.051), resolution=(1080, 2340)))
sleep(3)
# 断言，界面展示闪兑确认界面
assert_exists(Template(r"swap_assert4.png", record_pos=(-0.006, -0.759), resolution=(1080, 2340)), "请填写测试点")

# 点击闪兑按钮
touch(Template(r"swap_swapbutton2.png", record_pos=(0.184, 0.965), resolution=(1080, 2340)))
sleep(2)

# 断言，展示闪兑成功的提示
assert_exists(Template(r"swap_assert5.png", record_pos=(0.001, -0.538), resolution=(1080, 2340)), "闪兑成功提示")

# 点击查看钱包按钮
touch(Template(r"swap_assert_checkwallet.png", record_pos=(-0.24, 0.957), resolution=(1080, 2340)))

# 进入钱包界面
assert_exists(Template(r"swap_assert6.png", record_pos=(0.006, -0.094), resolution=(1080, 2340)), "存在充币/提币按钮")














