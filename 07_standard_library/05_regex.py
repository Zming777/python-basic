"""re 正则表达式：按模式查找、验证和替换文本。

适用场景：提取日志中的数字、检查简单编号、整理空白。
简单的固定字符串判断优先用 in、startswith、replace 等方法。
"""

import re


text = "订单 A123 金额 25 元；订单 B456 金额 80 元"
# 原始字符串 r"..." 可以保留反斜杠，便于书写正则。
print("1. 提取所有数字片段：", re.findall(r"\d+", text))
print("2. 提取订单编号：", re.findall(r"[A-Z]\d{3}", text))

match = re.search(r"金额 (\d+) 元", text)
if match is not None:
    # group(0) 是整个匹配；group(1) 是第一个括号内的部分。
    print("3. 第一个完整匹配：", match.group(0))
    print("4. 金额转为整数：", int(match.group(1)))

pattern = re.compile(r"[A-Z][0-9]{3}")
for value in ["A123", "a123", "A1234"]:
    print(f"5. {value} 是完整的合法编号：{bool(pattern.fullmatch(value))}")

messy = "Python    很好学\t一起练习"
print("6. 把连续空白替换成一个空格：", re.sub(r"\s+", " ", messy))
# search 找到一部分即可；fullmatch 要求整个字符串都符合模式。


# 小练习：从 "温度 18 度，湿度 65%" 中取出所有整数并求和。
