import cv2
import numpy as np


class SiftTool:
    MIN_MATCH_COUNT = 10
    SIFT = cv2.SIFT_create()

    @staticmethod
    def get_dst_by_p(kp1, des1, img1, img2):
        return SiftTool.get_dst_common(kp1, des1, img1, img2, min_match_count=6)

    @staticmethod
    def get_dst_by_m(kp1, des1, img1, img2):
        return SiftTool.get_dst_common(kp1, des1, img1, img2, min_match_count=8,
                                       obj_size=[30, 200])

    @staticmethod
    def get_dst_by_button(kp1, des1, img1, img2):
        return SiftTool.get_dst_common(kp1, des1, img1, img2, min_match_count=6,
                                       obj_size=[1, 1000], distance_rate=0.4)

    @staticmethod
    def get_dst_common(kp1, des1, img1, img2, min_match_count=10, obj_size=[20, 100], distance_rate=0.7):
        try:
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            # 使用SIFT检测器寻找关键点和描述符
            kp2, des2 = SiftTool.SIFT.detectAndCompute(img2, None)
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)
            # 根据Lowe比率测试存储所有良好匹配项
            good = []
            for m, n in matches:
                if m.distance < distance_rate * n.distance:
                    good.append(m)

            if len(good) > min_match_count:
                src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                h, w = img1.shape
                pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)
                # print(dst)
                # print(np.abs(dst[:, :, 0].max() - dst[:, :, 0].min()))
                # print(np.abs(dst[:, :, 1].max() - dst[:, :, 1].min()))
                ####### ------------ dst[:, :, 0] is x    dst[:, :, 1] is y --------- ###########
                if np.abs(dst[:, :, 0].max() - dst[:, :, 0].min()) < obj_size[0] or \
                        np.abs(dst[:, :, 0].max() - dst[:, :, 0].min()) > obj_size[1] or \
                        np.abs(dst[:, :, 1].max() - dst[:, :, 1].min()) < obj_size[0] or \
                        np.abs(dst[:, :, 1].max() - dst[:, :, 1].min()) > obj_size[1]:
                    return None
                return dst
            else:
                # print("Not enough matches are found - %d/%d" % (len(good), min_match_count))
                return None
        except:
            # print(traceback.format_stack())
            # print(cv2.contourArea(pts))
            # print(pts)
            return None

