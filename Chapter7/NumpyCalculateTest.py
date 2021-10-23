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


def JuZhenJiSuanTest():
    """矩阵相关计算方法测试"""
    arr3 = np.array([[1, 2, 3], [4, 5, 6]])
    # axis=1代表每一行求和 =0代表每一列
    print("求矩阵一行和：" + repr(np.sum(arr3, axis=1)))
    print("求矩阵最大值:" + repr(np.max(arr3)))
    print("求矩阵最小值：" + repr(np.min(arr3)))
    print("求矩阵均值：" + repr(np.mean(arr3)))
    print("求矩阵最大值下标：" + repr(arr3.argmax()))
    print("求矩阵最小值下标:" + repr(arr3.argmin()))



if __name__ == '__main__':
    # JuZhenJiSuanTest()
    # JuZhenChengFaTest()
    # Test()
