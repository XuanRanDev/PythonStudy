import pandas as pd


def SeriesBaseTest():
    """Series基本形式"""
    s = pd.Series(['a', 'b', 'c'])
    print(s)


def SeriesIndexTest():
    """Series支持多索引"""
    s = pd.Series(['a', 'b', 'c'], index=[100, 200, 100])
    print(s)


def SeriesFromDiect():
    """Series支持由字典转型而来"""
    dic = {'1' : 1 , '2' : 2, '3' : 3}
    s = pd.Series(dic)
    print(s)


if __name__ == '__main__':
    SeriesFromDiect()
    # SeriesIndexTest()
    # SeriesBaseTest()
