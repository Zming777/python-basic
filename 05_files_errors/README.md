# 05 文件与异常

[返回项目说明](../README.md)

在 VS Code 左侧打开下面任意一个 `.py` 文件，点击“运行 Python 文件”，在下方终端看结果。
每个示例都可以独立运行；改一两个值、保存，再次运行，观察变化。

| 编号 | 知识点 | 打开文件 |
| --- | --- | --- |
| 05.01 | 路径 | [01_paths.py](01_paths.py) |
| 05.02 | 读写文本 | [02_text_files.py](02_text_files.py) |
| 05.03 | 读写 CSV | [03_csv_files.py](03_csv_files.py) |
| 05.04 | 读写 JSON | [04_json_files.py](04_json_files.py) |
| 05.05 | 异常处理 | [05_exceptions.py](05_exceptions.py) |
| 05.06 | 上下文管理 | [06_context_manager.py](06_context_manager.py) |
| 05.07 | 日志 | [07_logging.py](07_logging.py) |

以下结果使用当前样例在 Python 3.8.7 下实测。修改代码后，输出也会改变。
输出里的 `<项目目录>` 代表项目实际保存位置；路径分隔符随操作系统而不同。

## 05.01 路径

打开 [01_paths.py](01_paths.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
文件名： hello.txt
不含扩展名： hello
扩展名： .txt
文件存在： True
完整位置： <项目目录>\_practice_output\01_paths\notes\hello.txt
换个扩展名： hello.md
```

</details>

## 05.02 读写文本

打开 [02_text_files.py](02_text_files.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
第 1 行：第一天：学习变量
第 2 行：第二天：学习列表
第 3 行：第三天：学习文件操作
文件位置： <项目目录>\_practice_output\02_text_files\study_notes.txt
```

</details>

## 05.03 读写 CSV

打开 [03_csv_files.py](03_csv_files.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
小林 原分数： 86 加 5 分后： 91
小周 原分数： 92 加 5 分后： 97
表格位置： <项目目录>\_practice_output\03_csv_files\scores.csv
```

</details>

## 05.04 读写 JSON

打开 [04_json_files.py](04_json_files.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
JSON 字符串： {"username": "小林", "daily_minutes": 30, "enabled": true}
读回用户名： 小林
文件读回后与原字典相等： True
文件位置： <项目目录>\_practice_output\04_json_files\settings.json
```

</details>

## 05.05 异常处理

打开 [05_exceptions.py](05_exceptions.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
'18' 转换成功，年龄是 18
这一条处理结束。
'十八' 转换失败：invalid literal for int() with base 10: '十八'
这一条处理结束。
'-3' 转换失败：年龄不能为负数
这一条处理结束。
```

</details>

## 05.06 上下文管理

打开 [06_context_manager.py](06_context_manager.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
1. 打开文件
2. 在 with 里面写入内容
3. 关闭文件
4. 接到样例错误： 故意出错，看看文件是否仍会关闭
文件已关闭： True
文件位置： <项目目录>\_practice_output\06_context_manager\context_note.txt
```

</details>

## 05.07 日志

打开 [07_logging.py](07_logging.py)，点击“运行 Python 文件”。

<details>
<summary>查看小结果</summary>

```text
INFO | 开始学习 Python。
WARNING | 这是一条提醒。
ERROR | 这是一条样例错误消息。
日志位置： <项目目录>\_practice_output\07_logging\study.log
```

</details>

需要时，也可以在项目根目录的终端直接运行单个文件，例如：

```powershell
python 05_files_errors/01_paths.py
```

上一个目录：[函数](../04_functions/README.md)
下一个目录：[类、模块与类型标注](../06_objects_modules/README.md)
