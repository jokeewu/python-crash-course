# coding=utf-8
# 从终端输入

# python3 
#   input()
# python2.7 
#   raw_input()
#   input() 输入会当作代码执行

full_name = input("What's your name?\n")
print("My name is " + full_name)

age = input("How old are you?\n")
print(age + ' old')

if int(age) > 18:
    print("yeah")


