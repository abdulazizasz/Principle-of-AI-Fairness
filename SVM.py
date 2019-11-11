import numpy as np
from sklearn.svm import SVC
"""
dataset must be included here 

"""

X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])

y = np.array([1, 1, 2, 2])

clf = SVC(gamma='auto')

clf.fit(X, y) 

print(clf.predict([[-0.8, -1]]))
