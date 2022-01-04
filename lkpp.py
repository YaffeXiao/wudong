import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from utils.WindowTool import WindowTool
from utils.WuDongTool import WuDongTool
from utils.ConVar import *
from core.SiftTool import SiftTool
import cv2

wd = WindowTool(up_offset=30, wn="逍遥模拟器4")

loc = wd.get_window_loc()


img = wd.get_screen_img()

print(np.sum(img - (np.ones_like(img) * 255) ))
if(np.sum(img[300:500, 300:500][:,:, :3] != 250) == 0):
    print("white")
print(img.max())

img[300:500, 300:500][:,:, :3]