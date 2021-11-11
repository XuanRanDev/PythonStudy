if __name__ == '__main__':
    """99乘法表和格式化输出测试"""

    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d * %d = %d \t' % (i, j, i*j), end='')
        print()
