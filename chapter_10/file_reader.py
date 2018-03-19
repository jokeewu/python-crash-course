# coding=utf-8
# 文件读取

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

print('===========================')

with open(file_name) as file_object:
    # 逐行读取
    for line in file_object:
        print(line)

print('===========================')

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # rstrip/lstrip

print(pi_string)