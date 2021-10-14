def showStringSplieTest():
    s = "Hello"
    s2 = "World"

    print(s + s2)
    print(s * 3)
    print(s[0:4])

    print('e' in s)
    print('e' not in s2)


def showStringJoinMethodTest():
    s = "Hello"
    print("-".join(s))


if __name__ == '__main__':
    showStringJoinMethodTest()
    # showStringSplieTest()