
import cv2
import os,sys
from Harris import *
from Sift import *

root_path = "E:/me/git/wudong/code/test/opencv/match_sample/datas"
img1_path = os.path.join(root_path, "p1.jpg")
img2_path = os.path.join(root_path, "zhulou2.png")
img1 = cv2.imread(img1_path)  # 查询图像
img2 = cv2.imread(img2_path)  # 训练图像


# harris_t(img1, img2)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2[400:])
sift_t(img1, img2[400:])



