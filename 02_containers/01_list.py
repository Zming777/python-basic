# 列表按顺序保存多个值，可以添加、删除和修改。
# 场景：记录待办事项、成绩或购物清单。
print(f"this is my first to create branch into githun!")
fruits = ["苹果", "香蕉", "橘子"]
print(fruits[0])  # 苹果：下标从 0 开始。
print(fruits[-1])  # 橘子
print(len(fruits))  # 3

fruits.append("葡萄")
fruits[0] = "青苹果"
print(fruits)  # ['青苹果', '香蕉', '橘子', '葡萄']

last = fruits.pop()  # 删除并返回最后一个元素。
print(last)  # 葡萄
fruits.remove("香蕉")  # 删除第一个匹配的值；找不到会报错。
print(fruits)  # ['青苹果', '橘子']

numbers = [8, 3, 5]
print(sorted(numbers))  # [3, 5, 8]：sorted 返回一个新列表。
print(numbers)  # [8, 3, 5]：原列表保持不变。

# 练习：创建三个待办事项，添加一项，再删除已完成的一项。
