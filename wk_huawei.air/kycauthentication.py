# -*- encoding=utf8 -*-
__author__ = "liuwei"
__desc__ = ""

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/8e36cb87?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",], project_root="/Users/liuwei/Desktop/UiTest/wk_huawei.air")


touch(Template(r"kyc_more.png", record_pos=(0.38, 1.002), resolution=(1080, 2340)))
touch(Template(r"kyc_verification.png", record_pos=(-0.152, -0.142), resolution=(1080, 2340)))
wait(Template(r"kyc_tab1.png", record_pos=(0.017, 0.0), resolution=(1080, 2340)),timeout=20,interval=2)
touch(Template(r"kyc_tab1_first name.png", record_pos=(-0.023, -0.695), resolution=(1080, 2340)))
text("KYC名称")
touch(Template(r"kyc_tab1_last name.png", record_pos=(0.012, -0.459), resolution=(1080, 2340)))
text("KYC名称")
touch(Template(r"kyc_tab1_date of birth.png", record_pos=(-0.021, -0.208), resolution=(1080, 2340)))
touch(Template(r"kyc_tab1_confirm.png", record_pos=(0.412, 0.312), resolution=(1080, 2340)))
touch(Template(r"kyc_tab1_gender.png", record_pos=(0.039, 0.032), resolution=(1080, 2340)))
touch(Template(r"kyc_tab1_female.png", record_pos=(0.019, 0.57), resolution=(1080, 2340)))
touch(Template(r"kyc_tab1_continue.png", record_pos=(-0.004, 0.957), resolution=(1080, 2340)))
touch(Template(r"kyc_tab2_street address.png", record_pos=(-0.006, -0.695), resolution=(1080, 2340)))
text("地址")
touch(Template(r"kyc_tab2_apartment number.png", record_pos=(0.006, -0.452), resolution=(1080, 2340)))
text("打开电视")
touch(Template(r"kyc_tab2_city.png", record_pos=(0.031, -0.202), resolution=(1080, 2340)))
text("站着看电视")
touch(Template(r"kyc_tab2_state.png", record_pos=(-0.003, 0.033), resolution=(1080, 2340)))
text("坐着看电视")
touch(Template(r"kyc_tab2_postal code.png", record_pos=(0.007, 0.265), resolution=(1080, 2340)))
text("躺着看电视")
touch(Template(r"kyc_tab2_country.png", record_pos=(0.02, 0.511), resolution=(1080, 2340)))
touch(Template(r"kyc_tab2_austria.png", record_pos=(-0.017, -0.286), resolution=(1080, 2340)))
touch(Template(r"kyc_tab2_continue.png", record_pos=(-0.002, 0.959), resolution=(1080, 2340)))
touch(Template(r"kyc_tab3_national id card.png", record_pos=(0.001, -0.519), resolution=(1080, 2340)))
touch(Template(r"kyc_tab4_upload1.png", record_pos=(0.043, 0.149), resolution=(1080, 2340)))
touch(Template(r"kyc_tab4_picture.png", record_pos=(0.123, -0.748), resolution=(1080, 2340)))
wait(Template(r"kyc_tab4.png", record_pos=(0.009, 0.034), resolution=(1080, 2340)),timeout=20,interval=2)
touch(Template(r"kyc_tab4_upload2.png", record_pos=(0.043, 0.466), resolution=(1080, 2340)))
touch(Template(r"kyc_tab4_picture2.png", record_pos=(0.37, -0.746), resolution=(1080, 2340)))
wait(Template(r"kyc_tab4_wait2.png", record_pos=(-0.001, 0.029), resolution=(1080, 2340)),timeout=20,interval=1)

touch(Template(r"kyc_tab4_name.png", record_pos=(-0.001, 0.825), resolution=(1080, 2340)))
text("KYC身份证名称")
swipe(Template(r"kyc_tab4_wait1.png", record_pos=(0.044, 0.663), resolution=(1080, 2340)), vector=[-0.0371, -0.1475])
touch(Template(r"kyc_tab4_id card number.png", record_pos=(-0.001, 0.751), resolution=(1080, 2340)))
text("98798798")
touch(Template(r"kyc_tab4_continue.png", record_pos=(-0.002, 0.959), resolution=(1080, 2340)))
wait(Template(r"kyc_tab5_wait1.png", record_pos=(-0.002, 0.029), resolution=(1080, 2340)), timeout=20, interval=1)

touch(Template(r"kyc_tab5_upload3.png", record_pos=(0.045, 0.294), resolution=(1080, 2340)))
touch(Template(r"kyc_tab5_picture3.png", record_pos=(0.123, -0.496), resolution=(1080, 2340)))
wait(Template(r"kyc_tab5_wait2.png", record_pos=(-0.006, 0.016), resolution=(1080, 2340)))
touch(Template(r"kyc_tab5_continue.png", record_pos=(-0.004, 0.959), resolution=(1080, 2340)))









