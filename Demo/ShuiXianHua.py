if __name__ == '__main__':
    """找出所有的水仙花数字"""
    for i in range(100, 1000):
        num = i
        a = num % 10
        num //= 10
        b = num % 10
        num //= 10
        c = num % 10
        num //= 10
        d = a * 100 + b * 10 + c
        # print("原数字:" + repr(i) + "新数字为:" + repr(d))
        if d == num:
            print(repr(num) + "是一个水仙花数字")

    print("运行完毕")
