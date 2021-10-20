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

    """参数二为如果找不到数据，返回的默认值"""
    print(dict1.get('D', 200))


def DictDelElementTest():
    """字典元素删除测试"""
    dict1 = {
        'A': 19,
        'B': 20,
        'C': 23,
    }
    print('Dict delete before:', dict1)
    del dict1['A']
    print('Dict delete after:', dict1)

    print('Dict prepare pop before', dict1)
    r = dict1.pop('A')  # have any issue.
    print(r)
    print(dict1)



if __name__ == '__main__':
    DictDelElementTest()
    # DictGetData()
    # DictKeyandValueTest()
    # DictValueTest()
    # DictKeySetTest()
    # DictItemTest()
    # DictChangeTest()
    # ListToDictTest()
    # Dict1Test()
