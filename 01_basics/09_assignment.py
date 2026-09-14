# 赋值用于保存或更新数据，+= 表示在已有数值上增加。
# 场景：更新余额、计数器，或者交换两个变量。

count = 3
count += 2
print(count)  # 5

balance = 100
balance -= 25
print(balance)  # 75

width, height = 8, 5
print(width, height)  # 8 5
width, height = height, width
print(width, height)  # 5 8：先计算右侧，再分别赋给左侧。

# 给变量赋一个新整数，不会改变另一个变量的值。
first = 10
second = first
second = 20
print(first, second)  # 10 20
# 列表的赋值有共享对象的问题，后续“复制”示例会演示。

# 练习：用 *= 把一个初始为 6 的数翻倍。
