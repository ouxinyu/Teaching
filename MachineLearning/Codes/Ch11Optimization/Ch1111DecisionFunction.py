from sklearn.svm import SVC
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

X, y = make_blobs(n_samples=200, random_state=1, centers=2, cluster_std=5)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.cool, edgecolor='k')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=68)

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2),
                     np.arange(y_min, y_max, 0.2))


svc = SVC(gamma="auto").fit(X_train, y_train)
dec_func = svc.decision_function(X_test)
print(dec_func[:5])

Z = svc.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.summer, alpha=.8)

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.cool,
            edgecolor='k')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.cool,
            edgecolor='k', alpha=0.6)

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('SVC decision_function')
plt.xticks(())
plt.yticks(())
plt.show()
