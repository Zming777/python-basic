"""return 把结果交还调用者；print 只负责显示。
函数执行到 return 就会结束；没有写 return 时自动返回 None。
"""


def add(left, right):
    return left + right


def show_sum(left, right):
    print("函数内部打印：", left + right)


# 返回值可以存进变量，再参与后续计算。
total = add(3, 5)
print("收到返回值：", total)
print("继续乘以 2：", total * 2)

# 显示了一个数字，不代表把这个数字返回给了调用者。
result = show_sum(3, 5)
print("show_sum 的返回值：", result)

# 小练习：让 show_sum 在打印后也返回计算结果，观察最后一行。
