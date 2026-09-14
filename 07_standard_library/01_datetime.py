"""datetime：表示日期时间、格式化、解析和计算时间差。

适用场景：处理日志时间、到期日期、任务日程。
示例使用固定日期，便于每次运行时对照输出。
"""

from datetime import date, datetime, timedelta, timezone


birthday = date(2000, 5, 20)
moment = datetime(2026, 9, 13, 14, 30)
print("1. 日期：", birthday)
print("2. 年、月、日：", moment.year, moment.month, moment.day)
print("3. 格式化：", moment.strftime("%Y-%m-%d %H:%M"))

parsed = datetime.strptime("2026-10-01", "%Y-%m-%d")
print("4. 字符串转日期：", parsed.date())
print("5. 七天以后：", (moment + timedelta(days=7)).date())
print("6. 距离国庆的天数：", (parsed.date() - moment.date()).days)

# 没有时区的 datetime 不会自动知道它属于哪个地区。
utc_moment = datetime(2026, 9, 13, 6, 30, tzinfo=timezone.utc)
china_time = utc_moment.astimezone(timezone(timedelta(hours=8)))
print("7. UTC 转为 UTC+8：", china_time.isoformat())
# 获取真实当前时间可用 datetime.now()；本示例不依赖当前日期。
# timedelta(days=30) 是 30 天，不代表任意月份的“一个月”。


# 小练习：解析两个 YYYY-MM-DD 字符串，计算它们相差多少天。
