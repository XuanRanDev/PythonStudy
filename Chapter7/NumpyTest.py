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


def NumpyMethodTest():
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(array)

    # 输出数组维度
    print("数组维度为：",array.ndim)

    # 输出数组形状
    print("数组形状是" + repr(array.shape))

    # 输出数组元素个数
    print("数组元素个数为:"  + repr(array.size))

    # 输出数组元素类型
    print("数组元素类型为：" + repr(array.dtype))


def ChangeNumpyShapeTest():
    """数组形状改变测试"""
    array = np.arange(6)
    print(array)

    print("数组准备改变")
    array = array.reshape([2, 3])
    print(array)



if __name__ == '__main__':
    ChangeNumpyShapeTest()
    # NumpyMethodTest()
    # emptyNumpyTest()
    # oneNumpyTest()
    # zeroNumpyTest()
    # NumpyTest()
