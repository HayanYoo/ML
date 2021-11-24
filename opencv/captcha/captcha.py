import cv2
import numpy as np





img = cv2.imread("src/captcha.jpg", cv2.IMREAD_GRAYSCALE)

ret, src = cv2.threshold(img, 0 , 255, cv2.THRESH_BINARY)

#모폴로지
k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# 침식 연산 적용 ---②
# erosion = cv2.erode(src, k)

erosion1 = cv2.dilate(src, k)


cv2.waitKey()

