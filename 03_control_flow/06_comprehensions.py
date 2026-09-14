"""列表推导式：用一行代码完成简单的转换或筛选。
基本写法：[结果表达式 for 元素 in 数据 if 条件]。
"""

numbers = [1, 2, 3, 4, 5]

# 先看普通循环：计算每个数字的平方。
squares_by_loop = []
for number in numbers:
    squares_by_loop.append(number ** 2)
print("普通循环：", squares_by_loop)

# 把相同的转换写成列表推导式。
squares = [number ** 2 for number in numbers]
print("推导式：", squares)

# 末尾的 if 用来筛选；% 是求余数，除以 2 余 0 就是偶数。
even_numbers = [number for number in numbers if number % 2 == 0]
print("保留偶数：", even_numbers)

# 小练习：把筛选条件改成“只保留大于 3 的数字”。
