import random


def sortedTest():
    ls = []
    while len(ls) < 10:
        temp = random.randint(1, 20)
        if temp not in ls:
            ls.append(temp)

    print(sorted(ls))


def sortedTest2():
    """逆向排序"""
    ls = []
    while len(ls) < 10:
        temp = random.randint(1, 20)
        if temp not in ls:
            ls.append(temp)

    print(sorted(ls, reverse=True))


if __name__ == '__main__':
    # sortedTest()
    sortedTest2()

