import cv2

flag = cv2.IMREAD_COLOR
image = cv2.imread("test.png", flag)
cv2.imshow("aaa", image)
cv2.waitKey(3000)
cv2.cvtColor(src, flag)

cv2.imwrite("text.png", src)



