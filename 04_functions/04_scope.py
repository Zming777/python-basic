"""作用域：函数内的局部变量与函数外的全局变量可以同名。
函数内赋值默认创建局部变量；给全局变量重新赋值需使用 global。
"""

course = "Python 入门"


def use_local():
    course = "函数练习"
    print("函数内的局部变量：", course)


def change_global():
    global course
    course = "Python 进阶"


use_local()
print("函数外仍然是：", course)

change_global()
print("使用 global 修改后：", course)

# 实际写项目时，通常优先用参数和返回值传递数据，减少全局修改。
# 小练习：注释掉 change_global() 这一行调用，观察最后的结果。
