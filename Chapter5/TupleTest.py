import random
def addNewTuple():
    # 声明一个元组
    tuple1 = ("1", "2", "3", "4")
    print(tuple1)
    print(type(tuple1))


def HasATupleTest():
    # 当Tuple只有一个元素时，需要加上逗号
    tuple1 = ("aaa")
    print(type(tuple1))
    tuple2 = ("aa", )
    print(type(tuple2))


def ChangeTupleTest():
    # 元组内容是不能改变的，所以不能添加数据，需要用另一种方法
    ls = []
    tu = ()

    for i in range(1,20,2):
        if i not in ls:
            ls.append(random.randint(1, 50))

    # 使用类型转换
    tu = tuple(ls)

    print(tu)

    print(type(tu))


def TupleShowElementTest():
    # 元组数据获取示例
    tu = ("a", "b", "c", "d")
    print(tu[1:2])
    print(tu[::1])


def TupleElementChangedTest():
    v = ("a", "c")
    print(v * 3)
    print(("A", "Q") * 4)


def TupleMethodTest():
    """元组相关方法测试"""
    f = ()
    v = []

    for i in range(10):
        if i not in v:
            v.append(random.randint(10, 20))
    f = tuple(v)
    print("最大值" + str(max(f)))
    print("最小值" + repr(min(f)))
    print("和" + str(sum(f)))
    print(len(f))

    # 统计元组中10的个数
    print("元组中10的个数为:" + str(f.count(10)))

    print("元组中有10吗：" + str(10 in f ))




if __name__ == '__main__':
    """元组Test"""
    TupleMethodTest()
    # TupleElementChangedTest()
    # TupleShowElementTest()
    # ChangeTupleTest()
    # HasATupleTest()
    # addNewTuple()
