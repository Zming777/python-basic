# 字符串是用引号包起来的文字。
# 场景：清理输入、替换文字、拆分简单文本。

name = "  Alice  "
clean_name = name.strip()  # 去掉两端空白，得到一个新字符串。
print(repr(name))  # '  Alice  '：原字符串没有改变。
print(clean_name)  # Alice
print(clean_name.lower())  # alice

text = "学习 Java"
print(text.replace("Java", "Python"))  # 学习 Python

language = "Python"
print(language[0])  # P：下标从 0 开始。
print(language[-1])  # n：-1 表示最后一个字符。
print(len(language))  # 6
print("Py" in language)  # True

fruits = "苹果,香蕉,橘子".split(",")
print(fruits)  # ['苹果', '香蕉', '橘子']
print(" / ".join(fruits))  # 苹果 / 香蕉 / 橘子

# 练习：去掉 "  HELLO  " 两端的空白，再转成小写。
