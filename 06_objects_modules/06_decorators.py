"""装饰器（选学）：在不修改函数主体的情况下增加共同的行为。

适用场景：日志、统计调用、检查条件。先学函数、*args 和 **kwargs。
第一次学 Python 可以先跳过，熟悉函数之后再回来。
"""

from functools import wraps


def announce(func):
    # 装饰器接收一个函数，再返回一个新函数。
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"开始调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"调用结束，结果是 {result}")
        # 别忘记返回结果，否则调用者只能拿到 None。
        return result

    return wrapper


@announce
def add(a, b):
    """返回两个数的和。"""
    return a + b


# @announce 大致等价于定义函数后执行 add = announce(add)。
total = add(3, b=4)
print("1. 调用方获得结果：", total)
# wraps 保留被装饰函数的名称、文档等信息。
print("2. 函数名：", add.__name__)
print("3. 函数说明：", add.__doc__)


# 小练习：定义 multiply(a, b)，也加上 @announce，观察输出顺序。
