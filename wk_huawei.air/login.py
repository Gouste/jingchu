# -*- encoding=utf8 -*-
__author__ = "mac"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


auto_setup(__file__)

# poco初始化代码
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 功能函数区===========================================================

# 滑块验证
# def slider_validation(x):
#     swipe(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340)), vector=[x,0],duration=0.5)
#     sleep(2)

# 递归算法调用
def slider_validation(x):
    swipe(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340)), vector=[x, 0], duration=0.5)
    sleep(2)
    if exists(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340))) :
        slider_validation(x+0.03)
        
# 设置pin码
def click8 ():
    for i in range(4):
        touch(Template(r"pin_number8.png", record_pos=(0.004, 0.638), resolution=(1080, 2340)))
# 功能函数区===========================================================

# 登录->查看主tab页面
def base_test():
    clear_app("com.kimpper.inhouse")
    # start_app("com.kimpper.inhouse")
    keyevent("home")
    touch(Template(r"kimpper-test.png", record_pos=(0.356, 0.594), resolution=(1080, 2340)))
    wait(Template(r"login.png", record_pos=(-0.006, 0.518), resolution=(1080, 1920)))
    touch(Template(r"login.png", record_pos=(-0.006, 0.518), resolution=(1080, 1920)))
    sleep(0.5)
    touch(Template(r"email.png", record_pos=(-0.37, -0.522), resolution=(1080, 2340)))
    sleep(0.5)
    text("wangkang@kimpper.ltd")
    touch(Template(r"password.png", record_pos=(-0.329, -0.274), resolution=(1080, 2340)))
    text("Wktest@123")
    touch(Template(r"login.png", record_pos=(-0.011, 0.016), resolution=(1080, 2340)))
    
    sleep(2)
    slider_validation(0.45)
#     list = [0.45,0.48,0.45,0.51,0.48,0.45,0.44]
#     for i in list:
#         if exists(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340))) :
#             slider_validation(i)
#         else:
#             break
    from tools import Tools
    po = Tools()
    po.inputGa('Q4AEF2BFCT7E2EY7')
#     sleep(0.2)
# 设置pin码
    wait(Template(r"please_enter_new_pin.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
    numkey = exists(Template(r"please_enter_new_pin.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
    if numkey:
        click8()
        sleep(0.5)
        click8()

    sleep(1.0)

    assert_exists(Template(r"tab_more.png"),"登录成功,已到主页面")
    touch(Template(r"tab_more.png", record_pos=(0.375, 1.0), resolution=(1080, 2340)))
    sleep(1.0)

    touch(Template(r"tab_invest.png", record_pos=(0.127, 1.004), resolution=(1080, 2340)))

    sleep(6.0)
    snapshot(msg="查看基金和固收列表")
    assert_exists(Template(r"invest_positions.png", record_pos=(0.381, -0.594), resolution=(1080, 2340)), "投资页面有数据")

    
#     assert_exists()

    touch(Template(r"tab_wallet.png", record_pos=(-0.129, 1.002), resolution=(1080, 2340)))
    sleep(1.0)

    touch(Template(r"tab_borrow.png", record_pos=(-0.375, 1.0), resolution=(1080, 2340)))
    sleep(1.0)
    touch(Template(r"tab_swap.png", record_pos=(-0.001, 0.848), resolution=(1080, 2340)))
    sleep(1.0)

    touch(Template(r"tab_more.png", record_pos=(0.375, 1.0), resolution=(1080, 2340)))
    sleep(1.0)
    swipe(Template(r"more_notifications_icon.png", record_pos=(-0.416, 0.349), resolution=(1080, 2340)), vector=[0.0, -0.55])
    touch(Template(r"logout.png", record_pos=(-0.005, 0.792), resolution=(1080, 2340)))
    assert_exists(Template(r"login.png", record_pos=(0.002, 0.54), resolution=(1080, 2340)), "退出登录成功")
    wait(3.0)

    clear_app("com.kimpper.inhouse")
for i in range(1):
    base_test()
    




