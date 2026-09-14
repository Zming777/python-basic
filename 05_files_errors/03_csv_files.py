"""CSV：把字典列表保存成表格，再读回来。
交换简单表格数据时使用。打开本文件，点击运行即可。
"""

import csv
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "_practice_output" / "03_csv_files"
output_dir.mkdir(parents=True, exist_ok=True)
csv_path = output_dir / "scores.csv"

students = [
    {"姓名": "小林", "分数": 86},
    {"姓名": "小周", "分数": 92},
]

# w 只覆盖自己的样例；newline="" 避免 Windows 多出空白行。
# utf-8-sig 带编码标记，方便常见表格软件识别中文。
with csv_path.open("w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["姓名", "分数"])
    writer.writeheader()        # 写表头
    writer.writerows(students)  # 写每一行数据

with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
    records = list(csv.DictReader(file))

# CSV 读到的值都是字符串，计算前要转换成数字。
for record in records:
    score = int(record["分数"])
    print(record["姓名"], "原分数：", score, "加 5 分后：", score + 5)

print("表格位置：", csv_path)

# 小练习：给 students 增加一名学生，再运行查看输出和样例表格。
