

from utils.WindowTool import WindowTool
from utils.ConVar import *
from core.SiftTool import SiftTool
from screen_test.AnySift import *
import os

# root_path = "E:/me/git/wudong/test_data"
# img1_path = os.path.join(root_path, "button/power_button.jpg")
# img2_path = os.path.join(root_path, "power_test.jpg")
# img1 = cv2.imread(img1_path)  # 查询图像
# img2 = cv2.imread(img2_path)  # 训练图像
# sift_t(img1, img2)


# img1_path = os.path.join(root_path, "ad/ad_name.jpg")
# img2_path = os.path.join(root_path, "ad_test.png")
# img1 = cv2.imread(img1_path)  # 查询图像
# img2 = cv2.imread(img2_path)  # 训练图像
# sift_t(img1, img2, 255)


wd = WindowTool()
# wd = WindowTool(wn="逍遥模拟器4")
loc = wd.get_window_loc()
# img2 = wd.get_screen_img()
#
# # img1_path = os.path.join(root_path, "button/power_button.jpg")
# img1_path = os.path.join("E:/me/git/wudong/sample/button/power_button.jpg")
# img1 = cv2.imread(img1_path)  # 查询图像
# sift_t(img1, img2, 0)
# root_path = "E:/me/git/wudong/sample"
# root_path = "E:/me/git/wudong/test_data"
# img1_path = os.path.join(root_path, "money/1.png")
# img2 = WindowTool().get_screen_img()
# img1 = cv2.imread(img1_path)
# sift_t(img1, img2)

# img = cv2.imread(root_path + "/sample/button/wudong1.png", 0)
# kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
# __xiaoji_get_button = [kp1, des1, img]
#
# dst = SiftTool.get_dst_by_button(self.__agree_button[0], self.__agree_button[1], self.__agree_button[2],
#                                  screen_img)


# root_path = "E:/me/git/wudong/sample/"
# img1_path = os.path.join(root_path, "ad_close/3.png")
# img1_path = os.path.join(root_path, "task/1.png")
# img1_path = os.path.join(root_path, "button/2.png")

root_path = "E:/me/git/wudong/sample/"
# img1_path = os.path.join(root_path, "ad_close/3.png")
# img1_path = os.path.join(root_path, "task/1.png")
img1_path = os.path.join(root_path, "wudong/5.png")


img2 = wd.get_screen_img()#[int(loc[KHEIGHT] * 0.3):]
img1 = cv2.imread(img1_path)
sift_t(img1, img2)