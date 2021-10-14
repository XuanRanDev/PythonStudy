v = ["春眠不觉晓", "处处闻啼鸟", "夜来风雨声", "花落知多少"]


# 序列定义测试
def VerseTest2():
    print(v[0])
    print(v[1])
    print("遍历输出：-------------")

    for s in v:
        print(s)
    print("end ---------------")


def SliceTest():
    """序列切片测试"""
    # param 1 : start 2 : end 3 : step
    new_v = v[1: 3]
    print(new_v)

    print("复制整个序列测试-------")
    # 复制整个序列
    new_v_2 = v[:]
    print(new_v_2)
    print("复制整个序列测试end-------")


def ListAddListTest():
    """序列相加测试"""
    new_v = v + v
    print(new_v)


def ListElementCheckTest():
    ls = ["风萧萧兮易水寒", "壮士一去不复返"]
    for i in ls:
        if i == "水":
            print("发现了水")
    else:
        print("没有水")

    if "风萧萧兮易水寒" in ls:
        print("Find out")
    else:
        print("Not find")


def ListAppendTest():
    girls = ['杨超越']
    girls.append('')
    print(girls)


def ListExtendsTest():
    """List相加"""
    girls = ['杨超越']
    girls2 = ['']
    girls3 = girls + girls2
    print(girls3)


def ListInsertTest():
    """List插入测试"""
    girls = ['']
    girls.insert(0, 'XuanRan')
    print(girls)


def ListChangeTest():
    """List修改测试"""
    girls = ["A"]
    girls[0] = "AAA"
    print(girls)

    fruit = ["Apple", "香蕉", "Bear"]

    for i in range(len(fruit)):
        if fruit[i] == "香蕉":
            fruit[i] = "banana"
            break
    print(fruit)


def ListDeleteElementTest():
    fruit = ['Apple', 'Bear', 'Other', 'Cat', 'Dog']

    del fruit[0]
    print(fruit)
    fruit.remove(fruit[0])
    print(fruit)
    fruit.pop(0)
    print(fruit)



if __name__ == '__main__':
    ListDeleteElementTest()
    # ListChangeTest()
    # ListInsertTest()
    # ListExtendsTest()
    # ListAppendTest()
    # ListElementCheckTest()
    # SliceTest()
    # ListAddListTest()