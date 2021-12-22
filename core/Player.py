import sys
import time

from utils.ViewTool import *
from utils.WuDongTool import WuDongTool
from utils.WindowTool import WindowTool
from utils.ConVar import *
from random import sample
from utils.MouseTool import MouseTool
from datetime import datetime, timedelta
import cv2


def check_close_status():
    if Player.STOP_PROGRAM is True:
        print("press ESC stop program")
        sys.exit(0)


class Player:
    STOP_PROGRAM = False

    def __init__(self, screen="off"):
        self.__screen = screen
        self.__wd_window = WindowTool()
        self.__wudong_window_loc = self.__wd_window.get_window_loc()
        print("wudong_window_loc:")
        print(self.__wudong_window_loc)
        self.__last_cqg_time = datetime.utcnow()
        self.__last_ct_time = datetime.utcnow()
        self.__last_ys_time = datetime.utcnow()
        self.vt = ViewTool()
        self.__people_top_index = None
        self.__people_bottom_index = None
        self.__init_datas()
        self.stop_program = False
        self.error_times = 0

    def start_play(self):
        # 仅第一次和出错后执行
        WuDongTool.rest_screen_main_building(self.__wudong_window_loc)
        if self.__screen == "debug":
            while True:
                check_close_status()
                screen_img = self.__wd_window.get_screen_img()
                _screen_img = self.__debug(screen_img)
                cv2.imshow('wudong', _screen_img)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
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

    def process_task(self, img):
        self.__check_cqg()
        self.__check_ct(self.__wudong_window_loc)
        self.__check_ys(self.__wudong_window_loc)
        gray_img = get_gray_img(img)
        people_gray_img = gray_img[self.__people_top_index: self.__people_bottom_index]
        contours = self.vt.get_rectangle(people_gray_img)
        if len(contours) < 5:
            self.error_times += 1
        if len(contours) == 0:
            print("check people error ~~~~~~~~~")
            self.error_times += 1
            time.sleep(1)
            return img
        if self.error_times > 10:
            WuDongTool.rest_game_main_building(self.__wudong_window_loc)
            time.sleep(1)
            WuDongTool.rest_screen_main_building(self.__wudong_window_loc)
            time.sleep(1)
        if self.error_times > 5:
            print("monster")
            contours = ViewTool(100, 600).get_rectangle(people_gray_img)
            if len(contours) == 0:
                return img
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawMarker(img, (x + int(w / 2), y + self.__people_top_index + int(h / 2)), (0, 0, 255), 0)
                MouseTool.click_obj(self.__wudong_window_loc, x, y + self.__people_top_index, 29, 0.01)
        if self.__screen == "debug" or self.__screen == "on":
            image_rectangle(img, contours, self.__people_top_index)
        img = self.__click_people(img, contours)
        self.__check_power(img)
        WuDongTool.click_space(self.__wudong_window_loc)
        self.error_times = 0
        return img

    def __init_datas(self):
        loc = self.__wudong_window_loc
        self.__people_top_index = int(loc[KHEIGHT] * WuDongTool.PEOPLE_TOP_RATE)
        self.__people_bottom_index = int(loc[KHEIGHT] * WuDongTool.PEOPLE_BOTTOM_RATE)

    def __click_people(self, img, contours):
        WuDongTool.click_space(self.__wudong_window_loc)
        # contours
        contour = sample(contours, 1)[0]
        x, y, w, h = cv2.boundingRect(contour)
        cv2.drawMarker(img, (x + int(w / 2), y + self.__people_top_index + int(h / 2)), (0, 0, 255), 0)
        MouseTool.click_obj(self.__wudong_window_loc, x, y + self.__people_top_index, 29, 0.01)
        time.sleep(0.5)
        return img

    def screen(self, _fun):
        while True:
            screen_img = self.__wd_window.get_screen_img()
            _screen_img = _fun(screen_img)
            cv2.imshow('wudong', _screen_img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    def init_sample(self):
        pass

    def __debug(self, img):
        gray_img = get_gray_img(img)
        people_gray_img = gray_img[self.__people_top_index: self.__people_bottom_index]
        contours = self.vt.get_rectangle(people_gray_img)
        if len(contours) < 10:
            print("monster")
            contours = ViewTool(100, 600).get_rectangle(people_gray_img)
            if len(contours) == 0:
                return img
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawMarker(img, (x + int(w / 2), y + self.__people_top_index + int(h / 2)), (0, 0, 255), 0)
                MouseTool.click_obj(self.__wudong_window_loc, x, y + self.__people_top_index, 29, 0.1)
        print(len(contours))
        image_rectangle(img, contours, self.__people_top_index)
        return img

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

    def __check_ys(self, loc):
        if datetime.utcnow() <= self.__last_ys_time + timedelta(minutes=1):
            return
        print("check showers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        WuDongTool.check_showers(loc)
        self.__last_ys_time = datetime.utcnow()

    def __check_power(self, img):
        print("check power ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if WuDongTool.get_power_is_empty(self.__wudong_window_loc, img):
            print("power is empty sleep 5 seconds!!!!")
            time.sleep(5)