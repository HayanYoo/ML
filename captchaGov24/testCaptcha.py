import tensorflow as tf
import cv2
import numpy as np
import testLocation1

imageWidth = 20

img = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)

ret, src = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)


x_train = np.zeros((6, 50, imageWidth), dtype=np.float)
location = testLocation1.location()
index = 0

for i in range(6):
    x_train[index] = src[:, location[i]: location[i] + imageWidth]

    index += 1

x_train /= 255

model = tf.keras.models.load_model('class_captcha')

ls = model.predict(x_train)

result = []
for number in ls:
    result.append(np.argmax(number))

print(''.join(map(str, result)))


