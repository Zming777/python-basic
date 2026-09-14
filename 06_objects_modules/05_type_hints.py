"""类型标注：告诉读代码的人和编辑器，预期使用什么类型。

适用场景：函数参数增多、多人协作、给编辑器提供提示。
Python 3.8 使用 typing.List 等写法；类型标注本身不做运行时检查。
"""

from typing import Dict, List, Optional, Tuple


def average(scores: List[float]) -> Optional[float]:
    # Optional[float] 表示返回值可能是 float，也可能是 None。
    if not scores:
        return None
    return sum(scores) / len(scores)


def split_name(full_name: str) -> Tuple[str, str]:
    """教学约定：姓是第一个字，名是剩余部分。"""
    if len(full_name) < 2:
        raise ValueError("名字至少需要两个字")
    return full_name[0], full_name[1:]


scores: List[float] = [70.0, 80.0, 90.0]
student: Dict[str, str] = {"name": "李小明", "city": "上海"}

result = average(scores)
if result is not None:
    print("1. 平均分：", result)
print("2. 空列表的平均分：", average([]))

family_name, given_name = split_name(student["name"])
print("3. 姓和名：", family_name, given_name)
print("4. 城市：", student["city"])
# 想在开发时检查类型，可进一步学习静态类型检查工具。


# 小练习：给一个接收整数列表并返回最大值的函数写类型标注。
# 同时决定：空列表应该返回 None，还是抛出异常？
