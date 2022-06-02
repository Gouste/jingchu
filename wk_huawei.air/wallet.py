# -*- encoding=utf8 -*-
__author__ = "liuwei"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/8e36cb87?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",], project_root="/Users/liuwei/Desktop/UiTest/wk_huawei.air")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
#  点击钱包按钮，进入钱包界面

touch(Template(r"Wallet_tab.png", record_pos=(-0.2, 0.953), resolution=(1080, 2340)))

# 断言
assert_exists(Template(r"wallet_assert2.png", record_pos=(-0.001, -0.094), resolution=(1080, 2340)), "界面存在提币/存币按钮")

#提币流程，点击提币按钮
touch(Template(r"Wallet_Withdraw.png", record_pos=(0.207, -0.087), resolution=(1080, 2340)))

# 断言。界面展示默认提币币种为USDT
assert_exists(Template(r"wallet_assert1.png", record_pos=(-0.227, -0.675), resolution=(1080, 2340)), "界面展示默认提币币种为USDT")

# 币种默认为USDT。点击可选择币种
# 默认主链为TRC_20，点击ERC_20 切换主网
# 点击地主输入框，弹出键盘进入编辑模式，不限制字符输入，长度不限制
touch(Template(r"Wallet_Withdraw_imputbox.png", record_pos=(-0.09, -0.151), resolution=(1080, 2340)))

#.# 点击地址簿标志，进入地址簿界面
touch(Template(r"wallet_address_book.png", record_pos=(0.284, -0.154), resolution=(1080, 2340)))

# 断言，没有地址时，展示暂无数据
assert_exists(Template(r"wallet_no_data.png", record_pos=(0.007, -0.047), resolution=(1080, 2340)), "无地址时，界面展示暂无数据的log")

# 点击添加地址按钮
touch(Template(r"wallet_Add_address.png", record_pos=(-0.004, 0.993), resolution=(1080, 2340)))

# 断言，点击添加地址按钮。界面进入地址添加界面，默认添加地址的币种为USDT
assert_exists(Template(r"wallet_assert4.png", record_pos=(-0.22, -0.684), resolution=(1080, 2340)), "默认添加地址的币种为USDT")

# 点击地址输入框，唤醒键盘进入编辑状态-不限制字符，长度
touch(Template(r"wallet_inputbox.png", record_pos=(-0.138, -0.153), resolution=(1080, 2340)))

# 点击扫码按钮，进入扫码界面
touch(Template(r"wallet_Scanning_code.png", record_pos=(0.381, -0.148), resolution=(1080, 2340)))

# 断言，扫码界面展示图片的log
assert_exists(Template(r"wallet_assert3.png", record_pos=(0.001, 0.869), resolution=(1080, 2340)), "扫码界面展示图片的log")

# 点击图片log，进入相册界面
touch(Template(r"wallet_album.png", record_pos=(-0.001, 0.869), resolution=(1080, 2340)))

# 点击图片，识别图片后降低至录入到输入框内
touch(Template(r"wallet_withdraw_album.png", record_pos=(-0.381, -0.746), resolution=(1080, 2340)))

# 断言。地址输入框不在为空
assert_not_exists(Template(r"wallet_assert5.png", record_pos=(-0.149, -0.147), resolution=(1080, 2340)), "地址输入框不在为空")

# 白名单地址选项，默认为选中状态
assert_exists(Template(r"wallet_assert6.png", record_pos=(-0.149, 0.292), resolution=(1080, 2340)), "白名单地址选项，默认为选中状态")

# 如果该按钮为选中状态，点击添加按钮，需要进入安全验证步骤
if assert_exists(Template(r"wallet_assert7.png", record_pos=(-0.389, 0.298), resolution=(1080, 2340)), "按钮勾选"):

    # 点击添加按钮
    touch(Template(r"wallet_continue1.png", record_pos=(-0.015, 0.993), resolution=(1080, 2340)))
    sleep(3)

    #断言，进入安全验证步骤
    assert_exists(Template(r"wallet_assert8.png", record_pos=(-0.006, -0.799), resolution=(1080, 2340)), "进入安全验证步骤")
    sleep(3)
# 滑动界面
swipe(Template(r"wallet_swipe.png", record_pos=(-0.001, -0.928), resolution=(1080, 2340)), vector=[0.0009, 0.7425])
sleep(4)
# 点击取消白名单地址添加选项
touch(Template(r"wallet_touch1.png", record_pos=(-0.391, 0.302), resolution=(1080, 2340)))

