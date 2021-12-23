import cv2
import numpy as np


class SiftTool:
    MIN_MATCH_COUNT = 10
    SIFT = cv2.xfeatures2d.SIFT_create()

    # @staticmethod
    # def get_dst(img1, img2):
    #
    #     img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #     img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #     # 初始化SIFT检测器
    #     sift = cv2.xfeatures2d.SIFT_create()
    #
    #     # 使用SIFT检测器寻找关键点和描述符
    #     kp1, des1 = sift.detectAndCompute(img1, None)
    #     kp2, des2 = sift.detectAndCompute(img2, None)
    #
    #     FLANN_INDEX_KDTREE = 0
    #     index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    #     search_params = dict(checks=50)
    #
    #     flann = cv2.FlannBasedMatcher(index_params, search_params)
    #
    #     matches = flann.knnMatch(des1, des2, k=2)
    #
    #     # 根据Lowe比率测试存储所有良好匹配项
    #     good = []
    #     for m, n in matches:
    #         if m.distance < 0.7 * n.distance:
    #             good.append(m)
    #
    #     if len(good) > MIN_MATCH_COUNT:
    #         src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    #         dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    #
    #         M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    #         matchesMask = mask.ravel().tolist()
    #
    #         h, w = img1.shape
    #         pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    #         dst = cv2.perspectiveTransform(pts, M)
    #         return dst
    #     else:
    #         print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
    #         return None


    @staticmethod
    def get_dst_by_p(kp1, des1, img1, img2, min_match_count=6):
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
            if m.distance < 0.6 * n.distance:
                good.append(m)

        if len(good) > min_match_count:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()

            h, w = img1.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            # if (pts.max() - pts.min()) > 10:
            #     return None
            # print(cv2.contourArea(pts))
            # print(pts)
            try:
                dst = cv2.perspectiveTransform(pts, M)
                # print(dst)
                if dst[:,:,0].max() - dst[:,:,0].min() > 100 or dst[:,:,1].max() - dst[:,:,1].min() > 100 or \
                        dst[:,:,0].max() - dst[:,:,0].min() < 20 or dst[:,:,1].max() - dst[:,:,1].min() < 20:
                    return None
                return dst
            except :
                # print(traceback.format_stack())
                # print(cv2.contourArea(pts))
                # print(pts)
                return None
        else:
            # print("Not enough matches are found - %d/%d" % (len(good), min_match_count))
            return None

    @staticmethod
    def get_dst_by_m(kp1, des1, img1, img2, min_match_count=10):
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
                if m.distance < 0.7 * n.distance:
                    good.append(m)
            if len(good) > min_match_count:
                src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                h, w = img1.shape
                pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)

                # print(dst)
                if dst[:, :, 0].max() - dst[:, :, 0].min() > 200 or dst[:, :, 1].max() - dst[:, :, 1].min() > 200 or \
                        dst[:, :, 0].max() - dst[:, :, 0].min() < 20 or dst[:, :, 1].max() - dst[:, :, 1].min() < 20:
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


    @staticmethod
    def get_dst_by_button(kp1, des1, img1, img2, min_match_count=10):
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
            if m.distance < 0.7 * n.distance:
                good.append(m)

        if len(good) > min_match_count:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            h, w = img1.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            try:
                dst = cv2.perspectiveTransform(pts, M)
                if len(dst) < 4:
                    return None
                return dst
            except:
                return None
        else:
            # print("Not enough matches are found - %d/%d" % (len(good), min_match_count))
            return None

    @staticmethod
    def get_dst_common(kp1, des1, img1, img2, min_match_count=10):
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
            if m.distance < 0.7 * n.distance:
                good.append(m)

        if len(good) > min_match_count:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()

            h, w = img1.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            # if (pts.max() - pts.min()) > 10:
            #     return None
            # print(cv2.contourArea(pts))
            # print(pts)
            try:
                dst = cv2.perspectiveTransform(pts, M)

                # print(dst)
                if dst[:, :, 0].max() - dst[:, :, 0].min() > 200 or dst[:, :, 1].max() - dst[:, :, 1].min() > 200 or \
                        dst[:, :, 0].max() - dst[:, :, 0].min() < 20 or dst[:, :, 1].max() - dst[:, :, 1].min() < 20:
                    return None
                return dst
            except:
                # print(traceback.format_stack())
                # print(cv2.contourArea(pts))
                # print(pts)
                return None
        else:
            # print("Not enough matches are found - %d/%d" % (len(good), min_match_count))
            return None