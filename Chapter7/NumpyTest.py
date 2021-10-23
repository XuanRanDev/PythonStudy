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


if __name__ == '__main__':
    zeroNumpyTest()
    # NumpyTest()