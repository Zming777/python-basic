# True / False 表示真 / 假；None 表示没有值。
# 场景：判断条件是否满足，或者表示某项信息尚未填写。

score = 85
print(score >= 60)  # True
print(score == 100)  # False：== 比较值是否相等。
print(60 <= score < 90)  # True

has_ticket = True
is_open = False
print(has_ticket and is_open)  # False：两个条件都满足才是真。
print(has_ticket or is_open)  # True：至少一个条件满足就是真。
print(not is_open)  # True：not 取反。

nickname = None
print(nickname is None)  # True：判断 None 用 is None。
nickname = "Python 新手"
print(nickname is not None)  # True

print(bool(""))  # False：空字符串是假。
print(bool("False"))  # True：这只是一个非空字符串。

# 练习：判断年龄 20 是否在 18 到 60 岁之间。
