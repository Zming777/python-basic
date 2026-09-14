# 集合保存不重复的元素，不保证显示顺序，也不能用下标访问。
# 场景：数据去重，或者查找两组数据的共同项。

numbers = set([1, 2, 2, 3, 1])
print(sorted(numbers))  # [1, 2, 3]：排序后显示，方便观察。

skills = {"Python", "Git"}
skills.add("SQL")
skills.add("Python")  # 已有的元素不会重复添加。
print(sorted(skills))  # ['Git', 'Python', 'SQL']
print("Git" in skills)  # True

group_a = {"Python", "Git"}
group_b = {"Python", "SQL"}
print(sorted(group_a & group_b))  # ['Python']：交集，双方都有。
print(sorted(group_a | group_b))  # ['Git', 'Python', 'SQL']：并集。
print(sorted(group_a - group_b))  # ['Git']：A 有但 B 没有。

print(type(set()).__name__)  # set：空集合写 set()。
print(type({}).__name__)  # dict：{} 是空字典。

# 练习：为两个人各建一个兴趣集合，再找出共同兴趣。
