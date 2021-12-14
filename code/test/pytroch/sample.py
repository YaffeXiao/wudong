import os
import random
import sys
import numpy as np
from random import randint
from PIL import Image
from torchvision import transforms
import torchvision
sys.path.append("..")
# from code.common.ContVar import *


project_path = "E:\\me\\git\\wudong"

'''
https://www.cnblogs.com/ghgxj/p/14219097.html
'''
file_path = os.path.join(project_path, 'sample\\face\\face1.png')
print(file_path)
img = Image.open(file_path)
#灰度
transform = transforms.Grayscale()
img = transform(img)

#随机裁剪
size = randint(50, 100)
print(size)
transform = torchvision.transforms.RandomCrop(size)
img = transform(img)

color = size = randint(0, 255)
#扩展边缘
transform = transforms.Pad(30, color)
img = transform(img)

#重置大小
transform = transforms.Resize((100, 100))
img = transform(img)

#随机旋转
transform = transforms.RandomRotation(degrees=(45, 45), expand=True)
img = transform(img)
#水平翻转
transform = transforms.RandomHorizontalFlip(p=1)
img = transform(img)
#垂直翻转
torchvision.transforms.RandomVerticalFlip(p=0.5)
img = transform(img)

#彩色抖动
# transform = torchvision.transforms.ColorJitter(brightness=0, contrast=0, saturation=0, hue=0)


# 高斯模糊
# kernel_size：模糊半径。必须是奇数。
# sigma：正态分布的标准差。如果是浮点型，则固定；如果是二元组(min, max)，sigma在区间中随机选取一个值。
transform = torchvision.transforms.GaussianBlur(3, sigma=(0.1, 2.0))

# 仿射变换
'''
描述
汇总了旋转、平移、缩放、扭曲等图像变换方法，并且支持叠加。比如旋转的同时又进行平移或缩放等。

参数
degrees (sequence or float or int)：随机旋转的角度范围。和随机旋转的参数定义一致。设置为0表示不旋转。
translate (tuple, optional) ：水平和垂直平移的因子。如(a, b)，表示在img_width * a < dx < img_width * a范围内随机水平平移，在-img_height * b < dy < img_height * b范围内随机垂直平移。
scale (tuple, optional)：缩放因子。如(a, b)，表示在a <= scale <= b随机缩放。
shear (sequence or float or int, optional)：随机扭曲的角度范围。如(45, 90)，表示在45~90范围内随机选取一个角度进行与横轴平行的扭曲。
resample (int, optional) ：重采样。
fillcolor (tuple or int) ：填充色。默认为0，也就是黑色。支持三元组的RGB颜色。
'''
# transform = torchvision.transforms.RandomAffine(36, translate=None, scale=None, shear=None, resample=0, fillcolor=0)

img = transform(img)
Image._show(img)



img = Image.open('test.jpg')
# 随机旋转
transform_1 = transforms.RandomAffine(90)
img_1 = transform_1(img)
# 随机平移
transform_2 = transforms.RandomAffine(0, (0.1, 0))
img_2 = transform_2(img)
# 随机缩放
transform_3 = transforms.RandomAffine(0, None, (0.5, 2))
img_3 = transform_3(img)
# 随机扭曲
transform_4 = transforms.RandomAffine(0, None, None, (45, 90))
img_4 = transform_4(img)
