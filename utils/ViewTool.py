import cv2


def get_gray_img(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def image_rectangle(image, contours, top_offset=0):
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y + top_offset), (x + w, y + top_offset + w), (255, 0, 0), 1)
    return image


class ViewTool:

    def __init__(self, min_contour_area=40, max_contour_area=200):
        self.min_contour_area = min_contour_area
        self.max_contour_area = max_contour_area

    def get_rectangle(self, gray):
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  # 图像二值化
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        result_contours = []
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if self.min_contour_area < area <= self.max_contour_area:
                result_contours.append(contour)
        return result_contours
