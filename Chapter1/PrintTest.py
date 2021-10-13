a = 10
b = 6
print(a * b)

print(a if a >= b else b)


def Fileinit():
    f = open("E:/PycharmProjects/PythonStudy/FileTest/1.txt","a+")
    print("This is a file test program.",file =  f)
    f.close()


if __name__ == '__main__':
    Fileinit()
