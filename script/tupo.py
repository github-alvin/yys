# -*- encoding=utf8 -*-
""" 个人突破自动脚本
"""
import time

from airtest.core.api import *
from airtest.core.cv import Predictor
from common.const import GLOBAL_SIFT_CONTINUE, GLOBAL_SIFT_VICTORY, GLOBAL_SIFT_FAILED
from common.utils import random_pos, touch_pos, image, get_current_resolution, select


MAX_WAIT_TIME =  5 * 60

# 突破名单窗口坐标偏移
COMMON_POS = (
    (-0.189, -0.089), (0.068, -0.089), (0.324, -0.089),
    (-0.189, 0.014), (0.068, 0.014), (0.324, 0.014),
    (-0.189, 0.118), (0.068, 0.118), (0.324, 0.118),
)

# 挑战按钮
challenge_button = image("tupo_fuck.png", (0, 0), (1152, 679))

# 挑战券不足
tip_noticket = image("tupo_no_ticket.png", (0.221, 0.083), (1152, 679))


def calc_pos():
    """ 根据当前分辨率计算出每个突破可选窗口坐标
    """
    resolution = get_current_resolution()
    ret = []
    for pos in COMMON_POS:
        ret.append(Predictor.get_predict_point(pos, resolution))
    return ret


def fuck(idx, pos):
    # 选择进攻
    touch_pos(pos)
    time.sleep(0.5)

    button = exists(challenge_button)
    if not button:
        print(f"第{idx + 1}号结界已挑战过，跳过")
        return -1
     # 确认进攻
    touch_pos(button, 2)
    if(exists(tip_noticket)):
        print("挑战券不足，脚本终止")
        return -2

    # 等待挑战结束
    ret, _ = select((GLOBAL_SIFT_VICTORY, GLOBAL_SIFT_FAILED), timeout=MAX_WAIT_TIME)
    # 挑战失败
    if ret == 1:
        print(f"第{idx + 1}号结界挑战失败，请注意更换阵容")
        return -3
    # 再次确认跳过等待时间
    pos = wait(GLOBAL_SIFT_CONTINUE, timeout=MAX_WAIT_TIME)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)
    time.sleep(4)
    touch_pos(random_pos(pos, 50, 100, 0, 1), 2)
    return 0


def run(args):
    print("个人突破 自动挂机脚本运行...")
    targets = calc_pos()

    while(True):
        cnt = 0
        for idx, pos in enumerate(targets):
            ret = fuck(idx, pos)
            if ret == -2:
                return
            if ret in (0, -1):
                cnt += 1
            # 每三次成功额外奖励结算时间
            if not ret and cnt and cnt % 3 == 0:
                print("等待额外奖励结算...")
                time.sleep(5)
                touch_pos(pos)
                time.sleep(1)
        if cnt < 9:
            print("部分挑战失败，请更换阵容再试！")
            break
 