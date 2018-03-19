# encoding=utf-8
# 类创建

# 编码问题

class Dog():
    """狗狗类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + ', ' + str(self.age))

    def roll_over(self):
        print(self.name + ' rolling')


class ZHDog(Dog):
    """中华田园犬"""

    def __init__(self, name, age):
        super().__init__(name, age)

    '''方法重写'''
    def roll_over(self):
        print(self.name + ' rolling, it is a ZH dog.')


dog_doudou = ZHDog(u"豆豆", 1)
dog_doudou.sit()
dog_doudou.roll_over()