"""property（选学）：以属性的写法读取计算结果，或检查赋值。

适用场景：希望使用 item.price 这样的接口，同时验证数据。
先学：类、异常和装饰器的基本写法。
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        # 每次访问时计算，不必在宽高改变后手动同步 area。
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("宽必须大于 0")
        # 单下划线表示约定内部使用，不是严格的访问权限限制。
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("高必须大于 0")
        self._height = value


rect = Rectangle(3, 4)
print("1. 面积（不用写括号）：", rect.area)
rect.width = 5
print("2. 改变宽后的面积：", rect.area)
try:
    rect.height = -1
except ValueError as error:
    print("3. 无效赋值被拒绝：", error)
print("4. 高仍为：", rect.height)


# 小练习：增加只读的 perimeter 属性，返回长方形的周长。
