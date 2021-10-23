import numpy as np


def Test():
    arr1 = np.array([[1, 2, 4], [2, 4, 5]])
    arr2 = np.ones([2, 3], dtype='int64')

    print("相加：", arr1 + arr2)
    print("相减：", arr1 - arr2)
    print("相乘:", arr1 * arr2)
    print("相除：", arr1 / arr2)
    print("元素相乘:", arr1 ** 2)


def JuZhenChengFaTest():
    """矩阵乘法测试"""

    arr3 = np.array([[1, 2, 3], [4, 5, 6]])
    arr4 = np.ones([3, 2], dtype='int64')

    print(arr3)
    print(arr4)
    print("矩阵乘法运算：")
    print(arr3.dot(arr4))


if __name__ == '__main__':
    JuZhenChengFaTest()
    # Test()
