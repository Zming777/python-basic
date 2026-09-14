"""logging：按严重程度记录程序运行信息。
排查程序问题时使用。打开本文件，点击运行即可。
"""

import logging
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "_practice_output" / "07_logging"
output_dir.mkdir(parents=True, exist_ok=True)
log_path = output_dir / "study.log"

logger = logging.getLogger("python_learning.logging_lesson")
logger.setLevel(logging.INFO)  # 记录 INFO 及以上级别，过滤 DEBUG。
logger.propagate = False      # 使用本课自己的输出设置。

# with 负责关闭文件；w 每次只覆盖自己的固定样例日志。
with log_path.open("w", encoding="utf-8") as log_file:
    handler = logging.StreamHandler(log_file)
    handler.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))
    logger.addHandler(handler)
    try:
        logger.debug("调试细节：当前不会记下来。")
        logger.info("开始学习 Python。")
        logger.warning("这是一条提醒。")
        logger.error("这是一条样例错误消息。")
    finally:
        # 移除本次 handler，避免在同一进程重复执行时重复记录。
        logger.removeHandler(handler)
        handler.close()

# 读出刚写好的日志，点击运行就能在终端看到结果。
print(log_path.read_text(encoding="utf-8"), end="")
print("日志位置：", log_path)

# 级别顺序：DEBUG < INFO < WARNING < ERROR < CRITICAL。
# logger.error 只记录消息，不会自动抛出异常或结束程序。
# 小练习：把 INFO 改为 DEBUG，再运行找出新增的一条日志。
