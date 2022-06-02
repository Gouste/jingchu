# -----------------------------
# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 12:03
# @Author  : wk！
# @Project : UiTest
# @FileName: tools
# @Software: PyCharm
# -----------------------------
# utils
from airtest.core.api import *
from pyotp import TOTP


class Tools:
    def __init__(self):
        pass

    # 递归算法调用,做腾讯滑块验证
    def slider_validation(self, x=0.45):
        swipe(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340)), vector=[x, 0],
              duration=0.5)
        sleep(2)
        if exists(Template(r"slider.png", record_pos=(-0.234, 0.246), resolution=(1080, 2340))):
            self.slider_validation(x + 0.03)

    def inputGa(self, ga_key):
        gacode = TOTP(ga_key).now()
        ga_list = list(gacode)
        img1 = Template(r"number1.png", record_pos=(-0.336, 0.169), resolution=(1080, 2340),threshold=0.6)
        img2 = Template(r"number2.png", record_pos=(-0.004, 0.169), resolution=(1080, 2340),threshold=0.6)
        img3 = Template(r"number3.png", record_pos=(0.334, 0.168), resolution=(1080, 2340),threshold=0.6)
        img4 = Template(r"number4.png", record_pos=(-0.333, 0.405), resolution=(1080, 2340),threshold=0.6)
        img5 = Template(r"number5.png", record_pos=(0.0, 0.404), resolution=(1080, 2340),threshold=0.6)
        img6 = Template(r"number6.png", record_pos=(0.333, 0.408), resolution=(1080, 2340),threshold=0.6)
        img7 = Template(r"number7.png", record_pos=(-0.335, 0.643), resolution=(1080, 2340),threshold=0.6)
        img8 = Template(r"number8.png", record_pos=(0.0, 0.64), resolution=(1080, 2340),threshold=0.6)
        img9 = Template(r"number9.png", record_pos=(0.333, 0.64), resolution=(1080, 2340),threshold=0.6)
        img0 = Template(r"number0.png", record_pos=(-0.002, 0.878), resolution=(1080, 2340),threshold=0.6)

        for i in ga_list:
            dest = eval("img" + i)  # 将字符串变更为变量
            touch(dest)
            sleep(1)

    def login(self, email, password, ga_key):
        clear_app("com.kimpper.inhouse")
        # start_app("com.kimpper.inhouse")
        keyevent("home")
        touch(Template(r"kimpper-test.png", record_pos=(0.356, 0.594), resolution=(1080, 2340)))
        wait(Template(r"login.png", record_pos=(-0.006, 0.518), resolution=(1080, 1920)))
        touch(Template(r"login.png", record_pos=(-0.006, 0.518), resolution=(1080, 1920)))
        sleep(0.5)
        touch(Template(r"email.png", record_pos=(-0.37, -0.522), resolution=(1080, 2340)))
        sleep(0.5)
        text(email)
        touch(Template(r"password.png", record_pos=(-0.329, -0.274), resolution=(1080, 2340)))
        text(password)
        touch(Template(r"login.png", record_pos=(-0.011, 0.016), resolution=(1080, 2340)))

        sleep(2)
        self.slider_validation(0.45)
        sleep(2)
        if exists(Template(r"two_factor_auth.png", record_pos=(0.003, -0.682), resolution=(1080, 2340))):
            self.inputGa(ga_key)
            sleep(2)
            # 设置pin码
            wait(Template(r"please_enter_new_pin.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
            numkey = exists(Template(r"please_enter_new_pin.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
            if numkey:
                for i in range(4):
                    touch(Template(r"pin_number8.png", record_pos=(0.004, 0.638), resolution=(1080, 2340)))
                sleep(0.5)
                for i in range(4):
                    touch(Template(r"pin_number8.png", record_pos=(0.004, 0.638), resolution=(1080, 2340)))

        else:
            wait(Template(r"please_enter_new_pin.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
            numkey = exists(Template(r"please_enter_new_pin.png", record_pos=(-0.005, -0.684), resolution=(1080, 2340)))
            if numkey:
                for i in range(4):
                    touch(Template(r"pin_number8.png", record_pos=(0.004, 0.638), resolution=(1080, 2340)))
                sleep(0.5)
                for i in range(4):
                    touch(Template(r"pin_number8.png", record_pos=(0.004, 0.638), resolution=(1080, 2340)))
