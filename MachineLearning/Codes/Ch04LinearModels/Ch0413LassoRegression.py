'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 套索回归在“糖尿病”数据集上的应用@
同时研究超参数alpha对性能的影响
@LastEditorTime: 2020-01-17
'''
# 0.导入数据集生成工具和拆分工具
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import numpy as np

# 1. 载入糖尿病情数据集
from sklearn.datasets import load_diabetes
X = load_diabetes().data
y = load_diabetes().target

# 2. 使用train_test_split()函数对数据集进行划分
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# 3. 使用线性回归模型计算权重 *w* 和 截距 *b* 的值，并给出回归模型的方程
lasso = Lasso().fit(X_train, y_train)
# lasso = Lasso(max_iter = 100000).fit(X_train, y_train)
# lasso = Lasso(alpha=0.1, max_iter=100000).fit(X_train, y_train)
# lasso = Lasso(alpha = 0.0001, max_iter = 100000).fit(X_train, y_train)


# 4. 性能分析
score_train = lasso.score(X_train, y_train)
score_test = lasso.score(X_test, y_test)
print("训练集得分: {:.3f}".format(score_train))
print("测试集得分: {:.3f}".format(score_test))
print("样本的特征数量: {0}; 模型所使用特征的数量: {1}".format(
    X_train.shape[1], np.sum(lasso.coef_ != 0)))
