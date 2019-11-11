import numpy as np
from sklearn.neighbors import KNeighborsClassifier

neigh_clf = KNeighborsClassifier(3)

X = [[0], [1], [2], [3]]

y = [0, 0, 1, 1]

neigh_clf.fit(X, y)

print(neigh.predict([[1.1]]))

print(neigh.predict_proba([[0.9]]))