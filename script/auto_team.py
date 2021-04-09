# -*- encoding=utf8 -*-
""" 自动组队脚本
"""
import time

from airtest.core.api import *
from common.const import (
    GLOBAL_TEAMMATES_SLOT,
    GLOBAL_TEAM_CHALLENGE,
    GLOBAL_SIFT_SHARE,
    GLOBAL_SIFT_CONTINUE,
    )
from common.utils import random_pos, touch_pos, image, wati_util

auto_setup(__file__)

MAX_WAIT_TIME = 10 * 60

def auto_continue():
    pos = wait(GLOBAL_SIFT_SHARE, timeout=MAX_WAIT_TIME, interval=2)
    touch_pos(random_pos(pos, 50, 100))

    pos = wait(GLOBAL_SIFT_CONTINUE, timeout=MAX_WAIT_TIME)
    time.sleep(4)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)


def leader_continue():

    def _wait_teammates(pos):
        if not pos or len(pos) >= 2:
            return False
        return True

    # 二次确认，防止界面加载瞬间
    for _ in range(2):
        wati_util(GLOBAL_TEAMMATES_SLOT, _wait_teammates, MAX_WAIT_TIME, 1)
        time.sleep(1.5)

    touch(GLOBAL_TEAM_CHALLENGE)

    pos = wait(GLOBAL_SIFT_CONTINUE, timeout=MAX_WAIT_TIME)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)

    time.sleep(4)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)


def run(args):
    if args.leader == "1":
        print("队长自动挂机脚本运行...")
        func = leader_continue
    else:
        print("队员自动挂机脚本运行...")
        func = auto_continue
    while(True):
        func()
