from Data.data_iris import irisData
import tensorflow as tf
import numpy as np

x_train, y_train = irisData()
x_test, y_test = irisData()


x_train = x_train.astype(np.float32)
x_test = x_test.astype(np.float32)
y_train = y_train.astype(np.float32)
y_test = y_test.astype(np.float32)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, input_shape=(4,), activation='softmax'),
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=500)

np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})
print(model.predict(x_test))

# 6. 정확도 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print('테스트 정확도:', test_acc)
k=10