# 点击继续按钮，弹出GA验证步骤，
touch(Template(r"wallet_contiune2.png", record_pos=(0.004, 0.993), resolution=(1080, 2340)))
sleep(3)

# 断言，进入GA验证界面
assert_exists(Template(r"wallet_assert9.png", record_pos=(-0.002, -0.681), resolution=(1080, 2340)), "界面展示该字段")

# 输入GA
from tools import Tools
ga_key = Tools()
ga_key.inputGa("6YDGV7U7EWIRE3VV")
sleep(4)

# 断言 进入地址选择界面，展示刚添加的新地址
assert_exists(Template(r"wallet_assert10.png", record_pos=(0.417, -0.591), resolution=(1080, 2340)), "添加的地址展示删除按钮")
sleep(2)

# 点击Confirm按钮
touch(Template(r"wallet_confirm1.png", record_pos=(0.229, 0.991), resolution=(1080, 2340)))

# 点击，地址录入到输入框内
touch(Template(r"wallet_assert11.png", record_pos=(-0.154, -0.156), resolution=(1080, 2340)))
sleep(2)

# 点击数量输入框
touch(Template(r"wallet_Amount_box.png", record_pos=(-0.335, 0.11), resolution=(1080, 2340)))

# 输入数量
text("10")

# 点击Contiune按钮
touch(Template(r"wallet_continue1.png", record_pos=(0.016, 0.993), resolution=(1080, 2340)))
sleep(3)

# 断言，进入提币确认界面
assert_exists(Template(r"wallet_assert12.png", record_pos=(-0.004, -0.799), resolution=(1080, 2340)), "展示提币确认字段")

# 点击Confirm按钮
touch(Template(r"wallet_confirm2.png", record_pos=(0.012, 0.964), resolution=(1080, 2340)))
sleep(1)

# 断言，进入提币界面
assert_exists(Template(r"wallet_assert13.png", record_pos=(-0.001, -0.794), resolution=(1080, 2340)), "进入提币界面")
sleep(2)

# 点击提笔密码验证输入框
touch(Template(r"wallet_password_box.png", record_pos=(-0.22, -0.538), resolution=(1080, 2340)))

# 输入密码
text("000000")

# 点击Ga输入框
touch(Template(r"wallet_GA_box.png", record_pos=(-0.212, -0.342), resolution=(1080, 2340)))

# 输入GA密码
from pyotp import TOTP
ga = TOTP("6YDGV7U7EWIRE3VV").now()
text(ga)

# 点击Confirm按钮
touch(Template(r"wallet_confirm3.png", record_pos=(-0.001, 0.96), resolution=(1080, 2340)))
sleep(5)

# 提币成功
assert_exists(Template(r"wallet_assert15.png", record_pos=(0.003, -0.506), resolution=(1080, 2340)), "提币成功")

# 点击Confirm按钮，进入提币详情界面
touch(Template(r"wallet_confirm4.png", record_pos=(-0.002, 0.961), resolution=(1080, 2340)))

# 断言，展示返回按钮
assert_exists(Template(r"wallet_assert16.png", record_pos=(-0.428, -0.938), resolution=(1080, 2340)), "界面展示返回按钮")

# 点击返回按钮，返回提币界面
touch(Template(r"wallet_return1.png", record_pos=(-0.426, -0.941), resolution=(1080, 2340)))
sleep(2)
# 点击返回按钮，返回钱包主页
touch(Template(r"wallet_return2.png", record_pos=(-0.424, -0.939), resolution=(1080, 2340)))
sleep(2)

# 断言。该界面展示提币/存币按钮
assert_exists(Template(r"wallet_assert17.png", record_pos=(0.003, -0.175), resolution=(1080, 2340)), "该界面展示提币/存币按钮")
sleep(2)

# 点击存币按钮
touch(Template(r"wallet_Deposit.png", record_pos=(-0.211, -0.167), resolution=(1080, 2340)))

# 断言，界面展示存币二维码
assert_exists(Template(r"wallet_assert18.png", record_pos=(-0.003, 0.106), resolution=(1080, 2340)), "界面展示存币二维码")

# 点击Save Picture按钮，将二维码保存到手机相册
touch(Template(r"wallet_savepicture.png", record_pos=(0.243, 0.986), resolution=(1080, 2340)))















