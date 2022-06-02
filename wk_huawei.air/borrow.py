# -*- encoding=utf8 -*-
__author__ = "liuwei"
__desc__ = "borrow"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from extend_utils import Utils
Utils_obj = Utils()
from tools import Tools
po = Tools()

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/9e06ed2e?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",], project_root="/Users/liuwei/Desktop/UiTest/wk_huawei.air")



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
# 借贷成功
touch(Template(r"borrow_tab.png", record_pos=(-0.375, 1.002), resolution=(1080, 2340)))
touch(Template(r"borrow_button.png", record_pos=(0.231, -0.186), resolution=(1080, 2340)))
touch(Template(r"borrow_enter collateral amonunt.png", record_pos=(-0.119, -0.344), resolution=(1080, 2340)))
text("1")
swipe(Template(r"borrow_swipe.png", record_pos=(-0.006, 0.701), resolution=(1080, 2340)), vector=[-0.0199, -0.2076])
touch(Template(r"borrow_installment.png", record_pos=(0.287, 0.338), resolution=(1080, 2340)))
sleep(1)
touch(Template(r"borrow_3 installments.png", record_pos=(-0.448, 0.287), resolution=(1080, 2412)))
touch(Template(r"borrow_coutinue.png", record_pos=(-0.006, 0.96), resolution=(1080, 2340)))
touch(Template(r"borrow_Check the agreement.png", record_pos=(-0.439, 0.787), resolution=(1080, 2340)))
touch(Template(r"borrow_confirm.png", record_pos=(-0.002, 0.961), resolution=(1080, 2340)))
wait(Template(r"borrow_success_swipe.png", record_pos=(0.003, -0.463), resolution=(1080, 2340)), timeout=20, interval=1)
touch(Template(r"borrow_back to borrow.png", record_pos=(0.236, 0.96), resolution=(1080, 2340)))

# 补充质押物
touch(Template(r"borrow_order.png", record_pos=(0.009, 0.311), resolution=(1080, 2340)))# 后期需要修改，因每次的订单数量不确定，后期需改为试用订单状态进行识别
touch(Template(r'borrow_add collateral.png', record_pos=(0.236, -0.031), resolution=(1080, 2340)))
wait(Template(r"borrow_add collateral_swipe.png", record_pos=(-0.012, 0.017), resolution=(1080, 2340)), timeout=20, interval=1)
touch(Template(r"borrow_add pledge.png", record_pos=(-0.056, -0.407), resolution=(1080, 2340)))
text("1")
touch(Template(r"borrow_continue.png", record_pos=(0.005, 0.995), resolution=(1080, 2412)))
sleep(2)
gacode = Utils_obj.get_gacode("I4KG3WGLGRER775X")
po.inputGa(gacode)
sleep(2)
wait(Template(r"borrow_add pledge wait.png", record_pos=(0.028, -0.543), resolution=(1080, 2412)),timeout=20,interval=1)
touch(Template(r"borrow_ok.png", record_pos=(0.001, 0.989), resolution=(1080, 2412)))
sleep(2)

# 提取质押物
touch(Template(r"borrow_Withdrawal pledge  .png", record_pos=(-0.231, -0.034), resolution=(1080, 2412)))
sleep(2)
wait(Template(r"borrow_wait.png", record_pos=(0.014, 0.163), resolution=(1080, 2412)), timeout=20, interval=1)
touch(Template(r"borrow_all.png", record_pos=(0.397, -0.512), resolution=(1080, 2412)))
touch(Template(r"boeeow_confirm.png", record_pos=(-0.007, 0.993), resolution=(1080, 2412)))
sleep(4)
gacode = Utils_obj.get_gacode("I4KG3WGLGRER775X")
po.inputGa(gacode)
sleep(2)
wait(Template(r"borrow_wait2.png", record_pos=(0.006, -0.567), resolution=(1080, 2412)))
touch(Template(r"borrow_ok2.png", record_pos=(0.003, 0.994), resolution=(1080, 2412)))

# 借贷订单续期:续三期

touch(Template(r"borrow_renew.png", record_pos=(0.243, 1.024), resolution=(1080, 2412)))
sleep(3)
wait(Template(r"borrow_renewal.png", record_pos=(0.006, -0.676), resolution=(1080, 2412)), timeout=20, interval=1)
touch(Template(r"borrow_renewal3  .png", record_pos=(-0.105, -0.534), resolution=(1080, 2412)))
sleep(2)
touch(Template(r"borrow_confirm3.png", record_pos=(0.004, 0.993), resolution=(1080, 2412)))
sleep(1)
touch(Template(r"borrow_confirm4.png", record_pos=(0.194, 0.243), resolution=(1080, 2412)))
sleep(2)
wait(Template(r"borrow_renewal success.png", record_pos=(0.01, 0.107), resolution=(1080, 2412)), timeout=20, interval=1)
touch(Template(r"borrow_ok3.png", record_pos=(0.001, 0.991), resolution=(1080, 2412)))
sleep(2)

# 还币：全还币
touch(Template(r"borrow_prepay.png", record_pos=(-0.233, 1.03), resolution=(1080, 2412)))
sleep(3)
touch(Template(r"borrow_all2.png", record_pos=(0.399, -0.525), resolution=(1080, 2412)))
sleep(3)
touch(Template(r"boorow_pay.png", record_pos=(-0.145, 1.028), resolution=(1080, 2412)))

sleep(3)
gacode = Utils_obj.get_gacode("I4KG3WGLGRER775X")
po.inputGa(gacode)
sleep(4)
touch(Template(r"borrow_back to borrow2.png", record_pos=(0.243, 0.993), resolution=(1080, 2412)))
sleep(4)

# 自动补仓按钮关闭，打开
touch(Template(r"borrow_automatic on.png", record_pos=(0.397, -0.697), resolution=(1080, 2412)))
sleep(3)
touch(Template(r"borrow_on confirm.png", record_pos=(0.18, 0.263), resolution=(1080, 2412)))
sleep(3)
gacode = Utils_obj.get_gacode("I4KG3WGLGRER775X")
po.inputGa(gacode)
sleep(3)
touch(Template(r"borrow_automatic off.png", record_pos=(0.415, -0.694), resolution=(1080, 2412)))




















