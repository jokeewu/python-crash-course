# coding=utf-8
# 字典

# key为字符串时需用引号包裹

jacky = {
    "name": "Wu,Jacky", # name: "Wu,Jacky"  Error
    "age": 26,
    2: 1, # jacky[2]
    "2": 2 # jacky["2"]
}

# add
jacky["address"] = "SiChuan,ChengDu"
jacky["address_new"] = "SiChuan,ChengDu"

# update
jacky["age"] = 27

# delete
del jacky[2]
del jacky["2"]

# iterator
for key, value in jacky.items():
    print(key + ":" + str(value))

for key in sorted(jacky.keys()):
    print(key)

for value in set(jacky.values()):
    print(value)

print(jacky)









