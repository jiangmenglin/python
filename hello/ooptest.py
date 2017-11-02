#!/usr/bin/python3

class MyClass:
    i = 123456
    def f(self):
        print('Hello world!')

#实例化一个对象
x = MyClass()
print(x.i)
x.f()

class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart
y = Complex(3.0, 4.5)
print('带有__init__函数的类')
print(y.r, y.i)

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
print('************************')
t.prt()

class People:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speaker(self):
        print("%s说：我%d岁了。"%(self.name, self.age))
p = People('李四', 12, 34)
print('*************************')
p.speaker()

print('---------练习类的继承-------')
class Student(People):
    grad = ''
    def __init__(self, name, age, weight, grad):
        People.__init__(self, name, age, weight)
        self.grad = grad
    def speaker(self):
        print('%s说：我%d岁了，我读%s年级。'%(self.name, self.age, self.grad))
s = Student('张三', 8, 23, 3)
s.speaker()

