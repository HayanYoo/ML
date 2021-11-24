import numpy as np
import os
import cv2

imagePath = "imgB"
labelPath = "labelB"
startIndex = 10
imageWidth = 20
endIndex = 130

imageDir = os.listdir(imagePath)
x_train = np.zeros((len(imageDir) * len(range(startIndex, endIndex - imageWidth)), 50, imageWidth), dtype=np.float)
y_train = np.zeros((len(imageDir) * len(range(startIndex, endIndex - imageWidth)), 2), dtype=np.float)
index = 0
for filename in imageDir:
    img = cv2.imread(imagePath + "/" + filename, cv2.IMREAD_GRAYSCALE)

    file = open(labelPath + "/" + filename.split(".")[0] + ".csv", "r")
    label = list(map(int, file.readline().split(",")))
    file.close()

    ret, src = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    for i in range(startIndex, endIndex - imageWidth):
        x_train[index] = src[:, i:i + imageWidth]
        list1 = []
        j = 0
        check = False

        for j in range(len(label)):
            if label[j] >= i and (label[j] <= i + imageWidth):
                check = True
                break
        if check:
            list1.append(label[j] - i)
            if j != len(label)-1 and (label[j + 1] >= i and (label[j + 1] <= i + imageWidth)):
                list1.append(label[j+1] - i)
            else:
                list1.append(30)
        else:
            list1.append(-10)
            list1.append(30)

        y_train[index] = np.array(list1)
        index = index + 1
    k = 10

x_train/=255.


import tensorflow as tf


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(50, imageWidth)),
    tf.keras.layers.Dense(200, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(2)
])
model.compile(optimizer='adam',
              loss='mse',
              metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=100)
model.save("location")

np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})
print(model.predict(x_train))

# 6. 정확도 평가
test_loss, test_acc = model.evaluate(x_train, y_train)
print('테스트 정확도:', test_acc)
k=10



