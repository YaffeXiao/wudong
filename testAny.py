



from utils.WindowTool import WindowTool
from utils.MouseTool import MouseTool
from utils.ConVar import *
import time
import win32api
import win32con
import cv2
wx = WindowTool(up_offset=0, wn="微信")
wx_loc = wx.get_window_loc()
#
# cv2.imshow("wx", wx.get_screen_img())
# cv2.waitKey(0)
x = wx_loc[KWIDTH] * 0.09
y = wx_loc[KHEIGHT] * 0.08
MouseTool.click_obj(wx_loc, x, y)
win32api.keybd_event(87,0,0,0)
win32api.keybd_event(69,0,0,0)
win32api.keybd_event(78,0,0,0)
win32api.keybd_event(13,0,0,0)
time.sleep(0.5)
MouseTool.click_obj(wx_loc, x, wx_loc[KHEIGHT] * 0.2)

MouseTool.click_obj(wx_loc, wx_loc[KWIDTH] * 0.8, wx_loc[KHEIGHT] * 0.95)