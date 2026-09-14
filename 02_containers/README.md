# 02 常用容器

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 02.01 | 列表 | [01_list.py](01_list.py) |
| 02.02 | 元组 | [02_tuple.py](02_tuple.py) |
| 02.03 | 字典 | [03_dict.py](03_dict.py) |
| 02.04 | 集合 | [04_set.py](04_set.py) |
| 02.05 | 切片 | [05_slicing.py](05_slicing.py) |
| 02.06 | 解包 | [06_unpacking.py](06_unpacking.py) |
| 02.07 | 赋值、浅复制与深复制 | [07_copy.py](07_copy.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。

## 02.01 列表

打开 [01_list.py](01_list.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
苹果
橘子
3
['青苹果', '香蕉', '橘子', '葡萄']
葡萄
['青苹果', '橘子']
[3, 5, 8]
[8, 3, 5]
```

</details>

## 02.02 元组

打开 [02_tuple.py](02_tuple.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
3
5
横坐标： 3 纵坐标： 5
tuple
int
('小明', [80, 90, 95])
```

</details>

## 02.03 字典

打开 [03_dict.py](03_dict.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
小明
{'name': '小明', 'age': 21, 'city': '杭州'}
未填写
True
杭州
{'name': '小明', 'age': 21}
name → 小明
age → 21
```

</details>

## 02.04 集合

打开 [04_set.py](04_set.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
[1, 2, 3]
['Git', 'Python', 'SQL']
True
['Python']
['Git', 'Python', 'SQL']
['Git']
set
dict
```

</details>

## 02.05 切片

打开 [05_slicing.py](05_slicing.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
[10, 20, 30]
[0, 10, 20]
[30, 40, 50]
[40, 50]
[0, 20, 40]
[50, 40, 30, 20, 10, 0]
2026
09
[0, 10, 20, 30, 40, 50]
```

</details>

## 02.06 解包

打开 [06_unpacking.py](06_unpacking.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
小明
20
10
[20, 30, 40]
['阅读', '练习', '复习']
{'theme': 'dark', 'font_size': 14}
```

</details>

## 02.07 赋值、浅复制与深复制

打开 [07_copy.py](07_copy.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
['苹果', '香蕉']
['苹果']
[['苹果', '梨'], ['香蕉']]
True
[['苹果'], ['香蕉']]
[['苹果', '梨'], ['香蕉']]
False
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 02_containers/01_list.py
```

上一个目录：[基础语法](../01_basics/README.md)
下一个目录：[判断与循环](../03_control_flow/README.md)
