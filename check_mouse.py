from pymouse import PyMouse

myMouse = PyMouse()
#获取当前的鼠标位置
nowP = myMouse.position()
print(nowP)
#鼠标移动到坐标(x,y)处
myMouse.move(-709, 1200)
#鼠标点击，x,y是坐标位置 button 1表示左键，2表示点击右键 n是点击次数，默认是1次，2表示双击
myMouse.click(-709, 1200,1,1)




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

import time
MouseTool.reset_window_center(loc)
pyautogui.mouseDown()
time.sleep(0.1)
pyautogui.dragRel(-300, 0, mouseDownUp=False)
time.sleep(0.2)
pyautogui.mouseUp()
cv2.imshow("1", img)
cv2.waitKey(0)
