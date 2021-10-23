import numpy as np


def Test():
    arr1 = np.array([[1, 2, 4], [2, 4, 5]])
    arr2 = np.ones([2, 3], dtype='int64')

    print("相加：", arr1 + arr2)
    print("相减：", arr1 - arr2)
    print("相乘:", arr1 * arr2)
    print("相除：", arr1 / arr2)
    print("元素相乘:", arr1 ** 2)


if __name__ == '__main__':
    Test()
