def main(filename):
    if '.' not in filename:
        return "null"
    pos = filename.rfind('.')  # 从右边开始查找
    return filename[pos + 1:]


if __name__ == '__main__':
    """返回给定文件名的文件类型"""
    print(main("XuanRan.mp3"))