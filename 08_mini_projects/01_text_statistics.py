"""小项目：统计一段英文文本，输出词频和最长单词。

会用到：字符串、正则表达式、函数、Counter、排序、循环。
何时用：快速了解文章中常出现哪些词，或生成简单文本摘要。
运行：python -X utf8 08_mini_projects/01_text_statistics.py
本例只在内存中处理固定样例，没有文件读写，也不需要输入。
"""

from collections import Counter
import re


SAMPLE_TEXT = """Python makes learning fun.
Learning Python takes practice, and practice builds confidence.
Write small programs. Read them. Run them. Improve them!"""


def extract_words(text):
    """提取英文字母组成的单词，并统一转为小写。"""
    # [a-z]+ 表示连续的一个或多个英文字母。
    # 这是适合当前样例的简化规则，不处理中文分词或英语缩写。
    return re.findall(r"[a-z]+", text.lower())


def analyze_text(text):
    """返回统计字典，把数据计算与打印显示分开。"""
    words = extract_words(text)
    frequencies = Counter(words)

    # 先按次数从高到低，再按字母顺序，次数相同时结果仍稳定。
    ranked_words = sorted(
        frequencies.items(),
        key=lambda item: (-item[1], item[0]),
    )
    # default 防止空文本导致 max([]) 报错。
    longest_word = max(sorted(frequencies), key=len, default="")
    return {
        "characters": len(text),
        "non_space_characters": sum(not char.isspace() for char in text),
        "lines": len(text.splitlines()),
        "word_count": len(words),
        "unique_word_count": len(frequencies),
        "longest_word": longest_word,
        "ranked_words": ranked_words,
    }


def print_report(result):
    """将统计结果整理成容易阅读的报告。"""
    print("\n=== 文本统计报告 ===")
    print("总字符数（含空白）：", result["characters"])
    print("非空白字符数（含标点）：", result["non_space_characters"])
    print("行数：", result["lines"])
    print("单词总数：", result["word_count"])
    print("不同单词数：", result["unique_word_count"])
    print("最长单词：", result["longest_word"] or "（没有单词）")
    print("\n最常见的 5 个单词：")
    for word, count in result["ranked_words"][:5]:
        print("  {:12s} {} 次 {}".format(word, count, "#" * count))
    if not result["ranked_words"]:
        print("  （没有可统计的英文单词）")


def main():
    print("=== 原始样例 ===")
    print(SAMPLE_TEXT)
    result = analyze_text(SAMPLE_TEXT)
    print_report(result)

    print("\n=== 空文本也能处理 ===")
    empty_result = analyze_text("")
    print("空文本的单词数：", empty_result["word_count"])
    print("空文本的词频列表：", empty_result["ranked_words"])


if __name__ == "__main__":
    main()

# 小练习：
# 1. 改写 SAMPLE_TEXT，运行前猜测最常见的单词。
# 2. 将前 5 个改成前 10 个，再加入一个平均单词长度指标。
# 3. 排除 and、them 等常见词，观察词频榜的变化。
