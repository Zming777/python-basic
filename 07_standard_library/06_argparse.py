"""argparse：为脚本添加命令行参数。

适用场景：让用户指定姓名、次数、输入文件等，不用修改源代码。
直接运行使用默认值；运行本文件后加 --help 可查看参数说明。
例：python 07_standard_library/06_argparse.py --name 小明 --count 2
"""

import argparse


def positive_count(value):
    """argparse 的 type 参数也可以接收自定义转换函数。"""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("次数必须是整数")
    if not 1 <= number <= 10:
        raise argparse.ArgumentTypeError("次数必须在 1 到 10 之间")
    return number


def build_parser():
    parser = argparse.ArgumentParser(description="一个可以设置姓名的问候脚本")
    parser.add_argument("--name", default="学习者", help="称呼，默认：学习者")
    parser.add_argument("--count", type=positive_count, default=1,
                        help="问候次数，1 到 10，默认：1")
    parser.add_argument("--excited", action="store_true", help="使用更热情的标点")
    return parser


args = build_parser().parse_args()
ending = "！！！" if args.excited else "。"
for index in range(1, args.count + 1):
    print(f"{index}. 你好，{args.name}{ending}")


# 小练习：添加 --language 参数，choices=["zh", "en"]，切换问候语言。
