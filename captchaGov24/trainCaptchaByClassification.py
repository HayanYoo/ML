
import os
import numpy as np
import cv2

imagePath = "imgB"
labelPath = "labelB"
imageWidth = 20

imageDir = os.listdir(imagePath)
x_train = np.zeros((6 * 3 * len(imageDir), 50, imageWidth), dtype=np.float)
y_train = np.zeros((6 * 3 * len(imageDir)), dtype=np.float)
index = 0
for filename in imageDir:
    img = cv2.imread(imagePath + "/" + filename, cv2.IMREAD_GRAYSCALE)

    file = open(labelPath + "/" + filename.split(".")[0] + ".csv", "r")
    label = list(map(int, file.readline().split(",")))
    file.close()

    y_value = filename.split("_")[0]

    ret, src = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

    for i in range(6):
        x_train[index] = src[:, label[i] - 1:label[i] + imageWidth - 1]
        x_train[index + 1] = src[:, label[i]:label[i] + imageWidth]
        x_train[index + 2] = src[:, label[i] + 1:label[i] + imageWidth + 1]
        y_train[index:index + 3] = int(y_value[i])

        index += 3

x_train/=255


import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(50, imageWidth)),
    tf.keras.layers.Dense(300, activation='sigmoid'),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=10)
model.save("class_captcha")

np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})
print(model.predict(x_train))

# 6. 정확도 평가
test_loss, test_acc = model.evaluate(x_train, y_train)
print('테스트 정확도:', test_acc)

k=10

