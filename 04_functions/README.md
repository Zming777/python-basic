# 04 函数

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 04.01 | 定义与调用函数 | [01_define_call.py](01_define_call.py) |
| 04.02 | 函数参数 | [02_parameters.py](02_parameters.py) |
| 04.03 | 返回值 | [03_return.py](03_return.py) |
| 04.04 | 变量作用域 | [04_scope.py](04_scope.py) |
| 04.05 | args 与 kwargs | [05_args_kwargs.py](05_args_kwargs.py) |
| 04.06 | lambda 与排序 | [06_lambda_sorted.py](06_lambda_sorted.py) |
| 04.07 | 生成器与 yield | [07_generators.py](07_generators.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。

## 04.01 定义与调用函数

打开 [01_define_call.py](01_define_call.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
你好，小林！
你好，小周！
```

</details>

## 04.02 函数参数

打开 [02_parameters.py](02_parameters.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
我叫 小林，来自 南京。
我叫 小周，来自 成都。
我叫 小陈，来自 杭州。
```

</details>

## 04.03 返回值

打开 [03_return.py](03_return.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
收到返回值： 8
继续乘以 2： 16
函数内部打印： 8
show_sum 的返回值： None
```

</details>

## 04.04 变量作用域

打开 [04_scope.py](04_scope.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
函数内的局部变量： 函数练习
函数外仍然是： Python 入门
使用 global 修改后： Python 进阶
```

</details>

## 04.05 args 与 kwargs

打开 [05_args_kwargs.py](05_args_kwargs.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
直接传数字： 10
收到的资料： {'name': '小林', 'city': '杭州'}
展开列表： 10
收到的资料： {'name': '小周', 'city': '南京'}
```

</details>

## 04.06 lambda 与排序

打开 [06_lambda_sorted.py](06_lambda_sorted.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
小周：95 分
小林：88 分
小陈：82 分
```

</details>

## 04.07 生成器与 yield

打开 [07_generators.py](07_generators.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
已创建生成器，函数体还没有开始执行。
函数准备产出： 2
第一次取值： 2
函数准备产出： 1
循环收到： 1
耗尽后再转成列表： []
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 04_functions/01_define_call.py
```

上一个目录：[判断与循环](../03_control_flow/README.md)
下一个目录：[文件与异常](../05_files_errors/README.md)
