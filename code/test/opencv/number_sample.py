
from PIL import Image
import cv2
import numpy as np
import pytesseract

def cv_show(_img, name="test"):
    cv2.namedWindow(name, 0)
    # cv2.resizeWindow(name,  720, 1200)
    # cv2.resizeWindow(name, _img.shape[0] / 4, _img.shape[1] / 4)
    cv2.resizeWindow(name, _img.shape[0], _img.shape[1])
    cv2.imshow(name, _img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("1080/zhulou.png", 0)

# pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# tessdata_dir_config = '--tessdata-dir "D:/Program Files (x86)/Tesseract-OCR/tessdata"'
# h, w = img.shape[:2]
    # 遍历像素点进行处理
# for y in range(0, w):
#     for x in range(0, h):
#         # 去掉边框上的点
#         if y == 0 or y == w - 1 or x == 0 or x == h - 1:
#             img[x, y] = 255
#             continue
#         count = 0
#         if np.all(img[x, y - 1] == 255):
#             count += 1
#         if np.all(img[x, y + 1] == 255):
#             count += 1
#         if np.all(img[x - 1, y] == 255):
#             count += 1
#         if np.all(img[x + 1, y] == 255):
#             count += 1
#         if count > 2:
#             img[x, y] = 255
# n_im = 255 - np.array(img_gray)
img = img[570:600, 200:250]
img[img < 100] = 0
img[img > 100] = 255
n_im = 255 - np.array(img)
print(img.shape)
cv_show(n_im)
n_im = cv2.resize(n_im, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST )
cv_show(n_im)
# image = Image.open("1080/zhulou.png")
resDict = pytesseract.image_to_string(Image.fromarray(n_im),config=" --psm 6   ")
# # resDict = pytesseract.image_to_string(Image.fromarray(img[500:700, 200:]), config=" --psm 6   ")
# print(resDict)
