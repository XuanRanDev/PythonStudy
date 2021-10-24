import matplotlib.pyplot as plt
import numpy as np

def MatplotlibBaseTest():
    x = np.linspace(-1,1,50)
    y = x * 2 + 1
    plt.plot(x, y)
    plt.show()


def FigureTest():
    """Figure画布测试"""
    x = np.linspace(-1, 1, 50)
    y1 = x * 2 + 1
    y2 = x ** 2
    plt.figure()
    plt.plot(x,y1)
    plt.show()
    # 设置指定画布大小
    plt.figure(figsize=(7,8))
    plt.plot(x,y2)
    plt.show()



if __name__ == '__main__':
    """Matplotlib绘图测试"""
    FigureTest()
    # MatplotlibBaseTest()