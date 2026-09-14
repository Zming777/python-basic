"""for：逐个取出列表中的元素。
这里把三件商品的价格加起来，每轮看看合计如何变化。
"""

prices = [12, 8, 15]
total = 0

for price in prices:
    # price 每轮是一个新价格；total 保留之前累计的结果。
    total += price
    print(f"加上 {price} 元，当前合计 {total} 元")

# 这行没有缩进到 for 里面，所以整个循环结束后才执行一次。
print(f"最终合计：{total} 元")

# 小练习：在 prices 中增加一个价格，观察合计与输出行数的变化。
