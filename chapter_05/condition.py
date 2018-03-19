# coding=utf-8

age = 26

if age < 0 or age > 100:
    print("invalid age")
elif age < 20:
    print("small")
elif age >= 20 and age <=30:
    print("ok")
elif age > 30:
    print("pass")

#某项是否在列表中
nickNames = ["Jacky", "Hokee"]
if "Jacky" in nickNames:
    print("Hello Jacky")

# 检查列表是否为空
emptyList = []

if emptyList:
    print("Not Empty")
else:
    print("Empty")