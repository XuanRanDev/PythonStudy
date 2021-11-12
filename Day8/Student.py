class Student:
    """
    在Python中属性和方法只有两种修饰符，分别为公有（Public）和私有（Private）
    Python中的所有属性和方法默认都是public
    如果想让属性或方法为私有可在属性或方法前加上__
    """

    # __init__函数是一个特殊的方法，相当于Java的构造器
    # 用于在对象创建时自动绑定属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, courseName):
        print('%s 正在学习 %s' % (self.name, courseName))

    def watch_TV(self, TVName):
        if self.age <= 10:
            print("%d岁的孩子只能看熊出没" % self.age)
            return
        print("正在观看: %s" % TVName)


if __name__ == '__main__':
    stu1 = Student("A", 12)
    stu1.study("Python程序设计")
    stu1.watch_TV("保持通话")
    stu2 = Student("B", 1)
    stu2.study("数学")
    stu2.watch_TV("喜羊羊")