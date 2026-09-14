"""dataclass：简化主要用来保存数据的类。

适用场景：表示配置、记录、任务等。Python 3.7 起内置，无需安装。
先学：类和对象；字段后面的冒号是类型标注。
"""

from dataclasses import asdict, dataclass, field


@dataclass
class Task:
    # 自动生成 __init__、便于阅读的 __repr__ 和按字段比较的 __eq__。
    title: str
    done: bool = False
    # 每个实例获得一个新列表；不要让不同任务共享可变默认值。
    tags: list = field(default_factory=list)


task = Task("学习 Python")
another = Task("整理笔记")
print("1. 创建任务：", task)

task.tags.append("基础")
task.done = True
print("2. 修改字段：", task)
print("3. 另一个任务的标签仍是空列表：", another.tags)

print("4. 转成字典：", asdict(task))
print("5. 相同字段值的对象相等：", Task("阅读") == Task("阅读"))

# 类型标注不会在运行时自动检查传入的值，仍需自行验证数据。


# 小练习：添加 priority: int = 1 字段，创建一个优先级为 3 的任务。
