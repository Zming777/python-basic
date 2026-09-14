"""random 和 math：随机抽取、打乱数据，以及常见数学运算。

适用场景：小游戏、抽样、基础计算。
random 适合模拟与游戏；生成安全令牌时应使用 secrets 模块。
"""

import math
import random


# 局部随机数生成器 + 固定种子，方便在相同 Python 版本中复现。
rng = random.Random(42)
print("1. 掷骰子（包含两端）：", rng.randint(1, 6))
print("2. 随机选择：", rng.choice(["苹果", "香蕉", "梨"]))
print("3. 不重复抽取两项：", rng.sample([1, 2, 3, 4, 5], 2))

cards = ["A", "B", "C", "D"]
rng.shuffle(cards)  # 原地修改列表，返回值是 None。
print("4. 打乱后的列表：", cards)

print("5. 开平方：", math.sqrt(25))
print("6. 向下 / 向上取整：", math.floor(3.8), math.ceil(3.2))
print("7. 半径为 2 的圆面积：", round(math.pi * 2 ** 2, 2))
# 浮点数有表示误差，比较近似结果可使用 isclose。
print("8. 直接比较：", 0.1 + 0.2 == 0.3)
print("9. 容差比较：", math.isclose(0.1 + 0.2, 0.3))


# 小练习：模拟掷 10 次骰子，把每次结果保存到一个列表。
