"""JSON：保存字典和列表，再恢复为 Python 数据。
保存设置、交换接口数据时使用。打开本文件，点击运行即可。
"""

import json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "_practice_output" / "04_json_files"
output_dir.mkdir(parents=True, exist_ok=True)
json_path = output_dir / "settings.json"

settings = {"username": "小林", "daily_minutes": 30, "enabled": True}

# dumps 把字典变成字符串；ensure_ascii=False 让中文直接显示。
json_text = json.dumps(settings, ensure_ascii=False)
print("JSON 字符串：", json_text)  # True 在 JSON 中写成 true

# loads 把 JSON 字符串恢复为字典。
restored = json.loads(json_text)
print("读回用户名：", restored["username"])

# dump/load 操作文件，dumps/loads 操作字符串。
# w 只覆盖自己的固定样例；indent=2 让文件缩进更好读。
with json_path.open("w", encoding="utf-8") as file:
    json.dump(settings, file, ensure_ascii=False, indent=2)

with json_path.open("r", encoding="utf-8") as file:
    loaded_settings = json.load(file)

print("文件读回后与原字典相等：", loaded_settings == settings)
print("文件位置：", json_path)

# 小练习：将 daily_minutes 改成 45，再运行并打开样例 JSON 看看。
