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


if __name__ == '__main__':
    # SliceTest()
    ListAddListTest()