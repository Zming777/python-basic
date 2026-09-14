"""while：只要条件为真，就重复执行循环体。
这里模拟倒计时，只打印数字，不会真的等待。
"""

remaining = 3

while remaining > 0:
    print(f"剩余：{remaining}")
    # 每轮减一，让条件最终变为假；漏掉这行会一直循环。
    remaining -= 1

# while 在每轮开始前检查条件，变成 0 后就不再进入循环。
print("倒计时结束，此时 remaining =", remaining)

# 小练习：把 remaining 改为 5，再改为 0，分别观察输出。
