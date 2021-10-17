import random


def CommonRandomTest():
    a = random.random()
    print(a)


def IntRandomTest():
    a = random.randint(1, 15)
    print(a)


def ZhongZiRandomTest():
    """种子随机数测试"""
    random.seed(1)
    a = random.randint(1, 10)
    print(a)
    random.seed(1)
    b = random.randint(1, 10)
    print(b)



if __name__ == '__main__':
    """随机数Random测试"""
    ZhongZiRandomTest()
    # IntRandomTest()
    # CommonRandomTest()
