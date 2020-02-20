from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.svm import SVC


# TODO: 1.载入数据集
# 载入wine数据集
wine = datasets.load_wine()

# TODO: 2.拆分数据集：按照 7:1:2 的比例来进行划分训练集、验证机和测试集
X_trainval, X_test, y_trainval, y_test = train_test_split(
    wine.data, wine.target, train_size=0.8, random_state=10)
X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, train_size=0.875,  random_state=10)

# 设置linear核的SVC
svc = SVC(kernel='linear')
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#     kernel='linear', max_iter=-1, probability=False, random_state=None,
#     shrinking=True, tol=0.001, verbose=False)

shuffle_split = ShuffleSplit(test_size=.2, train_size=.7, n_splits=10)

# 使用cross_val_score计算交叉验证评分
scores = cross_val_score(svc, X_trainval, y_trainval, cv=shuffle_split)
print("● 训练集上训练的结果")
print('迭代次数:{}'.format(len(scores)))
print('随机拆分平均分(验证集评分)：{:.3f}'.format(scores.mean()))

# TODO: 4.保持模型参数不变，在训练集+验证集上重新进行训练，并在测试集上输出模型的最终评分
svc.fit(X_trainval, y_trainval)
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#     kernel='linear', max_iter=-1, probability=False, random_state=None,
#     shrinking=True, tol=0.001, verbose=False)

score_test = svc.score(X_test, y_test)
print("● 训练验证集上训练的结果")
print("测试集评分{:.4f}.".format(score_test))
