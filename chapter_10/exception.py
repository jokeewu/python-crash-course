# coding=utf-8
# 异常

try:
    # r = 5 / 0
    r = 5 / ''
except ZeroDivisionError:
    print('zero')
except TypeError:
    print('type error')


msg = "I am w'jacky"
words = msg.split()
print(words)