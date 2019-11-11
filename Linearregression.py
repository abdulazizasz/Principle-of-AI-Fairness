import numpy as np
from sklearn.linear_model import LinearRegression

"""
data needs to be modified here i tried importing the data from website but it doesnt seem to work properly 

"""

x = np.array([3, 10, 35, 87, 33, 99]).reshape((-1, 1))
y = np.array([10, 87, 99, 32, 35, 38])

model = LinearRegression()

model.fit(x, y)

r_sq = model.score(x, y)

"""
coefficient of determination model.score(x, y)


intercept is model.intercept_

slope is model.coef_

    
"""
y_pred = model.predict(x)