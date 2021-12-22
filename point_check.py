


from utils.WindowTool import WindowTool
from utils.WuDongTool import WuDongTool
from utils.ConVar import *
from core.SiftTool import SiftTool
import cv2

wd = WindowTool()

loc = wd.get_window_loc()


img = wd.get_screen_img()

img1 = img[int(loc[KHEIGHT] * 0.6):, int(loc[KWIDTH] * 0.5):]


# button = cv2.imread("E:/me/git/wudong/sample/button/power_button.jpg", 0)
# kp1, des1 = SiftTool.SIFT.detectAndCompute(button, None)
# power_button = [kp1, des1, button]
# b = power_button
# dst = SiftTool.get_dst_by_button(b[0], b[1], b[2], img)
#
# cv2.imshow("1", button)
# cv2.waitKey(0)
#
# cv2.imshow("1", img)
# cv2.waitKey(0)
# x = int(dst[0, 0, 0]) + 10
# y = int(dst[0, 0, 1]) + 10
# print(x, y)
#
# img1 = cv2.drawMarker(img,  x, y, (0, 0, 255), 0)
#
cv2.imshow("1", img1)
cv2.waitKey(0)
