from Data.data_iris import irisData
import tensorflow as tf
import numpy as np

x_train, y_train = irisData(2)
x_test, y_test = irisData(2)


x_train = x_train.astype(np.float32)
x_test = x_test.astype(np.float32)
y_train = y_train.astype(np.float32)
y_test = y_test.astype(np.float32)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, input_shape=(4,), activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(loss='mse')

# train model
model.fit(x_train, y_train, epochs=500)

print(model.predict(x_test))

# 6. 정확도 평가
# test_loss, test_acc = model.evaluate(x_test, y_test)
# print('테스트 정확도:', test_acc)

aa = model.predict(x_test)
result = np.zeros((150, 2))
for i in range(len(y_train)):
    result[i][0] = aa[i]
    result[i][1] = y_train[i]

k=10



