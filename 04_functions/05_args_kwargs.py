"""*args 接收多个位置参数；**kwargs 接收多个关键字参数。
args 和 kwargs 是惯用名称，真正决定语法的是 * 和 **。
"""


def add_all(*args):
    # args 是元组，可以接收任意数量的数字。
    return sum(args)


def show_profile(**kwargs):
    # kwargs 是字典，键是调用时写的参数名。
    print("收到的资料：", kwargs)


print("直接传数字：", add_all(2, 3, 5))
show_profile(name="小林", city="杭州")

# 调用时反过来使用 * 和 **：把已有列表或字典展开为参数。
numbers = [2, 3, 5]
profile = {"name": "小周", "city": "南京"}
print("展开列表：", add_all(*numbers))
show_profile(**profile)

# 小练习：给 numbers 增加一个数字，给 profile 增加 hobby，重新运行。
