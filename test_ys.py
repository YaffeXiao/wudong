





from utils.MouseTool import MouseTool
from utils.WindowTool import WindowTool
from utils.WuDongTool import WuDongTool
import cv2
import pyautogui
from utils.ConVar import *
wt = WindowTool()
loc = wt.get_window_loc()
img = wt.get_screen_img()
# img2 = img[int(loc[KHEIGHT] * WuDongTool.SHOWERS_TOP):,
#        int(loc[KWIDTH] * WuDongTool.SHOWERS_LEFT):]

# img2 = img[int(loc[KHEIGHT] * WuDongTool.SHOWERS_3_TOP):,
       # int(loc[KWIDTH] * WuDongTool.SHOWERS_3_LEFT):]
img2 = img[int(loc[KHEIGHT] * WuDongTool.SPACE_TOP):,
       int(loc[KWIDTH] * WuDongTool.SPACE_LEFT):]
cv2.imshow("1", img2)
cv2.waitKey(0)
#click point : {-816, 89}  clicks: 1,  interval: 0.250000
# print(loc[KLEFT] + int(loc[KWIDTH] * WuDongTool.RESTAURANT_1_LEFT))
# print(loc[KTOP] + int(loc[KHEIGHT] * WuDongTool.RESTAURANT_1_TOP))
# pyautogui.moveTo(loc[KLEFT] + int(loc[KWIDTH] * WuDongTool.RESTAURANT_1_LEFT),
#                  loc[KTOP] + int(loc[KHEIGHT] * WuDongTool.RESTAURANT_1_TOP))


