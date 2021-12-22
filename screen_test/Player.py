import threading

import cv2
from utils.ConVar import *
from utils.WindowTool import WindowTool
from utils.WuDongTool import WuDongTool
from screen_test.Sift import *
import os

GLOBAL_SCREEN_IMG = None
PEOPLE_THREAD_FINISHED = True

class Player:

    def __init__(self):
        self.__wd_window = WindowTool()
        self.__wudong_window_loc = self.__wd_window.get_window_loc()
        self.p_list = []
        self.m_list = []
        self.s_list = []
        self.__people_top_index = None
        self.__people_bottom_index = None
        self.__init_datas()


    def play_people(self):
        global GLOBAL_SCREEN_IMG
        while True:
            screen_img = self.__wd_window.get_screen_img()[self.__people_top_index: self.__people_bottom_index]
            # if PEOPLE_THREAD_FINISHED:
            #     threading.Thread(target=self.__check_people, args=(self, screen_img)).start()
            self.__check_people(screen_img)
            if GLOBAL_SCREEN_IMG is None:
                cv2.imshow('wudong', screen_img)
            else:
                cv2.imshow('wudong', GLOBAL_SCREEN_IMG)
                GLOBAL_SCREEN_IMG = None
            cv2.waitKey(1)

    def play_monster(self):
        global GLOBAL_SCREEN_IMG
        while True:
            screen_img = self.__wd_window.get_screen_img()[self.__people_top_index: self.__people_bottom_index]
            # if PEOPLE_THREAD_FINISHED:
            #     threading.Thread(target=self.__check_people, args=(self, screen_img)).start()
            self.__check_monster(screen_img)
            if GLOBAL_SCREEN_IMG is None:
                cv2.imshow('wudong', screen_img)
            else:
                cv2.imshow('wudong', GLOBAL_SCREEN_IMG)
                GLOBAL_SCREEN_IMG = None
            cv2.waitKey(1)


    def __init_datas(self):
        loc = self.__wudong_window_loc
        self.__people_top_index = int(loc[KHEIGHT] * WuDongTool.PEOPLE_TOP_RATE)
        self.__people_bottom_index = int(loc[KHEIGHT] * WuDongTool.PEOPLE_BOTTOM_RATE)
        file_list = os.listdir("test_data/p/")
        for file_name in file_list:
            file_full_name = "test_data/p/" + file_name
            img = cv2.imread(file_full_name, 0)
            kp1, des1 = sift.detectAndCompute(img, None)
            self.p_list.append([kp1, des1, img])
        file_list = os.listdir("test_data/m/")
        for file_name in file_list:
            file_full_name = "test_data/m/" + file_name
            img = cv2.imread(file_full_name, 0)
            kp1, des1 = sift.detectAndCompute(img, None)
            self.m_list.append([kp1, des1, img])

    def __check_people(self, screen_img):

        global GLOB_SCREEN_IMG, PEOPLE_THREAD_FINISHED
        PEOPLE_THREAD_FINISHED = False
        # dst = get_dst(cv2.imread("test_data/p/ad_name.jpg"), screen_img)
        # if dst is not None and len(dst) == 4:
        #     GLOB_SCREEN_IMG = cv2.polylines(screen_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
        # PEOPLE_THREAD_FINISHED = True
        for p in self.p_list:
            dst = get_dst_by_p(p[0], p[1], p[2], screen_img)
            if dst is not None and len(dst) == 4:
                GLOB_SCREEN_IMG = cv2.polylines(screen_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
                break
            PEOPLE_THREAD_FINISHED = True


    def __check_monster(self, screen_img):

        global GLOB_SCREEN_IMG, PEOPLE_THREAD_FINISHED
        PEOPLE_THREAD_FINISHED = False
        for m in self.m_list:
            dst = get_dst_by_p(m[0], m[1], m[2], screen_img)
            if dst is not None and len(dst) == 4:
                GLOB_SCREEN_IMG = cv2.polylines(screen_img, [np.int32(dst)], True, 255, 1, cv2.LINE_AA)
                break
            PEOPLE_THREAD_FINISHED = True


