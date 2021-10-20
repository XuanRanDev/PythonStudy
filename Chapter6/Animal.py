class Animal:

    def __init__(self, name):
        """
            init 是一个构造函数
            类的所有方法第一个参数必须为self
        """
        self.name = name

    def eat(self):
        print(self.name + "要吃东西啦")

    def sleep(self):
        print(self.name + "要睡觉喽")


cat = Animal("Cat")
print(cat.name)
cat.eat()
cat.sleep()
