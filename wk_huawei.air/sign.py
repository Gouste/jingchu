# -*- encoding=utf8 -*-
__author__ = "wangkang"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from extend_utils import Utils
utils_obj = Utils()
from tools import Tools
tools_obj = Tools()

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/8KE0220117006068?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",], project_root="/Users/mac/Desktop/UiTest/wk_huawei.air")



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


# 功能函数区===========================================================
# 递归算法调用,滑块验证
def slider_validation(x):
    swipe(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340)), vector=[x, 0], duration=0.5)
    sleep(2)
    if exists(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340))) :
        slider_validation(x+0.03)
# 功能函数区===========================================================
clear_app("com.kimpper.inhouse")
# start_app("com.kimpper.inhouse")
keyevent("home")
touch(Template(r"kimpper-test.png", record_pos=(0.356, 0.594), resolution=(1080, 2340)))
touch(Template(r"signup.png", record_pos=(-0.008, 0.82), resolution=(1080, 2340)))
touch(Template(r"email.png", record_pos=(-0.383, -0.517), resolution=(1080, 2340)))
text("1806755030@qq.com")
touch(Template(r"password.png", record_pos=(-0.337, -0.271), resolution=(1080, 2340)))
text("Wktest@123")
touch(Template(r"repeat_password.png", record_pos=(-0.264, -0.031), resolution=(1080, 2340)))
text("Wktest@123")
touch(Template(r"continue.png", record_pos=(-0.005, 0.219), resolution=(1080, 2340)))
sleep(1)
touch(Template(r"signup_no.png", record_pos=(0.188, 0.356), resolution=(1080, 2340)))
# slider_validation(0.45)
tools_obj.slider_validation(0.45)
touch(Template(r"activation_code.png", record_pos=(-0.281, -0.281), resolution=(1080, 2340)))
# todo登录邮箱获取验证码
sleep(20)
code = utils_obj.get_email()
print(code,"code+++++++++++++++++++++++++++++")
text(code)
touch(Template(r"continue.png", record_pos=(0.0, 0.171), resolution=(1080, 2340)))
sleep(3)
assert_exists(Template(r"kimpper_icon.png", record_pos=(-0.005, -0.508), resolution=(1080, 2340)), "注册成功返回首页")
# todo删除该账号,重新进行注册



