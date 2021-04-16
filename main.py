# -*- encoding=utf8 -*-
import argparse
import logging
import sys

logging.disable(logging.ERROR)

from airtest.core.helper import G
from common.utils import connect_windows, connect_android

from script import auto_team
from script import chi
from script import tupo


def _get_parser():
    ap = argparse.ArgumentParser(description="yys auto tool")
    ap.add_argument('--android', help='connect to android device')
    subparsers = ap.add_subparsers(dest="action", help="auto/")

    ap_run = subparsers.add_parser("auto", help="自动挂机")
    ap_run.add_argument("script", help="挂机脚本")

    ap_run = subparsers.add_parser("team", help="自动组队挂机")
    ap_run.add_argument("leader", help="队长标记")
    return ap


def main(argv=None):
    ap = _get_parser()
    args = ap.parse_args(argv)

    # 连接设备
    if args.android:
        print("连接安卓设备%s" % args.android)
        if connect_android(args.android):
            sys.exit(1)
    else:
        if connect_windows("阴阳师-网易游戏"):
            sys.exit(1)
    print("\n设备连接成功")
    
    runner = None

    if args.action == "auto":
        if args.script == "1":
            runner = chi
        elif args.script == "2":
            runner = tupo
    elif args.action == "team":
        runner = auto_team
    else:
        ap.print_help()

    try:
        runner.run(args)
    except KeyboardInterrupt:
        print("退出脚本执行")
    except Exception:
        raise


if __name__ == "__main__": 
    main()
