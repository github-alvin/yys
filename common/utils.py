import random
import time

from airtest.core.api import *
from airtest.core.error import TargetNotFoundError
from airtest.core.helper import (G, delay_after_operation)


def connect(name):
    try:
        connect_device("windows:///?title_re=%s" % name)
    except Exception as e:
        print("connect failed! Please check or report it: ", e)
        return 1
    return 0


def random_pos(pos, xmin, xmax, zmin=-1, zmax=-1):
    if zmin == -1 or zmax == -1:
        zmin, zmax = xmin, xmax
    return (pos[0] + random.randrange(xmin, xmax),
            pos[1] + random.randrange(zmin, zmax))


def touch_pos(pos, times=1, **kwargs):
    for _ in range(times):
        G.DEVICE.touch(pos, **kwargs)
        time.sleep(0.05)
    delay_after_operation()


def image(path, rpos, rs):
    return Template(r"../assets/{}".format(path), record_pos=rpos, resolution=rs)


def get_current_resolution():
    return G.DEVICE.get_current_resolution()


def wati_util(v, condition, timeout=60, interval=0.5):
    start_time = time.time()
    while True:
        ret = find_all(v)
        if condition(ret):
            return ret
        if (time.time() - start_time) > timeout:
            raise TargetNotFoundError('Continue %s not found in screen' % v)
        time.sleep(interval)
