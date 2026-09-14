# int()、float()、str() 分别转换成整数、浮点数、字符串。
# 场景：把输入的数字文字转换成可以计算的数值。

quantity_text = "12"
print(quantity_text + quantity_text)  # 1212：字符串相加是拼接。

quantity = int(quantity_text)
print(quantity + quantity)  # 24：整数相加是计算。

price = float("3.50")
print(quantity * price)  # 42.0

age = 20
print("我今年 " + str(age) + " 岁")  # 数字转成文字后才能这样拼接。

print(int(3.9))  # 3：删除小数部分，不是四舍五入。
print(int(-3.9))  # -3：转换方向是趋向 0。
# int("十二")、int("3.9") 都会报 ValueError。

# 练习：把 "18.5" 转成浮点数，再加上 2。
