# Python 单文件练习

共 **8 个目录、54 个独立示例**。打开一个 `.py` 文件，运行它，观察一小段结果，再修改代码试一试。

兼容 Python 3.8 及以上版本，只用标准库，不需要安装额外的 Python 库。

## 在 VS Code 里这样使用

1. 用 VS Code 打开这个项目文件夹。
2. 在左侧展开 `01_basics`，打开 `01_print_comments.py`。
3. 点击右上角的 **运行 Python 文件**，或右键选择 **在终端中运行 Python 文件（Run Python File in Terminal）**。
4. 在下方终端看输出；改一个值，保存文件，再点一次运行。
5. 学完就打开下一个 `.py` 文件，用同样的方法运行。

**当前打开哪个文件，就运行哪个文件。** 文件之间没有执行顺序上的依赖。基础示例直接从上往下写，到函数、类的章节才引入对应的定义与调用。

例如，一个变量练习可以直接写成：

```python
age = 18
print(age)      # 输出 18
print(age + 1)  # 输出 19
```

如果当前仍开着之前的选课窗口，关闭它即可。现在的学习入口是左侧文件列表。

## 文件按学习顺序放好了

| 目录 | 内容 | 建议 |
| --- | --- | --- |
| [01_basics](01_basics/README.md) | 输出、变量、数字、字符串、类型转换、输入、格式化、布尔值、赋值 | 从这里开始，每次打开一个文件 |
| [02_containers](02_containers/README.md) | 列表、元组、字典、集合、切片、解包、复制 | 修改容器中的值并观察结果 |
| [03_control_flow](03_control_flow/README.md) | if、for、while、range、break/continue、推导式、enumerate/zip | 修改条件或循环次数 |
| [04_functions](04_functions/README.md) | 定义、参数、返回值、作用域、可变参数、lambda、生成器 | 观察函数定义与调用的区别 |
| [05_files_errors](05_files_errors/README.md) | 路径、文本、CSV、JSON、异常、with、日志 | 学习保存数据和处理错误 |
| [06_objects_modules](06_objects_modules/README.md) | 类、继承、dataclass、import、类型标注、装饰器、property | 后两项可以以后再学 |
| [07_standard_library](07_standard_library/README.md) | 日期、随机数、数学、计数分组、迭代工具、正则、命令行、SQLite | 用到哪个就打开哪个 |
| [08_mini_projects](08_mini_projects/README.md) | 文本统计、支出报表、JSON 待办事项 | 选做：稍长的综合例子，也各自独立运行 |

每个文件有中文说明、示例代码和小练习。各目录的 README 提供运行结果参考；日常学习直接打开 `.py` 文件就行。

也可以用 [学习打卡表](LEARNING_CHECKLIST.md) 记录进度，或用 [语法速查](docs/语法速查.md) 找到需要的写法。

## 只有这些例子稍有不同

- **input 输入课**：运行 `01_basics/06_input.py` 后，在下方终端输入姓名并按回车，才会显示问候结果。这里学习的就是键盘输入，不需要启动参数。
- **文件读写课**：结果文件保存在项目根目录的 `_practice_output/` 下，每课有自己的目录。每次运行会覆盖自己的样例文件，请把个人数据放在别处。
- **模块课**：为了讲解 `__name__` 和程序入口，会专门展示 `if __name__ == "__main__":`。
- **命令行参数课**：直接点运行会使用默认值。学到这一课时，再试终端里的 `--name`、`--count` 等选项。

## 遇到问题

- **没有运行按钮**：确认 VS Code 已安装 Microsoft 的 Python 扩展，并选择了本机 Python 解释器。
- **input 无法输入**：选择“在终端中运行 Python 文件”，点击下方“终端”面板输入；“输出”面板不能交互输入。
- **修改后结果没变**：先保存文件，再确认运行的是当前这个 `.py` 文件。
- **报错**：先看最后一行错误，再定位对应行号，检查缩进、冒号、引号和括号。

也可以在项目目录的终端直接运行某个文件：

```powershell
python 01_basics/01_print_comments.py
```

中文编码有问题时，在 `python` 后加上 `-X utf8`。`tools/check_examples.py` 是检查全部示例的维护工具，平时学习不用运行它。







附：目录介绍

你这个项目里，`01～08` 是学习代码，其他目录主要存放说明、运行结果和工具配置。** 我按实际结构给你解释。

先看学习用的 8 个目录：

| 目录                                                         | 中文意思      | 里面学什么                                                   |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ |
| [01_basics](D:/yan1/python learning/python basic/01_basics)  | 基础语法      | 输出、变量、数字、字符串、类型转换、输入、格式化、布尔值、赋值，共 9 个示例 |
| [02_containers](D:/yan1/python learning/python basic/02_containers) | 数据容器      | 列表、元组、字典、集合，以及切片、解包、复制，共 7 个示例    |
| [03_control_flow](D:/yan1/python learning/python basic/03_control_flow) | 控制执行流程  | `if` 判断、`for` 和 `while` 循环、跳出循环、推导式等，共 7 个示例 |
| [04_functions](D:/yan1/python learning/python basic/04_functions) | 函数          | 把操作写成函数、传入参数、返回结果，以及作用域、生成器等，共 7 个示例 |
| [05_files_errors](D:/yan1/python learning/python basic/05_files_errors) | 文件与异常    | 处理路径，读写文本、CSV、JSON，处理报错和记录日志，共 7 个示例 |
| [06_objects_modules](D:/yan1/python learning/python basic/06_objects_modules) | 对象与模块    | 类、继承、数据类、导入模块、类型标注、装饰器和属性，共 7 个示例 |
| [07_standard_library](D:/yan1/python learning/python basic/07_standard_library) | Python 标准库 | 日期、随机数、数学、统计计数、正则表达式、命令行参数、SQLite，共 7 个示例 |
| [08_mini_projects](D:/yan1/python learning/python basic/08_mini_projects) | 综合练习      | 文本统计、支出报表、JSON 待办事项，共 3 个独立示例           |

