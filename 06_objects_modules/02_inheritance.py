"""继承和方法重写：让相似对象共享行为，再定义各自的差异。

适用场景：几个类确实存在“是一种”的关系，例如狗是一种动物。
先学：类和对象。不要为了复用几行代码就强行建立继承关系。
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "发出声音"

    def describe(self):
        return f"{self.name}：{self.speak()}"


class Dog(Animal):
    # 不写 __init__ 时，可以直接继承父类的初始化方法。
    def speak(self):
        return "汪汪"


class Cat(Animal):
    def __init__(self, name, color):
        # super() 调用父类的方法，不必重复初始化 name。
        super().__init__(name)
        self.color = color

    def speak(self):
        return "喵喵"


pets = [Dog("小黑"), Cat("小白", "白色")]
for pet in pets:
    # 同样调用 describe()，得到的声音由具体对象决定。
    print(pet.describe())
print("猫的颜色：", pets[1].color)
print("Dog 对象也是 Animal 对象：", isinstance(pets[0], Animal))


# 小练习：添加 Bird 类，重写 speak()，再加入 pets 列表。
