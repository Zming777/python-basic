"""lambda 创建简短函数；sorted 的 key 指定排序依据。
lambda 只能写一个表达式，复杂逻辑使用 def 定义普通函数。
"""

students = [
    {"name": "小林", "score": 88},
    {"name": "小周", "score": 95},
    {"name": "小陈", "score": 82},
]

# student 是参数，冒号右边的 student["score"] 是返回的排序依据。
# reverse=True 表示从大到小；sorted 返回新列表，不改原列表的顺序。
ranked = sorted(students, key=lambda student: student["score"], reverse=True)

for student in ranked:
    print(f"{student['name']}：{student['score']} 分")

# 小练习：把 reverse 改为 False，观察成绩单的顺序。
