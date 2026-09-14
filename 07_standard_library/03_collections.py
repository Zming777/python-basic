"""collections：常用容器的补充工具。

适用场景：Counter 计数，defaultdict 分组，deque 处理队列。
先学：列表、字典、循环。
"""

from collections import Counter, defaultdict, deque


fruits = ["苹果", "香蕉", "苹果", "梨", "香蕉", "苹果"]
counts = Counter(fruits)
print("1. 计数：", dict(counts))
print("2. 最常见的两个：", counts.most_common(2))
print("3. 不存在的项计数为：", counts["草莓"])

students = [("一班", "小明"), ("二班", "小红"), ("一班", "小华")]
groups = defaultdict(list)
for classroom, name in students:
    # 遇到新键时自动建立空列表，不必先判断键是否存在。
    groups[classroom].append(name)
print("4. 按班级分组：", dict(groups))

queue = deque(["订单 A", "订单 B"])
queue.append("订单 C")
print("5. 处理队首：", queue.popleft())
print("6. 剩余队列：", list(queue))
# deque 在两端添加和删除都很方便，适合先进先出的队列。


# 小练习：用 Counter 统计字符串 "banana" 中每个字母的出现次数。
