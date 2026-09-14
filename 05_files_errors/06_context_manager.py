"""上下文管理器：把准备资源和释放资源放在一起。
自定义 with 的行为时使用。打开本文件，点击运行即可。
"""

from contextlib import contextmanager
from pathlib import Path


@contextmanager
def managed_note(path):
    # 只覆盖本课自己的样例文件；打开失败会正常报错。
    file = path.open("w", encoding="utf-8")
    print("1. 打开文件")
    try:
        # yield 把文件交给下面 with ... as note 中的 note。
        yield file
    finally:
        # with 内发生异常，也会执行这里的清理。
        file.close()
        print("3. 关闭文件")


project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "_practice_output" / "06_context_manager"
output_dir.mkdir(parents=True, exist_ok=True)
note_path = output_dir / "context_note.txt"

try:
    with managed_note(note_path) as note:
        note.write("这是上下文管理器的固定样例。\n")
        print("2. 在 with 里面写入内容")
        raise ValueError("故意出错，看看文件是否仍会关闭")
except ValueError as error:
    print("4. 接到样例错误：", error)

print("文件已关闭：", note.closed)  # True
print("文件位置：", note_path)

# 日常只需打开文件时，直接使用 with path.open(...) 就够了。
# 小练习：注释掉 raise 那一行，看看“关闭文件”还会不会打印。
