# -*- encoding=utf8 -*-
#! /usr/local/bin/python3
__author__ = "wangkang"
__desc__ = """
登录kimpper
"""
from pyotp import TOTP
from airtest.core.api import *


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

# clear_app("com.kimpper.inhouse")
# start_app("com.kimpper.inhouse")

auto_setup(__file__)

# poco初始化代码
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 功能函数区===========================================================

# 获取GA
def get_code():
    gacode = TOTP("Q4AEF2BFCT7E2EY7").now()
    return gacode
ga = get_code()
print(ga)

# 滑块验证
# def slider_validation(x):
#     swipe(Template(r"tpl1638455420014.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340)), vector=[x,0],duration=0.5)
#     sleep(2)

# 递归算法调用
def slider_validation(x):
    swipe(Template(r"tpl1638455420014.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340)), vector=[x,0],duration=0.5)
    sleep(2)
    if exists(Template(r"tpl1638455420014.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340))) :
        slider_validation(x+0.03)
        
# 设置pin码
def click8 ():
    for i in range(4):
        touch(Template(r"tpl1638455903093.png", record_pos=(0.004, 0.638), resolution=(1080, 2340)))
# 功能函数区===========================================================

# 登录->查看主tab页面
def base_test():
    clear_app("com.kimpper.inhouse")
    # start_app("com.kimpper.inhouse")
    keyevent("home")
    touch(Template(r"tpl1638454691072.png", record_pos=(0.356, 0.594), resolution=(1080, 2340)))
    wait(Template(r"tpl1645630447697.png", record_pos=(-0.006, 0.518), resolution=(1080, 1920)))
    touch(Template(r"tpl1645630447697.png", record_pos=(-0.006, 0.518), resolution=(1080, 1920)))
    sleep(0.5)
    touch(Template(r"tpl1638455251238.png", record_pos=(-0.37, -0.522), resolution=(1080, 2340)))
    sleep(0.5)
    text("7ivmy9rw@linshiyouxiang.net")
    touch(Template(r"tpl1638455236086.png", record_pos=(-0.329, -0.274), resolution=(1080, 2340)))
    text("Wktest@123")
    touch(Template(r"tpl1638455390324.png", record_pos=(-0.011, 0.016), resolution=(1080, 2340)))
    
    sleep(2)
    slider_validation(0.45)
#     list = [0.45,0.48,0.45,0.51,0.48,0.45,0.44]
#     for i in list:
#         if exists(Template(r"tpl1638455420014.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340))) :
#             slider_validation(i)
#         else:
#             break
    
# 设置pin码
    wait(Template(r"tpl1645520064724.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
    numkey = exists(Template(r"tpl1645520064724.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
    if numkey:
        click8()
        sleep(0.5)
        click8()

    sleep(1.0)
    touch(Template(r"tpl1645521340913.png", record_pos=(0.375, 1.0), resolution=(1080, 2340)))
    sleep(1.0)

    touch(Template(r"tpl1645523130321.png", record_pos=(0.127, 1.004), resolution=(1080, 2340)))

    sleep(6.0)
    snapshot(msg="查看基金和固收列表")
    assert_exists(Template(r"tpl1645711719444.png", record_pos=(0.381, -0.594), resolution=(1080, 2340)), "投资页面有数据")

    
#     assert_exists()

    touch(Template(r"tpl1645523172892.png", record_pos=(-0.129, 1.002), resolution=(1080, 2340)))
    sleep(1.0)

    touch(Template(r"tpl1645523241068.png", record_pos=(-0.375, 1.0), resolution=(1080, 2340)))
    sleep(1.0)
    touch(Template(r"tpl1645521340913.png", record_pos=(0.375, 1.0), resolution=(1080, 2340)))
    sleep(1.0)
    swipe(Template(r"tpl1645523732727.png", record_pos=(-0.416, 0.349), resolution=(1080, 2340)), vector=[0.0, -0.35])
    touch(Template(r"tpl1645523824877.png", record_pos=(-0.005, 0.792), resolution=(1080, 2340)))
    clear_app("com.kimpper.inhouse")
for i in range(2):
    base_test()







