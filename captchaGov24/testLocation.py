import tensorflow as tf
import cv2
import numpy as np

startIndex = 10
imageWidth = 20
endIndex = 130

img = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)

ret, src = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

x_train = np.zeros((len(range(startIndex, endIndex - imageWidth)), 50, imageWidth), dtype=np.float)
index = 0

for i in range(startIndex, endIndex - imageWidth):
    x_train[index] = src[:, i:i + imageWidth]

    index = index + 1

x_train /= 255.

model = tf.keras.models.load_model('location')

ls = model.predict(x_train)
result = []
index = 0
for l in ls:
    p = 10

    if l[0] >= 0 and l[0] <= imageWidth:
        result.append(l[0] + startIndex + index)

    if l[1] >= 0 and l[1] <= imageWidth:
        result.append(l[1] + startIndex + index)
    index += 1
k = 0

from sklearn.cluster import KMeans
from statistics import mean

kmodel = KMeans(6)
kmodel.fit(np.array(result).reshape(len(result), 1))
label = kmodel.labels_
empty = []

for i in range(6):
    empty.append(int(mean([result[i] for i in np.where(label == i)[0]])))

empty.sort()


k = 10
