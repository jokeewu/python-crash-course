# coding=utf-8
# 列表遍历

nicknames = ["jacky", "jokee", "hokee"]

for nickname in nicknames:
  print(nickname)

# xrange比range性能好，xrange返回一个生成器，range返回一个list对象
for x in xrange(1,10):
  print(x)

nums = range(1, 5) # [1, 5)
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))