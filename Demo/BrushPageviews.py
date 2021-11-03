import requests
import time


def start():
    url = "https://blog.xuanran.work/"

    heards = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    for i in range(100):
        body = requests.get(url, heards)
        print(body.text)
        print("已访问" + repr(i))
        i = i + 1


if __name__ == '__main__':
    start()
