

import win32api, win32con, win32gui

def DRAW_LINE(x1, y1, x2, y2):
    hwnd=win32gui.WindowFromPoint((x1,y1))
    hdc=win32gui.GetDC(hwnd)
    x1c,y1c=win32gui.ScreenToClient(hwnd,(x1,y1))
    x2c,y2c=win32gui.ScreenToClient(hwnd,(x2,y2))
    win32gui.MoveToEx(hdc,x1c,y1c)
    win32gui.LineTo(hdc,x2c,y2c)
    win32gui.ReleaseDC(hwnd,hdc)

x1 = 640
y1 = 400
x2 = 840
y2 = 600

DRAW_LINE(x1, y1, x2, y2)