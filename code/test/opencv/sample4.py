
import cv2 as cv
import numpy as np



def canny(image):
    """canny边缘提取"""
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

    # image：要检测的图像,threshold1：阈值1（最小值）,threshold2：阈值2（最大值），使用此参数进行明显的边缘检测,
    # canny_output2 = cv.Canny(grad_x, grad_y, 30, 150)
    canny_output1 = cv.Canny(gray, 50, 150)  # 也可以直接传入gray

    return canny_output1


def contours(image):
    """轮廓查找"""
    binary = canny(image)
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        # 函数 cv2.drawContours() 可以被用来绘制轮廓。它可以根据你提供的边界点绘制任何形状。
        # 它的第一个参数是原始图像，第二个参数是轮廓，一个 Python 列表。
        # 第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设 置为 -1 时绘制所有轮廓）。
        # 接下来的参数是轮廓的颜色和厚度等。
        cv.drawContours(image, contours, i, (0, 0, 255), 1)  # 2为像素大小，-1时填充轮廓
        print(i)
    cv.imshow("detect contours", image)

def image_contour(image):
    """轮廓查找并描点"""
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 图像二值化
    print("threshold value: %s" % ret)  # 输出阈值
    # cv.imshow("binary image", binary)

    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)  # 用红色线条画出轮廓

        epsilon = 0.01 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        cv.drawContours(image, approx, -1, (255, 0, 0), 10)
    cv.imshow("contour_approx", image)

def image_rectangle(image):

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # gray = cv.Canny(gray, 50, 150)
    # cv.imshow('test', gray)
    # cv.waitKey(0)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 图像二值化
    print("threshold value: %s" % ret)  # 输出阈值
    # cv.imshow("binary image", binary)

    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        # print(cv.contourArea(contour))
        if cv.contourArea(contour) < 25 : continue
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(image, (x,y), (x+w, y+w), (255, 0, 0), 1)
    cv.imshow("contour_jx", image)

if __name__ == "__main__":
    img2 = cv.imread('1080/zhulou.png')
    cv.imshow("img2", img2)
    gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)


    kernel = np.ones((1, 1), np.uint8)
    img_t = cv.erode(binary, kernel, iterations=1)

    cv.imshow("img_t",img_t)
    cv.imshow("binary",binary)
    cv.waitKey(0)
    image_rectangle(img2[620:720])
    cv.waitKey(0)