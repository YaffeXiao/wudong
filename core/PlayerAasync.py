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
        self.__wd_window = WindowTool()
        self.__wudong_window_loc = self.__wd_window.get_window_loc()
        print("wudong_window_loc:" + str(self.__wudong_window_loc))
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
        self.__ws_button = None
        self.__xiaoji_get_button = None
        self.__init_datas()
        self.__init_buttons()
        self.__last_rest_time = datetime.utcnow()

    def start_play(self):
        # 仅第一次和出错后执行
        # WuDongTool.rest_screen_main_building(self.__wudong_window_loc)
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
        img = self.__check_wasai(self.__wudong_window_loc)

        # self.__rest_game()

        return img

    def process_task(self, img):

        self.__check_wasai(self.__wudong_window_loc)
        self.__check_cqg()
        self.__check_ct(self.__wudong_window_loc)
        self.__check_ys(self.__wudong_window_loc)
        self.__check_yy(self.__wudong_window_loc)
        self.__click_monster(img)
        i = 0
        while i < 10:
            self.__click_people(img)
            img = self.__wd_window.get_screen_img()
            i += 1
        self.__check_power()
        self.__click_agree_button(img)
        WuDongTool.click_space(self.__wudong_window_loc)
        self.__rest_game()
        return img

    def __check_power(self):
        screen_img = self.__wd_window.get_screen_img()
        time.sleep(0.5)
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



        b = self.__ad_wait_button
        dst = SiftTool.get_dst_by_button(b[0], b[1], b[2], screen_img)
        if dst is not None and len(dst) == 4:
            print("don't have ad for watch")
            WuDongTool.click_space(self.__wudong_window_loc)
            print("stop 60 seconds")
            time.sleep(60)
            return

        b = self.__power_button
        dst = SiftTool.get_dst_by_button(b[0], b[1], b[2], screen_img)
        print(dst)
        if dst is not None and len(dst) == 4:
            x = int(dst[0, 0, 0]) + 100
            y = int(dst[0, 0, 1]) + 50
            MouseTool.click_obj(self.__wudong_window_loc, x, y)
            star_time = datetime.utcnow()
            last_img = screen_img
            print("start watch ad")
            while datetime.utcnow() < star_time + timedelta(seconds=35):
                new_img = self.__wd_window.get_screen_img()
                print(np.abs(new_img - last_img).max())
                if np.abs(new_img - last_img).max() < 10:
                    print("watch ad stop click close")
                    break
                last_img = new_img.copy()
                time.sleep(1)

            # time.sleep(35)
            WuDongTool.close_ad(self.__wudong_window_loc)
            return

    def __click_people(self, screen_img, counts=11):
        people_img = screen_img[self.__people_top_index: self.__people_bottom_index]
        for p in self.__p_list:
            dst = SiftTool.get_dst_by_p(p[0], p[1], p[2], people_img)
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

    def __click_monster(self, screen_img):
        monster_img = screen_img[self.__people_top_index: self.__people_bottom_index]
        for m in self.__m_list:
            dst = SiftTool.get_dst_by_m(m[0], m[1], m[2], monster_img)
            print(dst)
            if dst is not None and len(dst) == 4:
                # dst[:, :, 1] = dst[:, :, 1] + self.__people_top_index
                print("click monster ")
                if self.__screen == "debug":
                    print(dst)
                    Player.GLOBAL_SCREEN = cv2.polylines(monster_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
                else:
                    WuDongTool.click_space(self.__wudong_window_loc)
                    x = int(dst[0, 0, 0]) + 20
                    y = int(dst[0, 0, 1]) + 20 + self.__people_top_index
                    # print(x, y)
                    cv2.drawMarker(screen_img, (x, y), (0, 0, 255), 0)
                    Player.GLOBAL_SCREEN_IMG = monster_img
                    MouseTool.click_obj(self.__wudong_window_loc, x, y, 30, 0.01)
                    break

        return monster_img

    def screen(self, _fun):
        while True:
            screen_img = self.__wd_window.get_screen_img()
            _screen_img = _fun(screen_img)
            cv2.imshow('wudong', _screen_img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    def __check_cqg(self):
        if datetime.utcnow() <= self.__last_cqg_time + timedelta(minutes=1):
            return
        print("check piggy bank ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.click_cqg(self.__wudong_window_loc)
        self.__last_cqg_time = datetime.utcnow()

    def __check_ct(self, loc):
        if datetime.utcnow() <= self.__last_ct_time + timedelta(minutes=1):
            return
        print("check restaurant ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.check_restaurant(loc)
        self.__last_ct_time = datetime.utcnow()
        # time.sleep(0.5)

    def __check_ys(self, loc):
        if datetime.utcnow() <= self.__last_ys_time + timedelta(minutes=1):
            return
        print("check showers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.check_showers(loc)
        self.__last_ys_time = datetime.utcnow()
        # time.sleep(0.5)

    def __check_yy(self, loc):
        if datetime.utcnow() <= self.__last_yy_time + timedelta(minutes=1):
            return
        print("check cinema ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.check_cinema(loc)
        self.__last_yy_time = datetime.utcnow()
        # time.sleep(0.5)

    def __check_wasai(self, loc):
        screen_img = self.__wd_window.get_screen_img()
        # if datetime.utcnow() <= self.__last_yy_time + timedelta(minutes=1):
        #     return screen_img
        print("check wasai ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        b = self.__ws_button
        dst = SiftTool.get_dst_by_m(b[0], b[1], b[2], self.__wd_window.get_screen_img())
        if dst is not None and len(dst) == 4:
            cv2.polylines(screen_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
            WuDongTool.click_wasai(loc, dst)
            self.__last_yy_time = datetime.utcnow()
        return screen_img

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

        img = cv2.imread(self.__root_path + "/sample/button/agree_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__agree_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/button/power_share_button.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__power_share_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/button/ad_wait.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__ad_wait_button = [kp1, des1, img]

        img = cv2.imread(self.__root_path + "/sample/button/wasai.png", 0)
        kp1, des1 = SiftTool.SIFT.detectAndCompute(img, None)
        self.__ws_button = [kp1, des1, img]

    def __rest_game(self):
        # self.__check_wudong()

        self.__check_xiaoji()

        if datetime.utcnow() <= self.__last_rest_time + timedelta(minutes=10):
            return
        WuDongTool.rest_screen_main_building(self.__wudong_window_loc)
        self.__last_rest_time = datetime.utcnow()

    def __check_wudong(self):
        img = self.__wd_window.get_screen_img()

    def __click_agree_button(self, screen_img):
        dst = SiftTool.get_dst_by_button(self.__agree_button[0], self.__agree_button[1], self.__agree_button[2], screen_img)
        if dst is not None and len(dst) == 4:
            Player.GLOBAL_SCREEN = cv2.polylines(screen_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
            x = int(dst[0, 0, 0]) + 30
            y = int(dst[0, 0, 1]) + 30
            MouseTool.click_obj(self.__wudong_window_loc, x, y)
        return screen_img

    def __check_xiaoji(self):
        screen_img = self.__wd_window.get_screen_img()
        dst = SiftTool.get_dst_by_button(self.__agree_button[0], self.__agree_button[1], self.__agree_button[2],
                                         screen_img)
        if dst is not None and len(dst) == 4:
            x = int(dst[0, 0, 0]) + 50
            y = int(dst[0, 0, 1]) + 20
            MouseTool.click_obj(self.__wudong_window_loc, x, y)
            WuDongTool.click_space(self.__wudong_window_loc)
            WuDongTool.click_space(self.__wudong_window_loc)


