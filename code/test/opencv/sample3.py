# 在图像中找到SIFT特征并应用比率测试来找到最佳匹配。

import cv2
import numpy as np
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10
#
# img1 = cv2.imread('images/box.png', 0)  # 查询图像
# img2 = cv2.imread('images/box_in_scene.png', 0)  # 训练图像

img1 = cv2.imread('1080/face1.png', 0)  # 查询图像
img2 = cv2.imread('1080/zhulou2.png', 0)  # 训练图像
# 初始化SIFT检测器
sift = cv2.xfeatures2d.SIFT_create()

# 使用SIFT检测器寻找关键点和描述符
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

# 根据Lowe比率测试存储所有良好匹配项
good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)

if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()

    h, w = img1.shape
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)
    img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
else:
    print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
    matchesMask = None

# 匹配点绘制为绿色，只绘制内置点
draw_params = dict(matchColor=(0, 255, 0),  # 绘制匹配点为绿色
                   singlePointColor=None,
                   matchesMask=matchesMask,  # 只绘制内置点
                   flags=2)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

plt.imshow(img3, 'gray')
plt.xticks([])
plt.yticks([])
plt.title("feature_match & homography res")
plt.show()
