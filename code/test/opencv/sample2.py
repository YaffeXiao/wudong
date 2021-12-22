
import cv2
import numpy as np
import time


def cv_show(_img, name="test"):
    cv2.namedWindow(name, 0)
    # cv2.resizeWindow(name,  720, 1200)
    # cv2.resizeWindow(name, _img.shape[0] / 4, _img.shape[1] / 4)
    cv2.resizeWindow(name, _img.shape[0], _img.shape[1])
    cv2.imshow(name, _img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


src_img = cv2.imread("1080/zhulou2.png")
img = cv2.imread("1080/zhulou2.png", 0)
# face1 = cv2.imread("1080/face1.png", 0)
face1 = cv2.imread("1080/p1.jpg", 0)

imgN = cv2.Canny(img, 50, 150)
face1N = cv2.Canny(face1, 20, 150)
# face1N = cv2.pyrDown(face1N)
# face1N = cv2.pyrDown(face1N)
# face1N = cv2.pyrDown(face1N)
imgN = cv2.pyrUp(imgN)
cv_show(face1N)
# cv_show(cv2.imread("1080/face1.png"))
res = cv2.matchTemplate(imgN, face1N, cv2.TM_CCOEFF_NORMED)
print(res.shape)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(cv2.minMaxLoc(res))

top_left = max_loc
bottom_right = (top_left[0] + face1.shape[0], top_left[1] + face1.shape[1])

cv2.rectangle(src_img, top_left, bottom_right, (255, 0, 0), 2)
# cv_show(src_img)


threshold = 0.8
print(res.shape)
loc = np.where(res >= threshold)
# print(loc)
# print("")
for pt in zip(*loc[::-1]):
    bottom_right = (pt[0] + int(face1.shape[0]/1), pt[1] + int(face1.shape[1]/1))
    cv2.rectangle(src_img, top_left, bottom_right, (0, 255, 0), 1)

cv_show(src_img)
