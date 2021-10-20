import json


def JSONTest():
    data = [
        {
            'a': 2,
            'b': 3,
            'c': 4,
        }
    ]

    json1 = json.dumps(data)
    print(json1)


def JSONTest2():
    """JSON Test 2"""
    data = [
        {
            'a': 2,
            'b': 3,
            'c': 4,
        }
    ]
    #  sort_key 表示字典序排序
    #  indent 表示缩进位数
    json1 = json.dumps(data, sort_keys=True, indent=3)
    print(json1)


if __name__ == '__main__':
    JSONTest2()
    # JSONTest()
