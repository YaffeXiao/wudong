from utils.MouseTool import MouseTool
from core.SiftTool import SiftTool
from utils.ConVar import *
import time, cv2


class WuDongTool:
    # -----------相对定位位置----------------
    # 空白位置
    SPACE_TOP = 0.98
    SPACE_LEFT = 0.6

    # 体力检查位置
    POWER_TOP = 0.6
    POWER_LEFT = 0.2

    # 小人相对位置
    PEOPLE_TOP_RATE = 0.72
    PEOPLE_BOTTOM_RATE = 0.85

    # 返回按钮
    BACK_BUTTON_LEFT = 0.05
    BACK_BUTTON_TOP = 0.95

    # 储钱罐
    CQG_LEFT = 0.6
    CQG_TOP = 0.6

    #广告关闭 高分辨率广告位置
    AD_CLOSE_LEFT = 0.94
    AD_CLOSE_TOP = 0.03

    # 广告关闭 模拟器广告位置
    # AD_CLOSE_LEFT = 0.93
    # AD_CLOSE_TOP = 0.048

    #广告关闭 低分辨率广告位置
    # AD_CLOSE_LEFT = 0.91
    # AD_CLOSE_TOP = 0.06

    # 广告APP安装关闭
    INSTALL_CLOSE_LEFT = 0.8
    INSTALL_CLOSE_TOP = 0.96

    # #观看广告按钮
    # WATCH_AD_button_LEFT = 0.5
    # WATCH_AD_button_TOP = 0.6

    #误触提示接受按钮
    AGREE_CLOSE_LEFT = 0.5
    AGREE_CLOSE_TOP = 0.8

    # 餐厅
    RESTAURANT_LEFT = 0.73
    RESTAURANT_TOP = 0.57

    RESTAURANT_1_LEFT = 0.23
    RESTAURANT_1_TOP = 0.46

    RESTAURANT_2_LEFT = 0.43
    RESTAURANT_2_TOP = 0.54

    RESTAURANT_3_LEFT = 0.76
    RESTAURANT_3_TOP = 0.305

    #靠右侧后相对位置
    RESTAURANT_4_LEFT = 0.57
    RESTAURANT_4_TOP = 0.57

    # 浴室
    SHOWERS_LEFT = 0.62
    SHOWERS_TOP = 0.46

    SHOWERS_1_LEFT = 0.33
    SHOWERS_1_TOP = 0.52

    SHOWERS_2_LEFT = 0.5
    SHOWERS_2_TOP = 0.61

    SHOWERS_3_LEFT = 0.54
    SHOWERS_3_TOP = 0.46

    # 电影院
    CINEMA_LEFT = 0.32
    CINEMA_TOP = 0.37

    CINEMA_FLOWER_LEFT = 0.6
    CINEMA_FLOWER_TOP = 0.6

    # 不看广告按钮
    DWAD_LEFT = 0.3
    DWAD_TOP = 0.6


    # BACK_BUTTON = None
    #
    # WUDONG_WD = None

    @staticmethod
    def click_back_button(loc):
        # dst = SiftTool.get_dst_by_button(WuDongTool.BACK_BUTTON, WuDongTool.WUDONG_WD.get_screen_img())
        # if dst is not None and len(dst) == 4:
        #     print("find back button~~~~~~~~~~~~~~~~~~~~~~~~")
        #     x = int(dst[0, 0, 0]) + 20
        #     y = int(dst[0, 0, 1]) + 20
        #     MouseTool.click_rate_window(loc, x, y)
        # else:
        #     MouseTool.click_rate_window(loc, WuDongTool.BACK_BUTTON_LEFT, WuDongTool.BACK_BUTTON_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.BACK_BUTTON_LEFT, WuDongTool.BACK_BUTTON_TOP)

    @staticmethod
    def rest_game_main_building(loc):
        WuDongTool.click_window_space(loc)
        time.sleep(1)
        WuDongTool.click_back_button(loc)
        time.sleep(1)
        WuDongTool.click_window_space(loc)
        time.sleep(1)

    @staticmethod
    def back_game_main_building(loc):
        WuDongTool.click_back_button(loc)
        time.sleep(1)
        WuDongTool.click_window_space(loc)

    @staticmethod
    def click_space(loc):
        MouseTool.click_rate_window(loc, WuDongTool.SPACE_LEFT, WuDongTool.SPACE_TOP)
        time.sleep(0.2)

    @staticmethod
    def rest_screen_main_building(loc):
        print("rest screen main building")
        WuDongTool.rest_game_main_building(loc)
        i = 0
        while i < 3:
            MouseTool.reset_window_center(loc)
            MouseTool.drag_rel(100, 0)
            time.sleep(0.2)
            i += 1
        j = 0
        while j < 2:
            MouseTool.reset_window_center(loc)
            MouseTool.drag_rel(0, -100)
            time.sleep(0.2)
            j += 1
        time.sleep(1)
        MouseTool.reset_window_center(loc)
        time.sleep(0.1)
        MouseTool.drag_rel(-int(loc[KWIDTH] / 2 - 23), 0)
        time.sleep(2)

    @staticmethod
    def click_piggy(loc, watch_ad=False):
        MouseTool.click_rate_window(loc, WuDongTool.CQG_LEFT, WuDongTool.CQG_TOP)
        time.sleep(0.5)
        # 目前不看广告
        if watch_ad is False:
            MouseTool.click_rate_window(loc, WuDongTool.DWAD_LEFT, WuDongTool.DWAD_TOP)
        time.sleep(1)

    @staticmethod
    def click_window_space(loc):
        MouseTool.click_rate_window(loc, WuDongTool.SPACE_LEFT, WuDongTool.SPACE_TOP)
        time.sleep(0.1)

    @staticmethod
    def get_power_is_empty(loc, img):
        point_rgb = img[int(loc[KHEIGHT] * WuDongTool.POWER_TOP), int(loc[KWIDTH] * WuDongTool.POWER_LEFT)]
        # print(point_rgb)
        if point_rgb[0] > 200 and point_rgb[1] > 200 and point_rgb[3] > 200:
            return True
        return False

    @staticmethod
    def check_restaurant(loc, wd=None, task_buttons=None, buttons=[]):
        WuDongTool.init_room(loc, WuDongTool.RESTAURANT_LEFT, WuDongTool.RESTAURANT_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.RESTAURANT_1_LEFT, WuDongTool.RESTAURANT_1_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.RESTAURANT_2_LEFT, WuDongTool.RESTAURANT_2_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.RESTAURANT_3_LEFT, WuDongTool.RESTAURANT_3_TOP)

        if wd is not None:
            for task_button in task_buttons:
                WuDongTool.click_task(loc, wd, task_button, buttons, str(task_button))

        MouseTool.drag_rel(-350, 0)
        time.sleep(1)
        if wd is not None:
            for task_button in task_buttons:
                WuDongTool.click_task(loc, wd, task_button, buttons, str(task_button))

        MouseTool.click_rate_window(loc, WuDongTool.RESTAURANT_4_LEFT, WuDongTool.RESTAURANT_4_TOP)
        WuDongTool.back_game_main_building(loc)

    @staticmethod
    def check_showers(loc, wd=None, buttons=[]):
        WuDongTool.init_room(loc, WuDongTool.SHOWERS_LEFT, WuDongTool.SHOWERS_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.SHOWERS_1_LEFT, WuDongTool.SHOWERS_1_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.SHOWERS_2_LEFT, WuDongTool.SHOWERS_2_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.SHOWERS_3_LEFT, WuDongTool.SHOWERS_3_TOP)
        WuDongTool.back_game_main_building(loc)

    @staticmethod
    def check_cinema(loc, wd=None, buttons=[], watch_ad=False):
        WuDongTool.init_room(loc, WuDongTool.CINEMA_LEFT, WuDongTool.CINEMA_TOP)
        MouseTool.click_rate_window(loc, WuDongTool.CINEMA_FLOWER_LEFT, WuDongTool.CINEMA_FLOWER_TOP)
        time.sleep(0.5)
        # 目前不看广告
        if watch_ad is False:
            MouseTool.click_rate_window(loc, WuDongTool.DWAD_LEFT, WuDongTool.DWAD_TOP)
        WuDongTool.back_game_main_building(loc)
        time.sleep(0.3)
        WuDongTool.click_back_button(loc)

    @staticmethod
    def init_room(loc, left_rate, top_rate):
        MouseTool.click_rate_window(loc, left_rate, top_rate, 11, 0.01)
        MouseTool.reset_window_center(loc)
        time.sleep(0.5)
        # time.sleep(3)
        MouseTool.drag_rel(200, 0)
        MouseTool.reset_window_center(loc)
        MouseTool.drag_rel(200, 0)
        time.sleep(0.3)

    @staticmethod
    def click_wasai(loc, dst):
        x = int(dst[0, 0, 0]) + 20
        y = int(dst[0, 0, 1]) + 20
        MouseTool.click_obj(loc, x, y)
        time.sleep(0.5)
        WuDongTool.click_buy_goods(loc, 0.25, 0.35)#特价
        start_x_rate = 0.25
        start_y_rate = 0.55
        x_step = 0.25
        y_step = 0.15
        for i in range(2):
            for j in range(3):
                WuDongTool.click_buy_goods(loc, start_x_rate + j * x_step, start_y_rate + i * y_step)
        WuDongTool.click_window_space(loc)

    @staticmethod
    def click_task(loc, wd, task_button, agree_buttons, msg, times=5):
        i = 0
        while i < times:
            # task_img = WuDongTool.get_main_building_img(loc, wd.get_screen_img())
            dst = SiftTool.get_dst_by_task_button(task_button, wd.get_screen_img())
            if dst is not None and len(dst) == 4:
                print("find %s button~~~~~~~~~~~~~~~~~~~~~~~~" % msg)
                x = int(dst[0, 0, 0]) + 10
                y = int(dst[0, 0, 1]) + 10
                MouseTool.click_obj(loc, x, y)
                time.sleep(0.5)
                for b in agree_buttons:#agree_buttons 接受人物或领取奖励
                    dst = SiftTool.get_dst_by_button(b, wd.get_screen_img())
                    if dst is not None and len(dst) == 4:
                        MouseTool.click_obj(loc, x, y)
                        time.sleep(0.5)
                        break
            i += 1
        time.sleep(0.5)

    @staticmethod
    def click_buy_goods(loc, x_rate, y_rate):
        MouseTool.click_obj(loc, loc[KWIDTH] * x_rate, loc[KHEIGHT] * y_rate)
        time.sleep(0.3)
        MouseTool.click_obj(loc, loc[KWIDTH] * 0.5, loc[KHEIGHT] * 0.62)
        time.sleep(0.3)
        MouseTool.click_obj(loc, loc[KWIDTH] * 0.5, loc[KHEIGHT] * 0.62)
        time.sleep(0.5)

    @staticmethod
    def search_and_click_button(loc, screen_img, button,  msg="", x_offset=50, y_offset=20, count=1, interval=0.25):
        dst = SiftTool.get_dst_by_button(button, screen_img)
        if dst is not None and len(dst) == 4:
            print("find %s button and click ~~~~~~~~~~~~~~~~~~~~~~~~" % msg)
            x = int(dst[0, 0, 0]) + x_offset
            y = int(dst[0, 0, 1]) + y_offset
            MouseTool.click_obj(loc, x, y, count, interval)
            time.sleep(0.3)

    @staticmethod
    def draw_marker(loc, img):
        x = loc[KLEFT] + int(loc[KWIDTH] * WuDongTool.RESTAURANT_1_LEFT)
        y = loc[KTOP] + int(loc[KHEIGHT] * WuDongTool.RESTAURANT_1_TOP)
        cv2.drawMarker(img, (x, y), (0, 0, 255), cv2.MARKER_SQUARE)

    @staticmethod
    def close_ad(loc):
        x = int(loc[KWIDTH] * WuDongTool.AD_CLOSE_LEFT)
        y = int(loc[KHEIGHT] * WuDongTool.AD_CLOSE_TOP)
        MouseTool.click_obj(loc, x, y)

    @staticmethod
    def get_main_building_img(loc, screen_img):
        return screen_img[:int(loc[KHEIGHT] * WuDongTool.PEOPLE_BOTTOM_RATE)]
