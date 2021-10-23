from PIL import Image


img = Image.open("E:\PycharmProjects\PythonStudy\FileTest\lk2.png")


def PILBaseTest():
    # 调用系统去显示图像（仅限Windows)
    # img.show()
    # plt.imshow(img)
    # plt.show(img)

    # 获取图像通道（RGB and RGBA)
    img_mode = img.mode
    print(img_mode)

    width, height = img.size
    print(width, height)


def PLPFanZhuanTest():
    """图像反转测试"""
    img_rotate = img.rotate(45)
    img_rotate.show()


def PILCropTest():
    """PIL图像裁剪测试"""
    # TODO 测试未通过
    # 参数：左上角x 左上角y 右下角x 右下角y
    img_r = img.crop((900, 500, 600, 366))
    img_r.show()


def PILResizeTest():
    """图像缩放测试"""
    widght,height = img.size
    img2 = img.resize(((int(widght * 0.5)),(int(height*0.5))), 0)
    img2.show()
    img2.save("E:\PycharmProjects\PythonStudy\FileTest\lk2_resize.png")


def PILTransposeTest():
    """图像反转测试"""
    # 实现图像左右反转
    img_tr1 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_tr1.show()

    # 实现图像上下反转
    img_tr2 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_tr2.show()



if __name__ == '__main__':
    # PILTransposeTest()
    # PILResizeTest()
    # PILCropTest()
    # PLPFanZhuanTest()
    # PILBaseTest()