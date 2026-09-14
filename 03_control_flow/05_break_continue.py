"""continue：跳过本轮；break：结束整个循环。
这里处理一组数字：跳过负数，遇到 0 就停止。
"""

numbers = [3, -1, 5, 0, 8]

for number in numbers:
    if number < 0:
        print("跳过负数：", number)
        continue

    if number == 0:
        print("遇到 0，停止处理。")
        break

    # continue 或 break 执行后，都不会走到本轮的这一行。
    print("处理数字：", number)

print("循环结束。")

# 小练习：把列表中的 0 去掉，观察最后的 8 是否会被处理。
