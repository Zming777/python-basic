"""enumerate：同时取出序号和内容；zip：按位置配对。
下面用一份姓名和成绩数据，分别看看这两种写法。
"""

names = ["小林", "小周"]
scores = [88, 92]

# 默认序号从 0 开始；start=1 让展示的序号从 1 开始。
for number, name in enumerate(names, start=1):
    print(f"第 {number} 位：{name}")

# 第一个姓名配第一个分数，第二个姓名配第二个分数。
for name, score in zip(names, scores):
    print(f"{name}：{score} 分")

# zip 默认在最短的一组数据结束时停止，多出来的项不会被配对。
# 小练习：在 names 末尾增加“小陈”，观察两段循环输出有什么不同。
