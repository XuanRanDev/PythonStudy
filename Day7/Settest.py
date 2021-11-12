def BaseTest():
    """集合基本测试"""
    sets = {1, 3, 4, 3, 2}
    print(sets)
    print("Length :", len(sets))

    # 使用构造方法创建集合
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 4, 5))
    print(set2, set3)

    # 使用集合推导语法
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print(set4)


def AddElementTest():
    """向集合中添加元素"""
    set1 = {1, 2, 3}
    print(type(set1))
    set1.add(4)
    set1.add(5)
    print(set1)
    # Delete element
    set1.discard(5)
    print(set1)

    if 4 in set1:
        set1.remove(4)
    print(set1)
    set1.pop()
    print("Pop after:", set1)


if __name__ == '__main__':
    # BaseTest()
    AddElementTest()
