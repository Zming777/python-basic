"""Path：拼接路径、获取文件名、检查文件是否存在。
需要定位文件时使用。打开本文件，点击运行即可。
"""

from pathlib import Path

# __file__ 是当前脚本的位置，从哪里运行都能找到项目根目录。
project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "_practice_output" / "01_paths"

# / 用来拼接路径；mkdir 创建目录，已经存在也不报错。
sample_dir = output_dir / "notes"
sample_dir.mkdir(parents=True, exist_ok=True)
sample_file = sample_dir / "hello.txt"

# 只覆盖本课自己的固定样例，每次运行都得到相同内容。
sample_file.write_text("你好，pathlib！\n", encoding="utf-8")

print("文件名：", sample_file.name)          # hello.txt
print("不含扩展名：", sample_file.stem)      # hello
print("扩展名：", sample_file.suffix)        # .txt
print("文件存在：", sample_file.exists())    # True
print("完整位置：", sample_file)

# with_suffix 只得到一个新路径，不会真的重命名文件。
print("换个扩展名：", sample_file.with_suffix(".md").name)

# 小练习：把 hello.txt 改成 study.txt，再运行观察上面的结果。
