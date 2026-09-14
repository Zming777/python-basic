"""异常：尝试执行代码，遇到预期错误时给出反馈。
处理无效输入时使用。打开本文件，点击运行即可。
"""

# 三份固定样例：正常数字、无法转换的文字、不符合规则的数字。
samples = ["18", "十八", "-3"]

for text in samples:
    try:
        age = int(text)
        # raise 表示主动报错，本例约定年龄不能小于 0。
        if age < 0:
            raise ValueError("年龄不能为负数")
    except ValueError as error:
        # 只捕获自己知道如何处理的异常类型。
        print(f"{text!r} 转换失败：{error}")
    else:
        # try 没有抛出异常，才进入 else。
        print(f"{text!r} 转换成功，年龄是 {age}")
    finally:
        # 成功和失败都会执行，常用于清理资源。
        print("这一条处理结束。")

# 不要用 except: pass 隐藏所有错误，否则问题发生了也看不出来。
# 小练习：把 samples 改成 ["20", "18.5", "0"]，先猜结果再运行。
