import win32api, win32con, win32gui
import sys
import mss
import numpy as np


class WindowTool:
    HWND_TITLE = dict()

    def __init__(self, up_offset=230 - 185, wn="乌冬的旅店"):
        '''

        :param up_offset: 230 - 185
        :param wn:
        '''
        self.MONITOR_LOCATION = None
        self.up_offset = up_offset
        self.init_windows(wn)

    def get_all_hwnd(self, hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            self.HWND_TITLE.update({hwnd: win32gui.GetWindowText(hwnd)})

    def init_windows(self, wn):
        # 初始化窗口信息
        windows_id = -1
        win32gui.EnumWindows(self.get_all_hwnd, 0)
        for h, t in self.HWND_TITLE.items():
            if t is not "":
                print(h, t)
                if t.find(wn) != -1:
                    print(h)
                    windows_id = h
                    break
        if windows_id == -1:
            print("窗口信息初始化失败！！！")
            sys.exit(0)
        win_location = win32gui.GetWindowRect(windows_id)
        win_location = list(win_location)
        # win_location[0] += 280
        win_location[1] += self.up_offset
        # win_location[2] -= 100
        # win_location[3] -= 100

        self.MONITOR_LOCATION = {'top': win_location[1], 'left': win_location[0],
                                 'width': win_location[2] - win_location[0],
                                 'height': win_location[-1] - win_location[1]}

    def get_window_loc(self):
        return self.MONITOR_LOCATION

    def get_screen_img(self):
        # print(MONITOR_LOCATION)
        with mss.mss() as sct:
            img = np.array(sct.grab(self.MONITOR_LOCATION))
        return img
