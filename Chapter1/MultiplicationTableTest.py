def startMultipolicationTableTest():
    for i in range(0, 10):

        for j in range(1, i + 1):
            print(repr(j) + "*" + repr(i) + " = " + repr(i * j) + "\t", end='')

        print("\n")


if __name__ == '__main__':
    startMultipolicationTableTest()
