"""模块、import 和程序入口：复用已有代码。

一个 .py 文件就是一个模块。Python 自带的模块组成标准库。
适用场景：拆分项目、使用已有功能。这个示例可直接独立运行。
"""

# 方式一：导入整个模块，调用时写 模块名.功能名。
import math

# 方式二：只导入某个名称。
from pathlib import Path

# 方式三：起别名（这里只为演示，不必给所有模块都起别名）。
import statistics as stats


def greet(name):
    """假如别的文件导入本模块，也可以使用这个函数。"""
    return f"你好，{name}！"


def main():
    print("1. math.sqrt(81)：", math.sqrt(81))
    print("2. statistics.mean：", stats.mean([70, 80, 90]))
    print("3. 当前文件名：", Path(__file__).name)
    print("4. 本文件的 __name__：", __name__)
    print("5. 自己定义的函数：", greet("学习者"))

    # 自建模块时，可以创建 helpers.py，内有 def greet(name): ...
    # 另一个同目录脚本写 from helpers import greet 即可使用。
    # 模块名请用字母、数字和下划线，且不要以数字开头。
    # 本课程的数字前缀用于学习排序；这些文件主要作为脚本运行。
    # 避免把文件命名为 math.py/json.py，以免遮住标准库模块。


# 直接运行本文件：__name__ == "__main__"，执行 main()。
# 被 import 时：__name__ 是模块名，不执行这个入口里的演示。
if __name__ == "__main__":
    main()

# 小练习：导入 math.ceil，观察 ceil(3.2) 与 int(3.2) 的差别。
