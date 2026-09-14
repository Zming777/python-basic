"""range：表示一段整数序列，常用来循环固定次数。
规则是包含起点、不包含终点；list() 让这些数字直接显示出来。
"""

# 只有一个参数时，它是终点，默认从 0 开始。
print("range(5)：", list(range(5)))

# 两个参数分别是起点、终点。
print("range(1, 5)：", list(range(1, 5)))

# 第三个参数是步长；负数步长表示倒着数。
print("range(1, 6, 2)：", list(range(1, 6, 2)))
print("range(3, 0, -1)：", list(range(3, 0, -1)))

# 小练习：用 range 生成 2、4、6、8、10。
