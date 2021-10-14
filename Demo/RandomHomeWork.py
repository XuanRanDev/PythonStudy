import random

if __name__ == '__main__':
    ls = []

    while len(ls) < 10:
        temp = random.randint(1, 20)
        if temp not in ls:
            ls.append(temp)

    print(sorted(ls))
