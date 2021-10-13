"""
For 循环测试

其中range函数param 1 ： 开始数字 2： 终止（包头不包围） 3：step 步长
"""

if __name__ == '__main__':
    sum = 0
    for i in range(1, 101, 2):
        sum += i

    print(sum)
