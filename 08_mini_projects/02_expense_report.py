"""小项目：将样例支出按分类汇总，打印金额报告。

会用到：字典、列表、函数、Decimal、排序、格式化输出。
何时用：汇总账单、订单或其他需要准确表示金额的数据。
运行：python -X utf8 08_mini_projects/02_expense_report.py
本例只处理内置虚构数据，没有文件读写，也不需要输入。
"""

from decimal import Decimal


# 金额用字符串提供，避免先变成 float 时引入二进制近似值。
SAMPLE_EXPENSES = [
    {"category": "餐饮", "item": "早餐", "amount": "8.50"},
    {"category": "交通", "item": "地铁", "amount": "4.00"},
    {"category": "餐饮", "item": "午餐", "amount": "22.80"},
    {"category": "学习", "item": "练习本", "amount": "12.90"},
    {"category": "交通", "item": "公交", "amount": "2.00"},
    {"category": "学习", "item": "书籍", "amount": "39.90"},
]


def parse_amount(text):
    """转换金额，拒绝负数、非有限值及小于分的精度。"""
    amount = Decimal(text)
    if not amount.is_finite() or amount < 0:
        raise ValueError("样例支出必须是有限的非负金额")
    if amount != amount.quantize(Decimal("0.01")):
        raise ValueError("样例支出最多保留两位小数")
    return amount


def summarize_expenses(expenses):
    """分别累计各分类金额和全部支出，返回两个结果。"""
    by_category = {}
    total = Decimal("0.00")
    for expense in expenses:
        category = expense["category"]
        amount = parse_amount(expense["amount"])
        current = by_category.get(category, Decimal("0.00"))
        by_category[category] = current + amount
        total += amount
    return by_category, total


def main():
    print("=== 样例明细（金额单位：元） ===")
    for expense in SAMPLE_EXPENSES:
        print("{} / {}：{:.2f}".format(
            expense["category"], expense["item"],
            parse_amount(expense["amount"]),
        ))

    by_category, total = summarize_expenses(SAMPLE_EXPENSES)
    print("\n=== 按分类汇总：金额从高到低 ===")
    ranked = sorted(by_category.items(), key=lambda item: (-item[1], item[0]))
    for category, amount in ranked:
        # 显示百分比时保留一位小数，不把显示结果用于金额累计。
        percentage = amount / total * 100 if total else Decimal("0")
        print("{}：{:>6.2f} 元，占 {:>5.1f}%".format(
            category, amount, percentage,
        ))

    print("合计：{:.2f} 元".format(total))
    print("记录数：", len(SAMPLE_EXPENSES))
    if ranked:
        print("支出最多的分类：", ranked[0][0])

    print("\n=== 为什么金额使用 Decimal？ ===")
    print('Decimal("0.10") + Decimal("0.20") =',
          Decimal("0.10") + Decimal("0.20"))
    print("每一笔金额都从字符串转换，计算全程不使用 float。")

    # 空列表也能正常汇总，累计初值是 Decimal("0.00")。
    _, empty_total = summarize_expenses([])
    print("没有支出时的合计：{:.2f} 元".format(empty_total))


if __name__ == "__main__":
    main()

# 小练习：
# 1. 增加一条娱乐支出，观察分类排名与合计如何变化。
# 2. 增加预算 Decimal("100.00")，打印预算减去总支出的余额。
# 3. 将一个金额改成 "-1.00"，阅读报错后再改回来。
