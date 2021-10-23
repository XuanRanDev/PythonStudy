from PIL import Image
import matplotlib.pyplot as plt

def PILBaseTest():
    img = Image.open("E:\PycharmProjects\PythonStudy\FileTest\lk2.png")
    # 调用系统去显示图像（仅限Windows)
    # img.show()
    # plt.imshow(img)
    # plt.show(img)

    # 获取图像通道（RGB and RGBA)
    img_mode = img.mode
    print(img_mode)

    width, height = img.size
    print(width, height)



if __name__ == '__main__':
    PILBaseTest()