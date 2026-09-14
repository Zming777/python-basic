# 字典用“键: 值”保存数据，通过键找到对应的值。
# 场景：记录用户资料、商品信息或程序设置。

user = {"name": "小明", "age": 20}
print(user["name"])  # 小明

user["age"] = 21  # 已存在的键会更新值。
user["city"] = "杭州"  # 不存在的键会新增。
print(user)  # {'name': '小明', 'age': 21, 'city': '杭州'}

# get 可以给缺失的键提供默认值；直接用 [] 访问缺失键会报错。
print(user.get("email", "未填写"))  # 未填写
print("city" in user)  # True：in 检查键。

city = user.pop("city")
print(city)  # 杭州
print(user)  # {'name': '小明', 'age': 21}

# items() 每次给出一个键和对应的值。
for key, value in user.items():
    print(key, "→", value)

# 练习：用字典保存一本书的书名、作者和页数，再修改页数。
