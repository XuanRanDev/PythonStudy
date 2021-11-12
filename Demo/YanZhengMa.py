import random

def generate_code(len=4):
    all_char = ""
    for i in range(48, 58):
        all_char += chr(i)
    for i in range(65, 91):
        all_char += chr(i)
    for i in range(97, 123):
        all_char += chr(i)
    print(all_char)

    res = ""
    for i in range(1, len+1):
        ran = random.randint(0, 26 + 26 + 9)
        res += all_char[ran]

    return res


if __name__ == '__main__':
    """随机生成指定长度的验证码"""
    print(generate_code(len=4))
