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
    one = np.ones([3,2],dtype='int64')
    print(one)


if __name__ == '__main__':
    oneNumpyTest()
    # zeroNumpyTest()
    # NumpyTest()