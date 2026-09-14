"""文本文件：w 覆盖、a 追加、r 读取。
保存笔记、读取配置时使用。打开本文件，点击运行即可。
"""

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "_practice_output" / "02_text_files"
output_dir.mkdir(parents=True, exist_ok=True)
note_path = output_dir / "study_notes.txt"

# with 会自动关闭文件；指定 UTF-8，保证中文读写编码一致。
# w 每次覆盖自己的固定样例，重复运行不会越写越长。
with note_path.open("w", encoding="utf-8") as file:
    file.write("第一天：学习变量\n")
    file.write("第二天：学习列表\n")

# a 不清空文件，而是把内容追加到末尾。
with note_path.open("a", encoding="utf-8") as file:
    file.write("第三天：学习文件操作\n")

# r 读取文件，for 每次取出一行。
with note_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        # 行尾已经有换行符，去掉它以免 print 再多换一行。
        clean_line = line.rstrip("\n")
        print(f"第 {line_number} 行：{clean_line}")

print("文件位置：", note_path)

# 小练习：在 a 模式的 with 里面再追加一句话，运行后看看结果。
