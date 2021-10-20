class Person:

    def __init__(self, name):
        self.name = name;
        print('调用构造方法')

    def eat(self):
        print('调用父类方法')


class Student(Person):

    def __init__(self):
        print('调用子类构造方法')

    def study(self):
        print('调用子类方法')


s = Student()
s.study()
s.eat()
