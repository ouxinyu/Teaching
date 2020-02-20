from sklearn import datasets
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import numpy as np

# TODO: 1.载入数据集
# 载入wine数据集
wine = datasets.load_wine()

# TODO: 2.拆分数据集：按照 7:1:2 的比例来进行划分训练集、验证机和测试集
X_trainval, X_test, y_trainval, y_test = train_test_split(
    wine.data, wine.target, train_size=0.8, random_state=38)
X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, train_size=0.875,  random_state=38)

best_score = 0
for alpha in [0.01, 0.1, 1.0, 10.0]:
    for max_iter in [100, 1000, 5000, 10000]:
        lasso = Lasso(alpha=alpha, max_iter=max_iter)
        scores = cross_val_score(lasso, X_train, y_train, cv=6)
        score = np.mean(scores)
        if score > best_score:
            best_score = score
            best_parameters = {'alpha': alpha, 'max_iter': max_iter}

print("模型最高分(验证集）为：{:.4f}".format(best_score))
print('最佳参数设置：{}'.format(best_parameters))

# TODO: 3.根据交叉验证获得的参数输出最终评分
lasso = Lasso(alpha=0.01, max_iter=100)
lasso.fit(X_trainval, y_trainval)
score = lasso.score(X_test, y_test)

print("模型最高分(测试集）为：{:.4f}".format(score))
