if __name__ == '__main__':
    age = int(input("请输入你的年龄：\n"))

    if  age < 18 :
        print('你还没有成年')
    elif age == 18:
        print("你刚好成年")
    elif age == 19:
        print("你成年一年了！")
    else:
        print("你已经不是小孩子了！")


