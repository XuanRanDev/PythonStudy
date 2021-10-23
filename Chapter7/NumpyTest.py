import numpy as np


def NumpyTest():
    """Numpy创建"""
    array = np.array(
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
    )
    print(array)


def zeroNumpyTest():
    zero_array = np.zeros([3, 4])
    print(zero_array)


def oneNumpyTest():
    one = np.ones([3, 2], dtype='int64')
    print(one)


def emptyNumpyTest():
    """
    如果设置为空的话，所产生的值由当前内存状态决定
    :return:
    """
    empty = np.empty([3, 6])
    print(empty)


if __name__ == '__main__':
    emptyNumpyTest()
    # oneNumpyTest()
    # zeroNumpyTest()
    # NumpyTest()
