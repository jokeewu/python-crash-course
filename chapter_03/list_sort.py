#coding=utf-8
#列表排序

names = ["jacky", "jokee", "hokee"]
names.sort() # 影响原列表
print(names)

names.sort(reverse=True)
print(names)

print(sorted(names, reverse=True)) # 不影响原列表
print(names)