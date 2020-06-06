from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# TODO: 1.载入数据集
# 载入wine数据集
wine = datasets.load_wine()

# TODO: 2.拆分数据集：按照 7:1:2 的比例来进行划分训练集、验证机和测试集
X_trainval, X_test, y_trainval, y_test = train_test_split(
    wine.data, wine.target, train_size=0.8, random_state=10)
X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, train_size=0.875,  random_state=10)

# 观察数据集形态
print("原始数据集形态{}".format(wine.data.shape))
print("训练集形态{}, 验证集形态{}, 测试集形态{}".format(
    X_train.shape, X_val.shape, X_test.shape))

# TODO: 3.配置分类器，此处用一个简单的SVC分类器
# 1). 首先在训练集上进行训练
# 2). 然后分别在训练集和验证集上测试性能
# 3). 根据性能结果，反复调整超参数，直达达到预期性能
# 设置linear核的SVC
svc = SVC(kernel='linear')
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#     kernel='linear', max_iter=-1, probability=False, random_state=None,
#     shrinking=True, tol=0.001, verbose=False)

svc.fit(X_train, y_train)
score_train = svc.score(X_train, y_train)
score_val = svc.score(X_val, y_val)
score_test = svc.score(X_test, y_test)

print("● 训练集上训练的结果")
print("训练集评分{:.4f}, 验证集评分{:.4f}, 测试集评分{:.4f}".format(
    score_train, score_val, score_test))

# 按照评分结果反复调节参数，直到获得最优模型
# svc.fit(X_train, y_train)
# svc.score(X_train,y_train)
# svc.score(X_val, y_val)

# TODO: 4.保持模型参数不变，在训练集+验证集上重新进行训练，并在测试集上输出模型的最终评分
svc.fit(X_trainval, y_trainval)
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#     kernel='linear', max_iter=-1, probability=False, random_state=None,
#     shrinking=True, tol=0.001, verbose=False)
score_test = svc.score(X_test, y_test)

print("● 训练验证集上训练的结果")
print("测试集评分{:.4f}.".format(score_test))
