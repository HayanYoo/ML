import pandas as pd
import numpy as np

def irisData(col = -1, category = True):
    data = pd.read_csv("../Data/iris.csv").values
    if category:
        a, b = np.unique(data[:, -1], return_inverse=True)
        data[:, -1] = b
    data = data[:, 1:]
    #np.concatenate([a, b], axis=1)
    y = data[:, col]
    return np.delete(data, col, axis=1), y

#일반 x = 0~4, y = 5(품종, category적용1~3)
irisData()
#일반 x = 0~4, y = 5(품종)
irisData(-1, False)
#일반 x = 0~2 + 4~5, y = 3
irisData(3)