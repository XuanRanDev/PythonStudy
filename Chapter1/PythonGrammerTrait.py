# coding = utf-8

'''
    Created By XuanRan on 2021/10/13
'''

height = float(input("请输入你的身高"))
weight = float(input("请输入你的体重"))

bmi = weight / (height * height)

print("你的BMI指数为：" + str(bmi))

if bmi < 18.5:
    print("你的体重太轻")
if 18.5 <= bmi < 24.9:
    print("体重正常")
if 25 < bmi <= 29.9:
    print("肥胖")
if bmi >= 30:
    print("肥胖")

#   程序结束运行
