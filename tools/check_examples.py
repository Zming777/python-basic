"""维护工具：在独立进程中检查每个课程能否运行结束，无需第三方测试库。

学习时在 VS Code 中运行具体的 .py 文件；本工具仅供批量检查。
工作目录使用临时目录，验证文件路径不依赖“必须在项目根目录运行”。
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main():
    paths = sorted(ROOT.glob("[0-9][0-9]_*/[0-9][0-9]_*.py"))
    if not paths:
        print("没有找到课程文件。")
        return 1
    failures = []
    environment = os.environ.copy()
    environment["PYTHONIOENCODING"] = "utf-8"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"

    with tempfile.TemporaryDirectory(prefix="python_lessons_check_") as directory:
        for path in paths:
            relative = path.relative_to(ROOT).as_posix()
            # input 课使用真正的 input()；自动检查时替学习者提供样例姓名。
            sample_input = "小明\n" if relative == "01_basics/06_input.py" else ""
            try:
                result = subprocess.run(
                    [sys.executable, "-X", "utf8", str(path)],
                    cwd=directory,
                    env=environment,
                    input=sample_input,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf-8",
                    timeout=10,
                    check=False,
                )
            except subprocess.TimeoutExpired:
                failures.append((relative, "超时：检查是否等待输入或有无限循环"))
                print(f"FAIL {relative}")
                continue
            if result.returncode != 0:
                failures.append((relative, result.stdout + result.stderr))
                print(f"FAIL {relative}")
            elif not result.stdout.strip():
                failures.append((relative, "没有标准输出，检查示例是否执行了 print()"))
                print(f"FAIL {relative}")
            else:
                print(f"PASS {relative}")

    print(f"\n共 {len(paths)} 个示例，通过 {len(paths) - len(failures)} 个。")
    for relative, detail in failures:
        print(f"\n失败文件：{relative}\n{detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
