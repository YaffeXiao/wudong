
import time
import cv2
from utils.WindowTool import WindowTool
from utils.MouseTool import MouseTool
import numpy as np
from utils.ConVar import *
from matplotlib import pyplot as plt

wd = WindowTool()


top_rate = 0.72
bottom_rate = 0.87

# print(wd.get_window_loc())

# cv2.imshow("copy", wd.get_screen_img())
# cv2.waitKey(0)
def screen(_fun):
    while True:
        screen_img = wd.get_screen_img()
        _screen_img = _fun(screen_img)
        cv2.imshow('copy', _screen_img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

def image_contour(image):
    """轮廓查找并描点"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  # 图像二值化
    print("threshold value: %s" % ret)  # 输出阈值
    # cv2.imshow("binary image", binary)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv2.drawContours(image, contours, i, (0, 0, 255), 2)  # 用红色线条画出轮廓

        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        cv2.drawContours(image, approx, -1, (255, 0, 0), 10)
    cv2.imshow("contour_approx", image)

def image_rectangle(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.Canny(gray, 50, 150)
    # cv2.imshow('test', gray)
    # cv2.waitKey(0)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  # 图像二值化
    print("threshold value: %s" % ret)  # 输出阈值
    # cv2.imshow("binary image", binary)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        # print(cv2.contourArea(contour))
        if cv2.contourArea(contour) < 40 : continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x,y), (x+w, y+w), (255, 0, 0), 1)
    # cv2.imshow("contour_jx", image)
    return image


def match(img1, img2):
    MIN_MATCH_COUNT = 10
    # img1 = cv2.imread('1080/p1.jpg', 0)  # 查询图像
    # img2 = cv2.imread('1080/zhulou2.png', 0)  # 训练图像



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
    point = kp2[good[0].queryIdx].pt
    return good
    # point = kp2[good[0].trainIdx].pt
    # cv2.drawMarker(img2, (int(point[0]), int(point[1])), (0, 0, 255), 0)
    cv2.imshow("1", img2)
    cv2.waitKey(0)
    # if len(good) > MIN_MATCH_COUNT:
    # src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    # dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    #
    # M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    # matchesMask = mask.ravel().tolist()
    # # 匹配点绘制为绿色，只绘制内置点
    # draw_params = dict(matchColor=(0, 255, 0),  # 绘制匹配点为绿色
    #                    singlePointColor=None,
    #                    matchesMask=matchesMask,  # 只绘制内置点
    #                    flags=2)
    #
    # img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
    #
    # plt.imshow(img3, 'gray')
    # plt.xticks([])
    # plt.yticks([])
    # plt.title("feature_match & homography res")
    # plt.show()

def do_some(img):
    matchesMask = match(p1, img[int(top_rate): int(bottom_rate)])
    print(matchesMask)
    return image_rectangle(img)





if __name__ == '__main__':
    p1 = cv2.imread("sample/p/1.jpg", 0)
    screen_img = cv2.imread("sample/test/pps.jpg")
    img_gray = cv2.cvtColor(screen_img, cv2.COLOR_RGB2GRAY)
    # cv2.imshow("1", img_gray)
    # cv2.waitKey(0)
    matchesMask = match(p1, img_gray)
    print(matchesMask)
