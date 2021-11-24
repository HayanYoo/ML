import numpy as np
import tensorflow as tf

# 실제 결과로 매핑할 데이터
train_x = np.array([[1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]  # 0
                       , [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]  # 0
                       , [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]  # 0
                       , [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]  # 0
                       , [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1]  # 1
                       , [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1]  # 1
                       , [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1]  # 1
                       , [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1]  # 1
                    ], dtype="uint8")  # * 255
train_y = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype="uint8")

# create model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(6, input_shape=(15,), activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='mse')

# train model
model.fit(train_x, train_y, epochs=1000)



zero = np.array([1, 1, 1
                    , 1, 0, 1
                    , 1, 0, 1
                    , 1, 0, 1
                    , 1, 1, 1], dtype="uint8")  # * 255
one = np.array([0, 1, 0
                   , 1, 1, 0
                   , 0, 1, 0
                   , 0, 1, 0
                   , 1, 1, 1], dtype="uint8")  # * 255

test = np.array([zero, one])
np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})
print(model.predict(test))
