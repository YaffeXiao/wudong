from utils.ViewTool import *
from utils.WuDongTool import WuDongTool
from utils.WindowTool import WindowTool
from utils.ConVar import *
from random import sample
from utils.MouseTool import MouseTool
from datetime import datetime, timedelta
import cv2, time, sys, os
import numpy as np
from core.SiftTool import SiftTool
import win32api
import os


def check_close_status():
    if Player.STOP_PROGRAM is True:
        print("press ESC stop program")
        sys.exit(0)


class Player:
    STOP_PROGRAM = False
    GLOBAL_SCREEN_IMG = None

    def __init__(self, screen="off"):
        self.__root_path = os.getcwd()
        self.__screen = screen
        # self.__wd_window = WindowTool()
        self.__wd_window = WindowTool(up_offset=36)
        # self.__wd_window = WindowTool(up_offset=30, wn="逍遥模拟器4")
        self.__wudong_window_loc = self.__wd_window.get_window_loc()
        print("wudong_window_loc:" + str(self.__wudong_window_loc))
        self.__check_time = 1 #分钟
        self.__rest_time = 10 #分钟
        self.__last_cqg_time = datetime.utcnow()
        self.__last_ct_time = datetime.utcnow()
        self.__last_ys_time = datetime.utcnow()
        self.__last_yy_time = datetime.utcnow()
        self.__last_ws_time = datetime.utcnow()
        self.__people_top_index = None
        self.__people_bottom_index = None
        self.stop_program = False
        self.__p_list = []
        self.__m_list = []
        self.__s_list = []
        self.__power_button = None
        self.__ad_wait_button = None
        self.__ad_close_buttons = []
        self.__xiaoji_get_button = None
        self.__wasai_buttons = []
        self.__heart_button = None
        self.__get_button = None
        self.__wudong_buttons = []
        self.__right_buttons = []
        self.__exclamation_button = None
        self.__init_datas()
        self.__init_buttons()
        self.__last_rest_time = datetime.utcnow()

    def start_play(self):

        if self.__screen == "debug":
            while True:
                check_close_status()
                screen_img = self.__wd_window.get_screen_img()
                screen_img = self.debug_process_task(screen_img)
                cv2.imshow('wudong', screen_img)
                # if Player.GLOBAL_SCREEN_IMG is None:
                #     cv2.imshow('wudong', screen_img)
                # else:
                #     cv2.imshow('wudong', Player.GLOBAL_SCREEN_IMG)
                #     Player.GLOBAL_SCREEN = None
                cv2.waitKey(1)

        if self.__screen == "on":
            while True:
                check_close_status()
                screen_img = self.__wd_window.get_screen_img()
                _screen_img = self.process_task(screen_img)
                cv2.imshow('wudong', _screen_img)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
        else:
            # 仅第一次和出错后执行
            # WuDongTool.rest_screen_main_building(self.__wudong_window_loc)
            while True:
                check_close_status()
                screen_img = self.__wd_window.get_screen_img()
                self.process_task(screen_img)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break

    def debug_process_task(self, img):

        # img = self.__click_monster(img)
        # img = self.__click_people(img)
        # self.__check_wudong()
        self.__clear_buttons()
        # self.__check_xiaoji()
        # self.__check_ct()
        # self.__check_right_button()
        # self.__check_install_app()
        # self.__rest_game(True)
        # self.__check_main_building_task()
        # self.__rest_game()
        # self.__check_wudong()
        return img

    def process_task(self, img):
        i = 1
        while i <= 10:
            if self.__check_wudong():
                break
            i += 1
        if i > 10:
            self.__rest_game(True)
        self.__check_xiaoji()
        self.__check_wasai()
        self.__check_cqg()
        self.__check_ct()
        self.__check_ys()
        self.__check_yy()
        self.__click_monster()
        i = 0
        while i < 20:
            self.__click_people()
            i += 1
        self.__check_watch_ad_button(self.__power_button)
        # self.__check_main_building_task()
        WuDongTool.click_window_space(self.__wudong_window_loc)
        self.__rest_game()
        return img

    def __check_watch_ad_button(self, watch_button):
        screen_img = self.__wd_window.get_screen_img()
        time.sleep(1)
        # b = self.__power_share_button
        # dst = SiftTool.get_dst_by_button(b[0], b[1], b[2], screen_img)
        # if dst is not None and len(dst) == 4:
        #     print("don't share WX")
        #     WuDongTool.click_space(self.__wudong_window_loc)
            # MouseTool.click_obj(self.__wudong_window_loc, int(dst[0, 0, 0]) + 30,
            #                     int(dst[0, 0, 1]) + 50, 1, 0.01)
            # wx = WindowTool(up_offset=0, wn="微信")
            # wx_loc = wx.get_window_loc()
            # x = wx_loc[KWIDTH] * 0.09
            # y = wx_loc[KHEIGHT] * 0.08
            # MouseTool.click_obj(wx_loc, x, y)
            # win32api.keybd_event(87, 0, 0, 0)
            # win32api.keybd_event(69, 0, 0, 0)
            # win32api.keybd_event(78, 0, 0, 0)
            # win32api.keybd_event(13, 0, 0, 0)
            # time.sleep(0.5)
            # MouseTool.click_obj(wx_loc, x, wx_loc[KHEIGHT] * 0.2)
            #
            # MouseTool.click_obj(wx_loc, wx_loc[KWIDTH] * 0.8, wx_loc[KHEIGHT] * 0.95)

        dst = SiftTool.get_dst_by_button(self.__ad_wait_button, screen_img)
        if dst is not None and len(dst) == 4:
            print("don't have ad for watch")
            WuDongTool.click_window_space(self.__wudong_window_loc)
            print("stop 30 seconds")
            time.sleep(30)
            return

        dst = SiftTool.get_dst_by_button(watch_button, screen_img)
        # print(dst)
        if dst is not None and len(dst) == 4:
            x = int(dst[0, 0, 0]) + 100
            y = int(dst[0, 0, 1]) + 50
            MouseTool.click_obj(self.__wudong_window_loc, x, y)
            star_time = datetime.utcnow()
            last_img = screen_img
            print("start watch ad")

            while datetime.utcnow() < star_time + timedelta(seconds=35):
                time.sleep(1)
                new_img = self.__wd_window.get_screen_img()
                # print(np.abs(new_img - last_img).max())
                if np.abs(new_img - last_img).max() < 10:
                    print("watch ad stop click close")
                    break
                else:
                    print("ad is running")
                last_img = new_img.copy()

                if datetime.utcnow() > star_time + timedelta(seconds=10):
                    MouseTool.reset_window_center(self.__wudong_window_loc)
                    MouseTool.drag_rel(0, -100)

            # time.sleep(35)
            for close_b in self.__ad_close_buttons:
                dst = SiftTool.get_dst_by_button(close_b, screen_img)
                print(dst)
                if dst is not None and len(dst) == 4:
                    x = int(dst[0, 0, 0]) + 20
                    y = int(dst[0, 0, 1]) + 15
                    print("find close button")
                    MouseTool.click_obj(self.__wudong_window_loc, x, y)
                    self.__check_install_app()
                    return

            print("can't find close button")
            WuDongTool.close_ad(self.__wudong_window_loc)
            time.sleep(4)
            WuDongTool.close_ad(self.__wudong_window_loc)
            self.__check_install_app()
            return

    def __check_install_app(self):
        time.sleep(0.5)
        WuDongTool.close_ad(self.__wudong_window_loc)
        screen_img = self.__wd_window.get_screen_img()
        if np.sum(screen_img[300:500, 300:500][:, :, :3] != 250) == 0:
            print("start install app")
            MouseTool.click_rate_window(self.__wudong_window_loc, WuDongTool.INSTALL_CLOSE_LEFT, WuDongTool.INSTALL_CLOSE_TOP)
            WuDongTool.close_ad(self.__wudong_window_loc)

    def __click_people(self, counts=11):
        screen_img = self.__wd_window.get_screen_img()
        people_img = screen_img[self.__people_top_index: self.__people_bottom_index]
        for p in self.__p_list:
            dst = SiftTool.get_dst_by_p(p, people_img)
            if dst is not None and len(dst) == 4:
                # print(dst)
                if self.__screen == "debug":
                    print(dst)
                    Player.GLOBAL_SCREEN = cv2.polylines(people_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
                else:
                    x = int(dst[0, 0, 0]) + 10
                    y = int(dst[0, 0, 1]) + 10 + self.__people_top_index
                    MouseTool.click_obj(self.__wudong_window_loc, x, y, counts, 0)
                    break
        return people_img

    def __click_monster(self):
        screen_img = self.__wd_window.get_screen_img()
        monster_img = screen_img[self.__people_top_index: self.__people_bottom_index]
        for m in self.__m_list:
            dst = SiftTool.get_dst_by_m(m, monster_img)
            if dst is not None and len(dst) == 4:
                # dst[:, :, 1] = dst[:, :, 1] + self.__people_top_index
                print("click monster ")
                if self.__screen == "debug":
                    print(dst)
                    Player.GLOBAL_SCREEN = cv2.polylines(monster_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
                else:
                    WuDongTool.click_window_space(self.__wudong_window_loc)
                    x = int(dst[0, 0, 0]) + 20
                    y = int(dst[0, 0, 1]) + 20 + self.__people_top_index
                    # print(x, y)
                    cv2.drawMarker(screen_img, (x, y), (0, 0, 255), 0)
                    Player.GLOBAL_SCREEN_IMG = monster_img
                    MouseTool.click_obj(self.__wudong_window_loc, x, y, 30, 0.01)
                    break
        return monster_img

    def __check_cqg(self):
        if datetime.utcnow() <= self.__last_cqg_time + timedelta(minutes=self.__check_time ):
            return
        print("check piggy bank ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.click_piggy(self.__wudong_window_loc)
        self.__last_cqg_time = datetime.utcnow()

    def __check_wasai(self):
        screen_img = self.__wd_window.get_screen_img()
        if datetime.utcnow() <= self.__last_yy_time + timedelta(minutes=self.__check_time):
            return screen_img
        print("check wasai ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        wasai_img = WuDongTool.get_main_building_img(self.__wudong_window_loc, screen_img)
        for b in self.__wasai_buttons:
            dst = SiftTool.get_dst_by_m(b, wasai_img)
            if dst is not None and len(dst) == 4:
                if self.__screen == "debug":
                    cv2.polylines(wasai_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
                else:
                    WuDongTool.click_wasai(self.__wudong_window_loc, dst)
                self.__last_yy_time = datetime.utcnow()
                break
        return wasai_img

    def __check_ct(self):
        if datetime.utcnow() <= self.__last_ct_time + timedelta(minutes=self.__check_time):
            return
        print("check restaurant ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.check_restaurant(self.__wudong_window_loc)
        self.__last_ct_time = datetime.utcnow()
        # time.sleep(0.5)

    def __check_ys(self):
        if datetime.utcnow() <= self.__last_ys_time + timedelta(minutes=self.__check_time):
            return
        print("check showers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.check_showers(self.__wudong_window_loc)
        self.__last_ys_time = datetime.utcnow()
        # time.sleep(0.5)

    def __check_yy(self):
        if datetime.utcnow() <= self.__last_yy_time + timedelta(minutes=self.__check_time):
            return
        print("check cinema ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.check_cinema(self.__wudong_window_loc)
        self.__last_yy_time = datetime.utcnow()
        # time.sleep(0.5)

    def __check_right_button(self):
        print("check right button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for r_button in self.__right_buttons:
            dst = SiftTool.get_dst_by_button(r_button, self.__wd_window.get_screen_img())
            if dst is not None and len(dst) == 4:
                x = int(dst[0, 0, 0]) + 30
                y = int(dst[0, 0, 1]) + 30
                MouseTool.click_obj(self.__wudong_window_loc, x, y)
                self.__check_watch_ad_button(self.__get_button)

    def __rest_game(self, force=False):
        print("start rest game")
        if force is False and datetime.utcnow() <= self.__last_rest_time + timedelta(minutes=self.__rest_time):
            return
        WuDongTool.close_ad(self.__wudong_window_loc)
        if self.__check_wudong():
            return
        self.__check_xiaoji()
        if self.__check_wudong():
            return
        self.__clear_buttons()
        if self.__check_wudong():
            return
        self.__check_install_app()
        if self.__check_wudong():
            return
        WuDongTool.rest_screen_main_building(self.__wudong_window_loc)
        if self.__check_wudong():
            return
        self.__last_rest_time = datetime.utcnow()

    def __clear_buttons(self):
        screen_img = self.__wd_window.get_screen_img()
        MouseTool.click_rate_window(self.__wudong_window_loc, WuDongTool.AGREE_CLOSE_LEFT, WuDongTool.AGREE_CLOSE_TOP)
        WuDongTool.search_and_click_button(self.__wudong_window_loc, screen_img, self.__prize_button, "prize")
        WuDongTool.search_and_click_button(self.__wudong_window_loc, screen_img, self.__agree_button, "agree")

    def __check_wudong(self):
        for i in range(len(self.__wudong_buttons)):
            screen_img = self.__wd_window.get_screen_img()
            dst = SiftTool.get_dst_by_button(self.__wudong_buttons[i], screen_img)
            # print(dst)
            if dst is not None and len(dst) == 4:
                wd_x = int(dst[0, 0, 0]) + int((dst[2, 0, 0] - dst[0, 0, 0]) / 2)
                center_x = int(self.__wudong_window_loc[KWIDTH] / 2)
                cha = abs(center_x - wd_x)
                if cha < 2:
                    print("wudong on window center")
                    return True
                else:
                    print("wudong is deviation %d" % cha)
                    # if reset_x_direction:
                    MouseTool.reset_window_center(self.__wudong_window_loc)
                    MouseTool.drag_rel(center_x - wd_x, 0)
                    return True
        print("wudong is missing")
        return False

    def __check_xiaoji(self):
        screen_img = self.__wd_window.get_screen_img()
        dst = SiftTool.get_dst_by_button(self.__xiaoji_get_button, screen_img)
        if dst is not None and len(dst) == 4:
            print("find xiaoji get button~~~~~~~~~~~~~~~~~~~~~~~~")
            x = int(dst[0, 0, 0]) + 30
            y = int(dst[0, 0, 1]) + 10
            MouseTool.click_obj(self.__wudong_window_loc, x, y)
            WuDongTool.click_window_space(self.__wudong_window_loc)
            WuDongTool.click_back_button(self.__wudong_window_loc)
        else:
            WuDongTool.click_window_space(self.__wudong_window_loc)

    def __check_main_building_task(self):
        WuDongTool.click_task(self.__wudong_window_loc, self.__wd_window, self.__clock_button,
                              [self.__agree_button, self.__prize_button], "clock")
        WuDongTool.click_task(self.__wudong_window_loc, self.__wd_window, self.__exclamation_button,
                              [self.__agree_button, self.__prize_button], "exclamation")

    def __init_datas(self):
        loc = self.__wudong_window_loc
        self.__people_top_index = int(loc[KHEIGHT] * WuDongTool.PEOPLE_TOP_RATE)
        self.__people_bottom_index = int(loc[KHEIGHT] * WuDongTool.PEOPLE_BOTTOM_RATE)
        # file_list = os.listdir("sample/p/")
        p_path = self.__root_path + "/sample/p/"
        m_path = self.__root_path + "/sample/m/"
        file_list = os.listdir(p_path)
        for file_name in file_list:
            file_full_name = p_path + file_name
            img = cv2.imread(file_full_name, 0)
            kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
            self.__p_list.append([kp1, des1, img])
        file_list = os.listdir(m_path)
        for file_name in file_list:
            file_full_name = m_path + file_name
            img = cv2.imread(file_full_name, 0)
            kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
            self.__m_list.append([kp1, des1, img])

    def __init_buttons(self):
        img = cv2.imread(self.__root_path + "/sample/button/power_button.jpg", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__power_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/button/power_share_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__power_share_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/button/ad_wait.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__ad_wait_button = [kp1, des1, img]

        wasai_path = self.__root_path + "/sample/wasai/"
        wasai_files = os.listdir(wasai_path)
        for f in wasai_files:
            img = cv2.imread(wasai_path + f, 0)
            kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
            self.__wasai_buttons.append([kp1, des1, img])

        img = cv2.imread(self.__root_path + "/sample/button/xiaoji_get_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__xiaoji_get_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/button/get_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__get_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/task/heart_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__heart_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/task/clock_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__clock_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/task/agree_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__agree_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/task/prize_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__prize_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/task/exclamation_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__exclamation_button = [kp1, des1, img]

        wudong_path = self.__root_path + "/sample/wudong/"
        wudong_file_names = os.listdir(wudong_path)
        for file_name in wudong_file_names:
            img = cv2.imread(wudong_path + file_name, 0)
            kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
            self.__wudong_buttons.append([kp1, des1, img])

        close_path = self.__root_path + "/sample/ad_close/"
        close_file_names = os.listdir(close_path)
        for file_name in close_file_names:
            img = cv2.imread(close_path + file_name, 0)
            kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
            self.__ad_close_buttons.append([kp1, des1, img])

        close_path = self.__root_path + "/sample/r_button/"
        close_file_names = os.listdir(close_path)
        for file_name in close_file_names:
            img = cv2.imread(close_path + file_name, 0)
            kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
            self.__right_buttons.append([kp1, des1, img])

    # def screen(self, _fun):
    #     while True:
    #         screen_img = self.__wd_window.get_screen_img()
    #         _screen_img = _fun(screen_img)
    #         cv2.imshow('wudong', _screen_img)
    #         key = cv2.waitKey(1)
    #         if key == ord('q'):
    #             break