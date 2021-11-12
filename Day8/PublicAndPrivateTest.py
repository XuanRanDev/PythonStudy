class PublicAndPrivateTest:
    """
    在Python中属性和方法只有两种修饰符，分别为公有（Public）和私有（Private）
    Python中的所有属性和方法默认都是public
    如果想让属性或方法为私有可在属性或方法前加上__
    """
    """
    But,Python并没有严格保证属性和方法的私密性，也就是说你也可以通过特殊方法访问到（如果你知道其Name)
    """

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")