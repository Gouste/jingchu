# -*- encoding=utf8 -*-
__author__ = "mac"

from airtest.core.api import *

auto_setup(__file__)
from pyotp import TOTP


# text("wangkang@kimpper.ltd")
# text("Wktest@123")

# 获取GA
def get_gacode(ga_key):
    print(ga_key)
    gacode = pyotp.TOTP(ga_key).now()
    print(gacode, "||||||||||||||||||", end="")
    ga_list = list(gacode)
    print(ga_list)
    return ga_list


def inputGa(ga_list):
    img1 = Template(r"number1.png", record_pos=(-0.336, 0.169), resolution=(1080, 2340))
    img2 = Template(r"number2.png", record_pos=(-0.004, 0.169), resolution=(1080, 2340))
    img3 = Template(r"number3.png", record_pos=(0.334, 0.168), resolution=(1080, 2340))
    img4 = Template(r"number4.png", record_pos=(-0.333, 0.405), resolution=(1080, 2340))
    img5 = Template(r"number5.png", record_pos=(0.0, 0.404), resolution=(1080, 2340))
    img6 = Template(r"number6.png", record_pos=(0.333, 0.408), resolution=(1080, 2340))
    img7 = Template(r"number7.png", record_pos=(-0.335, 0.643), resolution=(1080, 2340))
    img8 = Template(r"number8.png", record_pos=(0.0, 0.64), resolution=(1080, 2340))
    img9 = Template(r"number9.png", record_pos=(0.333, 0.64), resolution=(1080, 2340))
    img0 = Template(r"number0.png", record_pos=(-0.002, 0.878), resolution=(1080, 2340))

    for i in ga_list:
        dest = eval("img" + i)  # 将字符串变更为变量
        touch(dest)
        sleep(1)



