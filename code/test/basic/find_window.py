

import win32api, win32con, win32gui
import sys
import mss
import numpy as np



HWND_TITLE = dict()
MONITOR_LOCATION = None
WINDOW_NAME = "乌冬的旅店"

def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        HWND_TITLE.update({hwnd: win32gui.GetWindowText(hwnd)})

def init_windows():
    # 初始化窗口信息
    windows_id = -1
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in HWND_TITLE.items():
        if t is not "":
            print(h, t)
            if t.find(WINDOW_NAME) != -1:
                print(h)
                windows_id = h
                break
    if windows_id == -1:
        print("窗口信息初始化失败！！！")
        sys.exit(0)
    win_location = win32gui.GetWindowRect(windows_id)
    win_location = list(win_location)
    win_location[0] += 280
    win_location[1] += 190
    win_location[2] -= 100
    win_location[3] -= 100

    global MONITOR_LOCATION
    MONITOR_LOCATION = {'top': win_location[1], 'left': win_location[0], 'width': win_location[2] - win_location[0],
               'height': win_location[-1] - win_location[1]}


def get_screen_img():
    # print(MONITOR_LOCATION)
    with mss.mss() as sct:
        img = np.array(sct.grab(MONITOR_LOCATION))
    return img

if __name__ == "__main__":
    init_windows()
    get_screen_img()