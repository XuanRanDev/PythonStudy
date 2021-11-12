import os
import time

def main():
    content = "洛阳欢迎您为您开天辟地"
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()