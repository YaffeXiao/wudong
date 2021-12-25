import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from utils.WindowTool import WindowTool
from utils.WuDongTool import WuDongTool
from utils.ConVar import *
from core.SiftTool import SiftTool
import cv2

wd = WindowTool()

loc = wd.get_window_loc()


img = wd.get_screen_img()

root_path = "E:/me/git/wudong/sample"
img1_path = os.path.join(root_path, "task/heart_button.png")

img1 = cv2.imread(img1_path, 0)
# img2 = cv2.imread('star2.jpg', 0)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
contours1, hierarchy = cv2.findContours(thresh, 2, 1)
cnt_star = contours1[2] # 模版轮廓
contours2, hierarchy = cv2.findContours(thresh2, 2, 1)
min_ret = 999
min_id = 0
for i, cnt2 in enumerate(contours2):
    ret = cv2.matchShapes(cnt_star, cnt2, 1, 0.0) # ret越小，越相似
    if ret < min_ret:
        min_ret = ret
        min_id = i
        print(min_id, min_ret)
show_img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
cv2.drawContours(show_img, contours2, min_id, (0, 0, 255), -1)
plt.imshow(show_img)