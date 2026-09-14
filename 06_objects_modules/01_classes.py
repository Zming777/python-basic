"""类和对象：把相关的数据与行为放在一起。

适用场景：表示学生、商品、订单等有状态的事物。
先学：函数、字典。self 表示当前这个对象。
"""


class Student:
    """类像一张设计图；每次调用 Student(...) 都创建一个对象。"""

    def __init__(self, name, score):
        # __init__ 在对象创建时初始化属性。
        self.name = name
        self.score = score

    def introduce(self):
        return f"我叫{self.name}，目前的分数是 {self.score}"

    def study(self, points):
        self.score += points


xiaoming = Student("小明", 70)
xiaohong = Student("小红", 85)

print("1. 读取属性：", xiaoming.name)
print("2. 调用方法：", xiaoming.introduce())
xiaoming.study(10)
print("3. 学习之后：", xiaoming.introduce())
print("4. 另一个对象有自己的数据：", xiaohong.introduce())

# 字典也能存数据；类还可以将操作这些数据的函数放在一起。
print("5. 对象属于 Student 类：", isinstance(xiaoming, Student))


# 小练习：添加 passed() 方法，返回这个学生是否达到 60 分。
