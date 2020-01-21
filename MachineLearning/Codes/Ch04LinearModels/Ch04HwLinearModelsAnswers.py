# 1.导入基本运算库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression

# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 2.导入线性回归模型


# 3. 载入糖尿病情数据集，并使用train_test_split()函数对数据集进行划分
X = load_boston().data
y = load_boston().target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=83, test_size=0.3)

# 4. 训练模型
lr = LinearRegression().fit(X_train, y_train)
ridge0 = Ridge(alpha=0).fit(X_train, y_train)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
ridge2 = Ridge(alpha=2).fit(X_train, y_train)
ridge5 = Ridge(alpha=5).fit(X_train, y_train)
lasso001 = Lasso(alpha=0.001, max_iter=100000).fit(X_train, y_train)
lasso02 = Lasso(alpha=0.2, max_iter=100000).fit(X_train, y_train)
lasso1 = Lasso(alpha=1, max_iter=100000).fit(X_train, y_train)

# 4. 性能分析
print("线性回归：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    lr.score(X_train, y_train), lr.score(X_test, y_test)))
print("岭回归(alpha=0)：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    ridge0.score(X_train, y_train), ridge0.score(X_test, y_test)))
print("岭回归(alpha=0.1)：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    ridge01.score(X_train, y_train), ridge01.score(X_test, y_test)))
print("岭回归(alpha=2)：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    ridge2.score(X_train, y_train), ridge2.score(X_test, y_test)))
print("岭回归(alpha=5)：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    ridge5.score(X_train, y_train), ridge5.score(X_test, y_test)))
print("套索回归(alpha=0.001)：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    lasso001.score(X_train, y_train), lasso001.score(X_test, y_test)))
print("套索回归(alpha=0.2)：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    lasso02.score(X_train, y_train), lasso02.score(X_test, y_test)))
print("套索回归(alpha=1)：训练集得分: {0:.4f}，测试集得分: {1:.4f}".format(
    lasso1.score(X_train, y_train), lasso1.score(X_test, y_test)))
