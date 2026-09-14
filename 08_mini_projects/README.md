# 08 选做：综合练习

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 08.01 | 文本统计 | [01_text_statistics.py](01_text_statistics.py) |
| 08.02 | 支出报表 | [02_expense_report.py](02_expense_report.py) |
| 08.03 | JSON 待办事项 | [03_todo_json.py](03_todo_json.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。

## 08.01 文本统计

打开 [01_text_statistics.py](01_text_statistics.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
=== 原始样例 ===
Python makes learning fun.
Learning Python takes practice, and practice builds confidence.
Write small programs. Read them. Run them. Improve them!

=== 文本统计报告 ===
总字符数（含空白）： 147
非空白字符数（含标点）： 127
行数： 3
单词总数： 21
不同单词数： 16
最长单词： confidence

最常见的 5 个单词：
  them         3 次 ###
  learning     2 次 ##
  practice     2 次 ##
  python       2 次 ##
  and          1 次 #

=== 空文本也能处理 ===
空文本的单词数： 0
空文本的词频列表： []
```

</details>

## 08.02 支出报表

打开 [02_expense_report.py](02_expense_report.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
=== 样例明细（金额单位：元） ===
餐饮 / 早餐：8.50
交通 / 地铁：4.00
餐饮 / 午餐：22.80
学习 / 练习本：12.90
交通 / 公交：2.00
学习 / 书籍：39.90

=== 按分类汇总：金额从高到低 ===
学习： 52.80 元，占  58.6%
餐饮： 31.30 元，占  34.7%
交通：  6.00 元，占   6.7%
合计：90.10 元
记录数： 6
支出最多的分类： 学习

=== 为什么金额使用 Decimal？ ===
Decimal("0.10") + Decimal("0.20") = 0.30
每一笔金额都从字符串转换，计算全程不使用 float。
没有支出时的合计：0.00 元
```

</details>

## 08.03 JSON 待办事项

打开 [03_todo_json.py](03_todo_json.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
=== 1. 在内存中创建三个样例任务 ===
[ ] 1. 独立运行一个列表示例
[ ] 2. 改写一个函数练习
[ ] 3. 理解 JSON 保存和读取
待完成：3 / 3

=== 2. 完成第一个任务并保存 ===
已保存到： <项目目录>\_practice_output\03_todo_json\sample_tasks.json

=== 3. 从磁盘重新读回 ===
[x] 1. 独立运行一个列表示例
[ ] 2. 改写一个函数练习
[ ] 3. 理解 JSON 保存和读取
待完成：2 / 3
读回内容与保存前一致： True
读回的是一个新列表： True
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 08_mini_projects/01_text_statistics.py
```

上一个目录：[常用标准库](../07_standard_library/README.md)
