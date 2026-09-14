# 01 基础语法

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 01.01 | 输出与注释 | [01_print_comments.py](01_print_comments.py) |
| 01.02 | 变量与类型 | [02_variables.py](02_variables.py) |
| 01.03 | 数字与运算 | [03_numbers.py](03_numbers.py) |
| 01.04 | 字符串 | [04_strings.py](04_strings.py) |
| 01.05 | 类型转换 | [05_type_conversion.py](05_type_conversion.py) |
| 01.06 | input 输入 | [06_input.py](06_input.py) |
| 01.07 | f-string 格式化 | [07_fstrings.py](07_fstrings.py) |
| 01.08 | 布尔值与 None | [08_bool_none.py](08_bool_none.py) |
| 01.09 | 赋值与交换 | [09_assignment.py](09_assignment.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。

## 01.01 输出与注释

打开 [01_print_comments.py](01_print_comments.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
你好，Python！
3
姓名： 小明 年龄： 18
2026-09-14
第一行
第二行
```

</details>

## 01.02 变量与类型

打开 [02_variables.py](02_variables.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
小明
20
1.75
明年年龄： 21
str
int
```

</details>

## 01.03 数字与运算

打开 [03_numbers.py](03_numbers.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
11
5
24
2.6666666666666665
小时： 2
剩余分钟： 5
-3
8
20
0.30000000000000004
```

</details>

## 01.04 字符串

打开 [04_strings.py](04_strings.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
'  Alice  '
Alice
alice
学习 Python
P
n
6
True
['苹果', '香蕉', '橘子']
苹果 / 香蕉 / 橘子
```

</details>

## 01.05 类型转换

打开 [05_type_conversion.py](05_type_conversion.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1212
24
42.0
我今年 20 岁
3
-3
```

</details>

## 01.06 input 输入

打开 [06_input.py](06_input.py)，点击“运行 Python 文件”。

本例会等待你在终端输入姓名。以下结果以输入 `小明` 并按回车为例；自动采集的输出未包含键盘输入回显。

<details>
<summary>查看小结果</summary>

```text
请输入你的姓名：你好，小明！
输入内容的类型： str
```

</details>

## 01.07 f-string 格式化

打开 [07_fstrings.py](07_fstrings.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
你好，小明！
你今年 20 岁，明年 21 岁。
买 3 件，合计 37.50 元。
单价：12.50
完成比例：87.5%
编号：007
```

</details>

## 01.08 布尔值与 None

打开 [08_bool_none.py](08_bool_none.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
True
False
True
False
True
True
True
True
False
True
```

</details>

## 01.09 赋值与交换

打开 [09_assignment.py](09_assignment.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
5
75
8 5
5 8
10 20
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 01_basics/01_print_comments.py
```

下一个目录：[常用容器](../02_containers/README.md)
