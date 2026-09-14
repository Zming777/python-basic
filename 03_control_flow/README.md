# 03 判断与循环

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 03.01 | if 条件判断 | [01_if.py](01_if.py) |
| 03.02 | for 循环 | [02_for.py](02_for.py) |
| 03.03 | while 循环 | [03_while.py](03_while.py) |
| 03.04 | range 数字范围 | [04_range.py](04_range.py) |
| 03.05 | break 与 continue | [05_break_continue.py](05_break_continue.py) |
| 03.06 | 推导式 | [06_comprehensions.py](06_comprehensions.py) |
| 03.07 | enumerate 与 zip | [07_enumerate_zip.py](07_enumerate_zip.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。

## 03.01 if 条件判断

打开 [01_if.py](01_if.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
成绩：合格
```

</details>

## 03.02 for 循环

打开 [02_for.py](02_for.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
加上 12 元，当前合计 12 元
加上 8 元，当前合计 20 元
加上 15 元，当前合计 35 元
最终合计：35 元
```

</details>

## 03.03 while 循环

打开 [03_while.py](03_while.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
剩余：3
剩余：2
剩余：1
倒计时结束，此时 remaining = 0
```

</details>

## 03.04 range 数字范围

打开 [04_range.py](04_range.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
range(5)： [0, 1, 2, 3, 4]
range(1, 5)： [1, 2, 3, 4]
range(1, 6, 2)： [1, 3, 5]
range(3, 0, -1)： [3, 2, 1]
```

</details>

## 03.05 break 与 continue

打开 [05_break_continue.py](05_break_continue.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
处理数字： 3
跳过负数： -1
处理数字： 5
遇到 0，停止处理。
循环结束。
```

</details>

## 03.06 推导式

打开 [06_comprehensions.py](06_comprehensions.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
普通循环： [1, 4, 9, 16, 25]
推导式： [1, 4, 9, 16, 25]
保留偶数： [2, 4]
```

</details>

## 03.07 enumerate 与 zip

打开 [07_enumerate_zip.py](07_enumerate_zip.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
第 1 位：小林
第 2 位：小周
小林：88 分
小周：92 分
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 03_control_flow/01_if.py
```

上一个目录：[常用容器](../02_containers/README.md)
下一个目录：[函数](../04_functions/README.md)
