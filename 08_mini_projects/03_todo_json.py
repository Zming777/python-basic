"""小项目：创建待办事项、完成任务，再用 JSON 保存和读回。

会用到：函数、列表、字典、循环、Path、JSON、异常。
何时用：给小工具保存数据，让下一次运行能重新读到它。
运行：python -X utf8 08_mini_projects/03_todo_json.py
这是固定样例演示，每次重建并覆盖本课样例，不是个人待办管理器。
"""

import json
from pathlib import Path


def add_task(tasks, title):
    """添加任务，使用当前最大编号加一作为新编号。"""
    title = title.strip()
    if not title:
        raise ValueError("任务标题不能为空")
    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": next_id, "title": title, "done": False})
    return next_id


def complete_task(tasks, task_id):
    """按编号修改任务；找不到编号就明确报错。"""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return
    raise ValueError("找不到编号为 {} 的任务".format(task_id))


def save_tasks(path, tasks):
    """只将调用者传入的样例任务列表写入指定演示文件。"""
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
        file.write("\n")


def load_tasks(path):
    """读取本程序刚刚生成的样例；格式出错时让异常正常报告。"""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def show_tasks(tasks):
    """按完成状态显示，并统计尚未完成的数量。"""
    for task in tasks:
        mark = "x" if task["done"] else " "
        print("[{}] {}. {}".format(mark, task["id"], task["title"]))
    remaining = sum(not task["done"] for task in tasks)
    print("待完成：{} / {}".format(remaining, len(tasks)))


def main():
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "_practice_output" / "03_todo_json"
    output_dir.mkdir(parents=True, exist_ok=True)
    todo_path = output_dir / "sample_tasks.json"

    print("=== 1. 在内存中创建三个样例任务 ===")
    tasks = []
    first_id = add_task(tasks, "独立运行一个列表示例")
    add_task(tasks, "改写一个函数练习")
    add_task(tasks, "理解 JSON 保存和读取")
    show_tasks(tasks)

    print("\n=== 2. 完成第一个任务并保存 ===")
    complete_task(tasks, first_id)
    # 为保证重复运行结果一致，此处覆盖自己的固定样例文件。
    save_tasks(todo_path, tasks)
    print("已保存到：", todo_path)

    print("\n=== 3. 从磁盘重新读回 ===")
    restored_tasks = load_tasks(todo_path)
    show_tasks(restored_tasks)
    print("读回内容与保存前一致：", restored_tasks == tasks)
    print("读回的是一个新列表：", restored_tasks is not tasks)


if __name__ == "__main__":
    main()

# 小练习：
# 1. 增加第四个任务，并将第二个任务也设为已完成。
# 2. 写一个只显示未完成任务的函数。
# 3. 给每项任务增加 priority 字段，保存后检查样例 JSON。
