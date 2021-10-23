import pandas as pd

def SeriesBaseTest():
    """Series基本形式"""
    s = pd.Series(['a', 'b' , 'c'])
    print(s)


if __name__ == '__main__':
    SeriesBaseTest()