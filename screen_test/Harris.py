
import cv2
import numpy as np

def harris_t(file_name):
    img = cv2.imread(file_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    # 输入图像必须是float32，最后一个参数在0.04 到0.06 之间
    dst = cv2.cornerHarris(gray,2,3,0.04)
    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('dst',img)
    cv2.waitKey()
