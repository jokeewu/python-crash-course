# coding=utf-8
# 函数
# 位置实参/关键字实参/默认值

def say(name, age, sex):
    print("hello " + name + ', old ' + str(age) + ', sex ' + sex)


# 位置实参 顺序很重要
say("jacky", 26, 'F')

# 关键字实参 顺序无关紧要
say(name="hokee1", age=27, sex="F")
say(age=27, sex="F", name="hokee2")
# say(name="hokee2", 28, sex="F")  Error

# 默认值
def display_message(type, level, msg="Empty"):
    print(type, level, msg)

display_message(level=1, type="error")

# 返回值
# 传递列表

'''
引用传递
def pass_list(names):
    del names[0]
    names.remove('hokee')

names = ['jacky', 'hokee']
pass_list(names)
pass_list(names[:]) # 防止原列表被修改
print(names)
'''

# 任意个实参
def muti_params(*params):
    print(params, type(params))

muti_params(1, 2, 3)

# 位置实参与任意数量实参
'''
def join_x(a, *b):
    pass
'''

# 使用任意数量的关键字实参 参考：8.5.3
def make_profile(name, age, **user_info):
    # user_info 将是一个字典形式
    print(user_info)
make_profile("jacky", 26, sex="F", address="SiChuan")





