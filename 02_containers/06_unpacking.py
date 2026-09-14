# 解包把一组数据分配给多个变量；* 可以收集剩余元素。
# 场景：拆开一条记录，或者组合多个列表。

name, age = ("小明", 20)
print(name)  # 小明
print(age)  # 20

first, *rest = [10, 20, 30, 40]
print(first)  # 10
print(rest)  # [20, 30, 40]：收集得到的是列表。

# 列表里面的 * 则是把另一组元素展开。
morning = ["阅读", "练习"]
plan = [*morning, "复习"]
print(plan)  # ['阅读', '练习', '复习']

# 字典用 ** 展开，重复的键以右侧的值为准。
defaults = {"theme": "light", "font_size": 14}
settings = {**defaults, "theme": "dark"}
print(settings)  # {'theme': 'dark', 'font_size': 14}

# 练习：把 [1, 2, 3, 4] 拆成 first、middle、last，其中 middle 用 * 收集。
