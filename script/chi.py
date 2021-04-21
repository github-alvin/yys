# -*- encoding=utf8 -*-
""" 业原火-痴之阵自动脚本
"""
import time

from airtest.core.api import *
from common.const import GLOBAL_BUTTON_EXPLORE, GLOBAL_SIFT_SHARE, GLOBAL_SIFT_CONTINUE
from common.utils import random_pos, touch_pos, image

auto_setup(__file__)


# 探索-御魂 按钮
step1 = image("explore_yuhun.png", (0.723, 0.379), (1152, 679))

# 御魂-业原火封面
step2 = image("yuhun_yeyuanhuo.png", (0.605, 0.039), (1152, 679))

# 业原火-痴之阵
step3 = image("yeyuanhuo_chi_page.png", (0.783, 0.294), (1152, 679))

# 痴之阵-挑战 按钮
step4 = image("yeyuanhuo_chi_challenge.png", (1.059, 0.296), (1152, 679))


def enter_challenge_ui():
    """主界面跳转到痴之阵界面
    """
    touch(GLOBAL_BUTTON_EXPLORE)
    touch(step1)
    touch(step2)
    touch(step3)

def challenge():
    touch(wait(step4, timeout=60))

    pos = wait(GLOBAL_SIFT_SHARE, timeout=5 * 60, interval=2)
    touch_pos(random_pos(pos, 50, 100))

    pos = wait(GLOBAL_SIFT_CONTINUE, timeout = 60)
    time.sleep(4)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)


def run(args):
    print("业原火-痴之阵 自动挂机脚本运行...")
    # enter_challenge_ui()
    while(True):
        challenge()
