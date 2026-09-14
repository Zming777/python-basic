# 07 常用标准库

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 07.01 | 日期与时间 | [01_datetime.py](01_datetime.py) |
| 07.02 | 随机数与数学 | [02_random_math.py](02_random_math.py) |
| 07.03 | collections 容器工具 | [03_collections.py](03_collections.py) |
| 07.04 | itertools 迭代工具 | [04_itertools.py](04_itertools.py) |
| 07.05 | 正则表达式 | [05_regex.py](05_regex.py) |
| 07.06 | 命令行参数 | [06_argparse.py](06_argparse.py) |
| 07.07 | SQLite 数据库 | [07_sqlite.py](07_sqlite.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。
随机数例子使用固定种子；部分抽样结果可能随 Python 版本变化。

## 07.01 日期与时间

打开 [01_datetime.py](01_datetime.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 日期： 2000-05-20
2. 年、月、日： 2026 9 13
3. 格式化： 2026-09-13 14:30
4. 字符串转日期： 2026-10-01
5. 七天以后： 2026-09-20
6. 距离国庆的天数： 18
7. UTC 转为 UTC+8： 2026-09-13T14:30:00+08:00
```

</details>

## 07.02 随机数与数学

打开 [02_random_math.py](02_random_math.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 掷骰子（包含两端）： 6
2. 随机选择： 苹果
3. 不重复抽取两项： [1, 3]
4. 打乱后的列表： ['D', 'C', 'A', 'B']
5. 开平方： 5.0
6. 向下 / 向上取整： 3 4
7. 半径为 2 的圆面积： 12.57
8. 直接比较： False
9. 容差比较： True
```

</details>

## 07.03 collections 容器工具

打开 [03_collections.py](03_collections.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 计数： {'苹果': 3, '香蕉': 2, '梨': 1}
2. 最常见的两个： [('苹果', 3), ('香蕉', 2)]
3. 不存在的项计数为： 0
4. 按班级分组： {'一班': ['小明', '小华'], '二班': ['小红']}
5. 处理队首： 订单 A
6. 剩余队列： ['订单 B', '订单 C']
```

</details>

## 07.04 itertools 迭代工具

打开 [04_itertools.py](04_itertools.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 串接两组数据： [1, 2, 3, 4]
2. 颜色与尺码的所有搭配：
   白色，M码
   白色，L码
   蓝色，M码
   蓝色，L码
3. 三个人中任选两人： [('A', 'B'), ('A', 'C'), ('B', 'C')]
4. 同一个迭代器已用完： []
5. 只取前五个偶数： [10, 12, 14, 16, 18]
6. 下一项是： 20
```

</details>

## 07.05 正则表达式

打开 [05_regex.py](05_regex.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 提取所有数字片段： ['123', '25', '456', '80']
2. 提取订单编号： ['A123', 'B456']
3. 第一个完整匹配： 金额 25 元
4. 金额转为整数： 25
5. A123 是完整的合法编号：True
5. a123 是完整的合法编号：False
5. A1234 是完整的合法编号：False
6. 把连续空白替换成一个空格： Python 很好学 一起练习
```

</details>

## 07.06 命令行参数

打开 [06_argparse.py](06_argparse.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 你好，学习者。
```

</details>

## 07.07 SQLite 数据库

打开 [07_sqlite.py](07_sqlite.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 页数不少于 200 的书：
   自动化脚本：220 页
   数据处理：260 页
2. 修改后的总页数： 670
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 07_standard_library/01_datetime.py
```

上一个目录：[类、模块与类型标注](../06_objects_modules/README.md)
下一个目录：[选做：综合练习](../08_mini_projects/README.md)
