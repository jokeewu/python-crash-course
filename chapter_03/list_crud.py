#coding=utf-8

# 列表操作

names = []

# names[0] = "jacky" # IndexError: list assignment index out of range
# 添加
names.append("jakcy")
names.append("jokee")
names.append("hokee")
names.append("hokee")
names.append("hokee")
# 插入
names.insert(0, "wu")
# 删除
del names[0]
last_nickname = names.pop()
first_nickname = names.pop(0) # 传递索引
names.remove("hokee") # 根据值删除元素

print(names)