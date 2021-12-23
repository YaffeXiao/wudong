
from utils.ConVar import *
import pyautogui


class MouseTool:

    @staticmethod
    def get_relative_point(loc, left_rate, top_rate):
        x = loc[KLEFT] + int(loc[KWIDTH] * left_rate)
        y = loc[KTOP] + int(loc[KHEIGHT] * top_rate)
        return x, y

    @staticmethod
    def click_rate_window(loc, left_rate, top_rate, clicks=1, interval=0.25):
        x, y = MouseTool.get_relative_point(loc, left_rate, top_rate)
        print("click point : {%d, %d}  clicks: %d,  interval: %f" % (x, y, clicks, interval))
        MouseTool._click(x, y, clicks, interval)

    @staticmethod
    def click_obj(loc, obj_x, obj_y, clicks=1, interval=0.25):
        x = loc[KLEFT] + obj_x
        y = loc[KTOP] + obj_y
        print("click obj : {%d, %d}  clicks: %d,  interval: %f" % (x, y, clicks, interval))
        if x <= loc[KLEFT] or x >= loc[KLEFT] + loc[KWIDTH] or y <= loc[KTOP] or y >= loc[KTOP] + loc[KHEIGHT]:
            print("click point is not inner window")
            return
        MouseTool._click(x, y, clicks, interval)

    @staticmethod
    def reset_window_center(loc):
        pyautogui.moveTo(loc[KLEFT] + int(loc[KWIDTH] / 2), loc[KTOP] + int(loc[KHEIGHT] / 2))

    @staticmethod
    def drag_rel(x, y):
        pyautogui.mouseDown()
        pyautogui.dragRel(x, y, mouseDownUp=False)
        pyautogui.mouseUp()

    @staticmethod
    def _move(x, y):
        pyautogui.moveTo(x, y)

    @staticmethod
    def _click(x=None, y=None, clicks=1, interval=0.25):
        print("click point : {%d, %d}  clicks: %d,  interval: %f" % (x, y, clicks, interval))
        pyautogui.click(x, y, clicks, interval)


