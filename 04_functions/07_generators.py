"""yield 让函数按需逐个提供值，调用这种函数会得到生成器。
每次取值才继续执行；生成器被消耗完后不会自动从头开始。
"""


def countdown(start):
    while start > 0:
        print("函数准备产出：", start)
        yield start  # 交出一个值，然后暂停在这里。
        start -= 1


numbers = countdown(2)
print("已创建生成器，函数体还没有开始执行。")

# next 让函数执行到下一个 yield。
print("第一次取值：", next(numbers))

# for 从上次暂停的位置继续，处理剩余的值。
for number in numbers:
    print("循环收到：", number)

print("耗尽后再转成列表：", list(numbers))
# 要重新遍历，需要再次调用 countdown(...) 创建新的生成器。

# 小练习：把 countdown(2) 改为 countdown(3)，观察 for 多收到几个值。
