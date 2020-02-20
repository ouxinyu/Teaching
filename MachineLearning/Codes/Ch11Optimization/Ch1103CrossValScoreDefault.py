from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.svm import SVC
import numpy as np

# TODO: 1.载入数据集
# 载入wine数据集
wine = datasets.load_wine()

# TODO: 2.拆分数据集：按照 7:1:2 的比例来进行划分训练集、验证机和测试集
X_trainval, X_test, y_trainval, y_test = train_test_split(
    wine.data, wine.target, train_size=0.8, random_state=10)

nums = 10
scores = np.zeros([2, nums])

# TODO: 3.配置分类器，此处用一个简单的SVC分类器
# 1). 将训练验证集上进行K折
# 2). 输出每个验证集上的评分
# 3). 计算每个验证集上评分的平均分
# 设置linear核的SVC
# 设置4折验证，并使用SVC模型进行训练
kf = KFold(n_splits=nums, random_state=None, shuffle=False)
# 设置linear核的SVC
svc = SVC(kernel='linear')
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#     kernel='linear', max_iter=-1, probability=False, random_state=None,
#     shrinking=True, tol=0.001, verbose=False)

# TODO: 4.配合cross_val_score的默认参数实现KFold
# 使用cross_val_score计算交叉验证评分
scores = cross_val_score(svc, X_trainval, y_trainval, cv=5)
# C:\ProgramData\Anaconda3\lib\site-packages\sklearn\model_selection\_split.py:1978: FutureWarning: The default value of cv will change from 3 to 5 in version 0.22. Specify it explicitly to silence this warning.
#   warnings.warn(CV_WARNING, FutureWarning)
print("● 训练集上训练的结果")
print('交叉验证得分：{}'.format(scores))
print('交叉验证平均分(验证集评分)：{:.3f}'.format(scores.mean()))

# TODO: 4.保持模型参数不变，在训练集+验证集上重新进行训练，并在测试集上输出模型的最终评分
svc.fit(X_trainval, y_trainval)
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#     kernel='linear', max_iter=-1, probability=False, random_state=None,
#     shrinking=True, tol=0.001, verbose=False)

score_test = svc.score(X_test, y_test)
print("● 训练验证集上训练的结果")
print("测试集评分{:.4f}.".format(score_test))
