# 赋值不会复制列表；浅复制只复制外层；深复制会复制内部列表。
# 场景：想修改一份数据，同时保留原来的内容。
import copy

original = ["苹果"]
alias = original
alias.append("香蕉")
print(original)  # ['苹果', '香蕉']：两个名字指向同一列表。

original = ["苹果"]
shallow = original.copy()
shallow.append("香蕉")
print(original)  # ['苹果']：外层列表已经独立。

original = [["苹果"], ["香蕉"]]
shallow = original.copy()
shallow[0].append("梨")
print(original)  # [['苹果', '梨'], ['香蕉']]：内部列表仍共用。
print(shallow[0] is original[0])  # True

original = [["苹果"], ["香蕉"]]
deep = copy.deepcopy(original)
deep[0].append("梨")
print(original)  # [['苹果'], ['香蕉']]：原来的内部列表不受影响。
print(deep)  # [['苹果', '梨'], ['香蕉']]
print(deep[0] is original[0])  # False

# 练习：在浅复制那段中给 shallow 添加 ["橘子"]，观察 original 的外层。
