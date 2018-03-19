# coding=utf-8
# 继承

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

'''
# python2.7
class ClassName(object|ParentClassName):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
'''

'''
# python3
class ClassName(ParentClassName):
    """docstring for ClassName"""
    def __init__(self, arg):
        super().__init__()
        self.arg = arg
'''
        
        