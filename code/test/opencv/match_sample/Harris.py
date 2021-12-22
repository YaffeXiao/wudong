
import cv2
import numpy as np
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10
def harris_t(img1, img2):

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray1 = np.float32(gray1)
    dst = cv2.cornerHarris(gray1, 2, 3, 0.04)

    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    img1[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow('dst1', img1)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    img2 = img2[600:]
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    gray2 = np.float32(gray2)
    dst2 = cv2.cornerHarris(gray2, 2, 3, 0.04)

    # result is dilated for marking the corners, not important
    dst2 = cv2.dilate(dst2, None)

    # Threshold for an optimal value, it may vary depending on the image.
    img2[dst2 > 0.01 * dst2.max()] = [0, 0, 255]

    cv2.imshow('dst2', img2)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

    