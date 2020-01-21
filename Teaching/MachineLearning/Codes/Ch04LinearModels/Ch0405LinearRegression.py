'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 基本线性回归
@LastEditorTime: 2020-01-17
'''
# 0.导入数据集生成工具和拆分工具
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# 1. 使用make_regression()函数生成一个样本数为1000，特征数为2的的数据集
X, y = make_regression(n_samples=1000, n_features=2,
                       n_informative=2, random_state=20, noise=0)

# 2. 使用train_test_split()函数对数据集进行划分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=8, test_size=0.3)

# 3. 使用线性回归模型计算权重 *w* 和 截距 *b* 的值，并给出回归模型的方程
lr = LinearRegression().fit(X_train, y_train)
w = lr.coef_
b = lr.intercept_

# 显示回归模型的方程及参数
print("lr.coef_: {}".format(w))
print("lr.intercept_: {}".format(b))
print("回归方程为：y = {0:.3f}*x1 + {1:.3f}*x2 + {2}".format(w[0], w[1], b))

# 4. 性能分析
score_train = lr.score(X_train, y_train)
score_test = lr.score(X_test, y_test)
print("训练集得分: {:.3f}".format(score_train))
print("测试集得分: {:.3f}".format(score_test))
