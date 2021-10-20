def Dict1Test():
    dict1 = {}
    dict2 = {'name': 'XuanRan', 'age': 19, 'sex': '男'}
    print(dict2['name'])


def ListToDictTest():
    """TODO"""
    """将List转成字典，前提是List中元素是成对出现的"""


def DictChangeTest():
    """字典修改测试"""
    dict1 = {}
    dict1['name'] = 'XuanRan'
    dict1['age'] = 19
    print(dict1)
    dict1['age'] = 15
    print(dict1['age'])


def DictItemTest():
    """Dictionary Item Method test"""
    dict1 = {'name': 'XuanRan', 'age': 19}
    print(dict1.items())


def DictKeySetTest():
    """Dict Key method test"""
    dict1 = {'name': 'XuanRan', 'age': 19}
    print(dict1.keys())


def DictValueTest():
    """Dict value method test"""
    dict1 = {
        'name': 'XuanRan',
        'age': 19,
        'sex': '男'
    }

    print(dict1.values())


def DictKeyandValueTest():
    """Dict key and value test"""
    dict1 = {
        'A': 166,
        'B': 133,
        'C': 242
    }

    for key, value in dict1.items():
        if value >= 160:
            print(key)

    print("All value is :")
    values = dict1.values()
    print(values)

    heights = sum(dict1.values())
    print('总身高为：' + repr(heights))

    avg = heights/dict1.__len__()
    print("avg is " + repr(avg))


def DictGetData():
    """Dict get data test"""
    dict1 = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    print(dict1.get('A'))


if __name__ == '__main__':
    DictGetData()
    # DictKeyandValueTest()
    # DictValueTest()
    # DictKeySetTest()
    # DictItemTest()
    # DictChangeTest()
    # ListToDictTest()
    # Dict1Test()