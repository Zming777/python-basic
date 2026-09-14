"""itertools（选学）：组合与串接可迭代对象。

适用场景：生成选项组合、合并遍历、按需取出少量数据。
先学：循环、生成器。下面的工具返回迭代器，按需产生结果。
"""

from itertools import chain, combinations, count, islice, product


print("1. 串接两组数据：", list(chain([1, 2], [3, 4])))

print("2. 颜色与尺码的所有搭配：")
for color, size in product(["白", "蓝"], ["M", "L"]):
    print(f"   {color}色，{size}码")

# combinations 不考虑顺序，A+B 和 B+A 算同一组。
pairs = combinations(["A", "B", "C"], 2)
print("3. 三个人中任选两人：", list(pairs))
print("4. 同一个迭代器已用完：", list(pairs))

# count 本身不会停止，必须限制读取的数量。
numbers = count(start=10, step=2)
print("5. 只取前五个偶数：", list(islice(numbers, 5)))
print("6. 下一项是：", next(numbers))

# 不要直接 list(count())，它会不断生成，耗尽内存。


# 小练习：用 product 生成两种饮料与三种甜点的所有搭配。
