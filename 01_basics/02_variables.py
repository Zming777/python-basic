# 变量是给数据起的名字，= 把右边的值赋给左边的名字。
# 场景：保存姓名、年龄等后面还会用到的数据。

user_name = "小明"
age = 20
height = 1.75

print(user_name)  # 小明
print(age)  # 20
print(height)  # 1.75

age = age + 1
print("明年年龄：", age)  # 21

# type() 可以查看值的类型。
print(type(user_name).__name__)  # str：字符串
print(type(age).__name__)  # int：整数

# 练习：增加一个 city 变量，再把它打印出来。
