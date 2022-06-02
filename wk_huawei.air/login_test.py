# -*- encoding=utf8 -*-
__author__ = "mac"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/8KE0220117006068?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",], project_root="/Users/mac/Desktop/UiTest/wk_huawei.air")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
from tools import Tools
tool_obj = Tools()
tool_obj.login('wangkang@kimpper.ltd','Wktest@123','Q4AEF2BFCT7E2EY7')
