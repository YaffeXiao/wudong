from utils.WuDongTool import WuDongTool
from utils.WindowTool import WindowTool
from utils.MouseTool import MouseTool
import pyautogui
from utils.ConVar import *
import time


loc = WindowTool().get_window_loc()


# MouseTool.reset_window_center(loc)
# pyautogui.scroll(100)
# i =0
# while i < 3:
#     MouseTool.dragRel(300, 0)
#     MouseTool.reset_window_center(loc)
#     time.sleep(1)
#     i += 1
# j = 0
# while j < 3:
#     MouseTool.dragRel(0, -300)
#     MouseTool.reset_window_center(loc)
#     time.sleep(1)
#     j += 1

# MouseTool.reset_window_center(loc)
# MouseTool.dragRel(-int(loc[KWIDTH]/2), 0)
# WuDongTool.rest_screen_main_building(loc)

WuDongTool.click_cqg(loc)