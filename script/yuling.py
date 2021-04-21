# -*- encoding=utf8 -*-
""" 御灵自动脚本
"""
import time

from airtest.core.api import *
from common.const import GLOBAL_SIFT_CONTINUE
from common.utils import random_pos, touch_pos, image

auto_setup(__file__)


# 挑战 按钮
step1 = image("yeyuanhuo_chi_challenge.png", (1.059, 0.296), (1152, 679))


def challenge():
    touch(wait(step1, timeout=60)) 
    pos = wait(GLOBAL_SIFT_CONTINUE, timeout = 120)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)
    time.sleep(4)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)


def run(args):
    print("御灵 自动挂机脚本运行...")
    while(True):
        challenge()
