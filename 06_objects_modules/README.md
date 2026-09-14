# 06 类、模块与类型标注

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 06.01 | 类与对象 | [01_classes.py](01_classes.py) |
| 06.02 | 继承 | [02_inheritance.py](02_inheritance.py) |
| 06.03 | dataclass 数据类 | [03_dataclasses.py](03_dataclasses.py) |
| 06.04 | 模块与程序入口 | [04_modules.py](04_modules.py) |
| 06.05 | 类型标注 | [05_type_hints.py](05_type_hints.py) |
| 06.06 | 装饰器 | [06_decorators.py](06_decorators.py) |
| 06.07 | property 属性 | [07_properties.py](07_properties.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。

## 06.01 类与对象

打开 [01_classes.py](01_classes.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 读取属性： 小明
2. 调用方法： 我叫小明，目前的分数是 70
3. 学习之后： 我叫小明，目前的分数是 80
4. 另一个对象有自己的数据： 我叫小红，目前的分数是 85
5. 对象属于 Student 类： True
```

</details>

## 06.02 继承

打开 [02_inheritance.py](02_inheritance.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
小黑：汪汪
小白：喵喵
猫的颜色： 白色
Dog 对象也是 Animal 对象： True
```

</details>

## 06.03 dataclass 数据类

打开 [03_dataclasses.py](03_dataclasses.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 创建任务： Task(title='学习 Python', done=False, tags=[])
2. 修改字段： Task(title='学习 Python', done=True, tags=['基础'])
3. 另一个任务的标签仍是空列表： []
4. 转成字典： {'title': '学习 Python', 'done': True, 'tags': ['基础']}
5. 相同字段值的对象相等： True
```

</details>

## 06.04 模块与程序入口

打开 [04_modules.py](04_modules.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. math.sqrt(81)： 9.0
2. statistics.mean： 80
3. 当前文件名： 04_modules.py
4. 本文件的 __name__： __main__
5. 自己定义的函数： 你好，学习者！
```

</details>

## 06.05 类型标注

打开 [05_type_hints.py](05_type_hints.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 平均分： 80.0
2. 空列表的平均分： None
3. 姓和名： 李 小明
4. 城市： 上海
```

</details>

## 06.06 装饰器

打开 [06_decorators.py](06_decorators.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
开始调用 add
调用结束，结果是 7
1. 调用方获得结果： 7
2. 函数名： add
3. 函数说明： 返回两个数的和。
```

</details>

## 06.07 property 属性

打开 [07_properties.py](07_properties.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 面积（不用写括号）： 12
2. 改变宽后的面积： 20
3. 无效赋值被拒绝： 高必须大于 0
4. 高仍为： 4
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 06_objects_modules/01_classes.py
```

上一个目录：[文件与异常](../05_files_errors/README.md)
下一个目录：[常用标准库](../07_standard_library/README.md)
