


from utils.WindowTool import WindowTool
from utils.WuDongTool import WuDongTool
from utils.MouseTool import MouseTool
import pyautogui
from utils.ConVar import *
from core.SiftTool import SiftTool
import cv2

wd = WindowTool(up_offset=36)
# wd = WindowTool(up_offset=30, wn="逍遥模拟器4")

loc = wd.get_window_loc()


img = wd.get_screen_img()

# img1 = img[int(loc[KHEIGHT] * 0.6):, int(loc[KWIDTH] * 0.5):]


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
img = cv2.imread("sample/test/img.png")
img1 = img[int(loc[KHEIGHT] * WuDongTool.AGREE_CLOSE_TOP):,int(loc[KWIDTH] * WuDongTool.AGREE_CLOSE_LEFT):]
# img1 = img[int(loc[KHEIGHT] * WuDongTool.PEOPLE_TOP_RATE):int(loc[KHEIGHT] * WuDongTool.PEOPLE_BOTTOM_RATE)]
# img1 = img[int(loc[KHEIGHT] * WuDongTool.AD_CLOSE_TOP):,int(loc[KWIDTH] * WuDongTool.AD_CLOSE_LEFT):]
# img1 = img[int(loc[KHEIGHT] * WuDongTool.INSTALL_CLOSE_TOP):,int(loc[KWIDTH] * WuDongTool.INSTALL_CLOSE_LEFT):]
# img1 = img[int(loc[KHEIGHT] * WuDongTool.SHOWERS_TOP):, int(loc[KWIDTH] * WuDongTool.SHOWERS_LEFT):]
# img1 = img[int(loc[KHEIGHT] *0.6):, int(loc[KWIDTH] * 0.6):]
# x = int(loc[KWIDTH] * WuDongTool.AD_CLOSE_LEFT)
# y = int(loc[KHEIGHT] * WuDongTool.AD_CLOSE_TOP)
# img1 = img[y:, x:]
# WuDongTool.close_ad(loc)
cv2.imshow("1", img1)
cv2.waitKey(0)
