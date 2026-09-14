# 元组保存一组固定结构的数据，不能替换其中的元素。
# 场景：表示坐标、图片尺寸等一组有关联的值。

point = (3, 5)
print(point[0])  # 3
print(point[1])  # 5

x, y = point
print("横坐标：", x, "纵坐标：", y)

# 单元素元组需要逗号，否则括号只是普通分组。
print(type((42,)).__name__)  # tuple
print(type((42)).__name__)  # int

# 元组本身不能修改，但里面引用的列表仍然可以修改。
student = ("小明", [80, 90])
student[1].append(95)
print(student)  # ('小明', [80, 90, 95])
# point[0] = 9 会报 TypeError；这里只解释，没有执行。

# 练习：用元组保存图片的宽和高，再计算宽乘以高。
