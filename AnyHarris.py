


from screen_test.Harris import *
import os

root_path = "E:/me/git/wudong/test_data"
# img1_path = os.path.join(root_path, "button/power_button.jpg")
# img2_path = os.path.join(root_path, "power_test.jpg")
# img1 = cv2.imread(img1_path)  # 查询图像
# img2 = cv2.imread(img2_path)  # 训练图像
# sift_t(img1, img2)


img1_path = os.path.join(root_path, "ad/ad_name.jpg")
img2_path = os.path.join(root_path, "ad_test.png")
# img1 = cv2.imread(img1_path)  # 查询图像
# img2 = cv2.imread(img2_path)  # 训练图像
harris_t(img1_path)



 # -*- coding: utf-8 -*-
from pylab import *
from PIL import Image

from PCV.localdescriptors import harris
from PCV.tools.imtools import imresize

'''
https://blog.csdn.net/weixin_44037639/article/details/88628253
'''

"""
This is the Harris point matching example in Figure 2-2.
"""

# Figure 2-2上面的图
#im1 = array(Image.open("../data/crans_1_small.jpg").convert("L"))
#im2= array(Image.open("../data/crans_2_small.jpg").convert("L"))

# Figure 2-2下面的图
im1 = array(Image.open(r'C:\Users\dell\Desktop\作业\计算机视觉\尚大楼2.png').convert("L"))
im2 = array(Image.open(r'C:\Users\dell\Desktop\作业\计算机视觉\尚大楼3.png').convert("L"))

# resize加快匹配速度
im1 = imresize(im1, (im1.shape[1]//2, im1.shape[0]//2))
im2 = imresize(im2, (im2.shape[1]//2, im2.shape[0]//2))

wid = 5
harrisim = harris.compute_harris_response(im1, 5)
filtered_coords1 = harris.get_harris_points(harrisim, wid+1)
d1 = harris.get_descriptors(im1, filtered_coords1, wid)

harrisim = harris.compute_harris_response(im2, 5)
filtered_coords2 = harris.get_harris_points(harrisim, wid+1)
d2 = harris.get_descriptors(im2, filtered_coords2, wid)

print ('starting matching')
matches = harris.match_twosided(d1, d2)

figure()
gray()
harris.plot_matches(im1, im2, filtered_coords1, filtered_coords2, matches)
show()
