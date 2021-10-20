class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + "要吃东西啦")

    def sleep(self):
        print(self.name + "要睡觉喽")


cat = Animal("Cat")
print(cat.name)
cat.eat()
cat.sleep()