**这 8 个目录内部目前没有子文件夹。** 每个 `.py` 都是可以单独运行的代码文件；每个目录里的 `README.md` 是这一章的说明和输出参考。前面的数字用于排序。

[_practice_output](D:/yan1/python learning/python basic/_practice_output) 是**运行示例后产生的结果**，也包括我检查示例时生成的文件。它的子目录是：

```
D:\yan1\python learning\python basic\_practice_output\
├─ 01_paths\                 路径操作示例的结果
│  └─ notes\                 用来演示创建和查找子文件夹
│     └─ hello.txt           示例创建的文本文件
├─ 02_text_files\            文本读写示例的结果
│  └─ study_notes.txt        示例学习笔记
├─ 03_csv_files\             CSV 读写示例的结果
│  └─ scores.csv             示例成绩表
├─ 03_todo_json\             综合练习中待办事项的结果
│  └─ sample_tasks.json      示例任务列表
├─ 04_json_files\            JSON 读写示例的结果
│  └─ settings.json          示例配置数据
├─ 06_context_manager\       上下文管理示例的结果
│  └─ context_note.txt       用来观察文件打开与关闭的文本
└─ 07_logging\               日志示例的结果
   └─ study.log              程序记录的运行信息
```

这里的编号对应**脚本的文件名**，不代表章节号。例如，待办事项的结果来自第 08 章。目录前面的 `_` 只是命名习惯，没有特殊功能。这个输出目录已经被 `.gitignore` 忽略。

另外两个辅助目录比较简单：

| 目录                                                | 里面的内容          | 用途                                             |
| --------------------------------------------------- | ------------------- | ------------------------------------------------ |
| [docs](D:/yan1/python learning/python basic/docs)   | `语法速查.md`       | 忘记某种写法时，用它查找对应示例                 |
| [tools](D:/yan1/python learning/python basic/tools) | `check_examples.py` | 批量检查全部示例能否运行。平时逐个学习不用运行它 |

它们目前都没有子文件夹。

[.idea](D:/yan1/python learning/python basic/.idea) 是 **PyCharm 等 JetBrains 编辑器使用的项目配置目录**。它保存编辑器设置，例如项目结构、工作区偏好和版本控制配置。[JetBrains 官方说明](https://www.jetbrains.com/help/pycharm/setting-up-your-project.html)

它里面只有一个子文件夹：

- [inspectionProfiles](D:/yan1/python learning/python basic/.idea/inspectionProfiles)：保存代码检查规则，例如编辑器应该提示哪些警告。里面的两个 XML 文件分别保存检查配置和配置选择信息。

其余都是配置文件，例如 `modules.xml` 描述项目模块，`vcs.xml` 记录使用 Git，`workspace.xml` 保存工作区状态。**这些不是 Python 学习代码，运行示例不需要阅读它们。**

[.git](D:/yan1/python learning/python basic/.git) 是 **Git 管理版本所使用的内部目录**。它的主要子目录如下：

```
D:\yan1\python learning\python basic\.git\
├─ hooks\           存放 Git 操作前后可以触发的脚本
├─ info\            仓库的辅助信息，例如本地忽略规则
├─ objects\         存储文件内容、目录结构等版本数据
│  ├─ 两位编号目录\ 按对象编号分组存放数据，很多目录用途相同
│  ├─ info\         对象存储的辅助信息
│  └─ pack\         打包后的版本数据
└─ refs\            保存指向版本数据的引用
   ├─ heads\        本地分支的引用
   ├─ tags\         版本标签的引用
   └─ codex\        Codex 命名空间下的内部引用
      └─ turn-diffs\
         ├─ captures\
         └─ checkpoints\
```

`objects` 下面那些两位编号的文件夹，是 Git 根据数据标识自动分组使用的；不需要逐个学习。其他标准目录的含义见 [Git 官方目录说明](https://git-scm.com/docs/gitrepository-layout)。

`codex` 下面的 `turn-diffs`、`captures`、`checkpoints`，**从名称推测与每轮修改的捕获、对比检查点有关**，更深的长编号目录用于区分内部记录。官方文档确认 Codex 可以查看最近一轮修改，但没有在该说明中解释这些内部目录的具体格式，因此这部分用途是推断。[Codex 修改查看说明](https://learn.chatgpt.com/docs/code-review?surface=app)

这次发现这些引用，说明 `.git` 中确实包含 Codex 相关记录；但仍不能仅凭这些目录确定最初是谁初始化了仓库。

最后，项目根目录还有三个常用文件，**它们是文件，不是文件夹**：

| 文件                                                         | 作用                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| [README.md](D:/yan1/python learning/python basic/README.md)  | 整个项目的使用说明和学习目录                          |
| [LEARNING_CHECKLIST.md](D:/yan1/python learning/python basic/LEARNING_CHECKLIST.md) | 学习打卡表，学完后把 `[ ]` 改成 `[x]`                 |
| [.gitignore](D:/yan1/python learning/python basic/.gitignore) | 告诉 Git 忽略哪些文件，例如练习输出、缓存和编辑器配置 |