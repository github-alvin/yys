# -*- encoding=utf8 -*-
import argparse
import logging
import sys

logging.disable(logging.INFO)

from airtest.core.helper import G
from common.utils import connect

from script import auto_team
from script import chi


def _get_parser():
    ap = argparse.ArgumentParser(description="yys auto tool")
    subparsers = ap.add_subparsers(dest="action", help="auto/")

    ap_run = subparsers.add_parser("auto", help="自动挂机")
    ap_run.add_argument("script", help="挂机脚本")

    ap_run = subparsers.add_parser("team", help="自动组队挂机")
    ap_run.add_argument("leader", help="队长标记")
    return ap


def main(argv=None):
    # 连接设备
    if connect("阴阳师-网易游戏"):
        sys.exit(1)

    print("\n客户端连接成功")

    ap = _get_parser()
    args = ap.parse_args(argv)

    runner = None

    if args.action == "auto":
        if args.script == "1":
            runner = chi
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
