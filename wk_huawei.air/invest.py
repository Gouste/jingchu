# -*- encoding=utf8 -*-
__author__ = "mac"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",], project_root="/Users/mac/Desktop/UiTest/wk_huawei.air")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)