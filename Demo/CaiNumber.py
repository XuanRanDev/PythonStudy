import random

if __name__ == '__main__':
    ran = random.randint(1, 10)
    count = 1
    x = int(input("请输入一个数字\n"))
    if x != ran:
        while x != ran:
            if x > ran:
                print("太大了，请小一点")
            if x < ran:
                print("太小了，请大一点")
            count += 1
            x = int(input("请重新输入\n"))

    print("恭喜你，答对了。共耗 :" + repr(count) + "次")