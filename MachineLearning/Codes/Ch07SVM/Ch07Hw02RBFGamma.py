'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 鸢尾花数据集上RBF-SVM的超参数Gamma对比
@LastEditorTime: 2020-01-26
'''
# TODO: 1. 导入必须库 以及 定义必要的函数
import numpy as np
import matplotlib.pyplot as plt
import os
# 导入机器学习数据集处理工具
from sklearn import datasets
from sklearn.model_selection import train_test_split
# 导入支持向量机SVM
from sklearn import svm

# TODO: 2. 创建/导入数据
iris = datasets.load_iris()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6)


# TODO: 4. 构建模型，并进行模型训练（或称为拟合数据）
C = 1.0
# gamma = np.concatenate((np.linspace(0.1, 1, 10), np.linspace(2, 10, 9)), axis=0)
gamma = np.linspace(0.1, 1, 10)
num = gamma.shape[0]
scores = np.zeros([2, num])  # 第1-4列分别为：score_train_rbf,score_test_rbf
x_lim = np.arange(0, num)


for i in range(num):
    n = i + 1
    model = svm.SVC(kernel='rbf', gamma=gamma[i], C=C)
    model.fit(X_train, y_train)

    scores[0, i] = model.score(X_train, y_train)
    scores[1, i] = model.score(X_test, y_test)

plt.figure(dpi=150)
plt.plot(gamma, scores[0, :], label="Train")
plt.plot(gamma, scores[1, :], label="Test")
plt.xticks(gamma)

plt.legend(loc='best')
plt.savefig(os.getcwd() + '/Codes/Ch07SVM/results/Ch08Hw01SVM.png', dpi=300)
plt.show()
