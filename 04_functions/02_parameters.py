"""参数：让同一个函数接收不同的数据。
可以按位置传入，也可以写参数名；有默认值的参数可以省略。
"""


def introduce(name, city="杭州"):
    print(f"我叫 {name}，来自 {city}。")


# 位置参数：按顺序对应 name、city。
introduce("小林", "南京")

# 关键字参数：通过名字对应，顺序可以调整。
introduce(city="成都", name="小周")

# 默认参数：没有传 city，使用定义时写的“杭州”。
introduce("小陈")

# 小练习：增加一个默认值为“阅读”的 hobby 参数，并在函数中打印。
