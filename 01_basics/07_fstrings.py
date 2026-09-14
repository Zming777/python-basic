# f-string 在字符串前加 f，用 {变量} 把值放进文字中。
# 场景：显示姓名、价格或计算结果。

name = "小明"
age = 20
print(f"你好，{name}！")
print(f"你今年 {age} 岁，明年 {age + 1} 岁。")

price = 12.5
quantity = 3
print(f"买 {quantity} 件，合计 {price * quantity:.2f} 元。")

# :.2f 表示显示两位小数，只改变显示文字，不改变原值。
print(f"单价：{price:.2f}")  # 单价：12.50
print(f"完成比例：{0.875:.1%}")  # 完成比例：87.5%
print(f"编号：{7:03d}")  # 编号：007

# 练习：设置商品名和价格，用 f-string 打印一句介绍。
