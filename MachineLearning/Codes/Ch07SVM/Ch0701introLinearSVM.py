'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 基于线性核的SVM简介
@LastEditorTime: 2020-01-22
'''
# 1.导入必须库
import os
import numpy as np
import matplotlib.pyplot as plt
# 导入支持向量机SVM
from sklearn import svm
# 导入数据集生成和拆分工具
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

# 2.创建/导入数据
X, y = make_blobs(n_samples=100, centers=2, random_state=6)

# 3.数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 4.构建模型，并进行模型训练（或称为拟合数据）
clf = svm.SVC(kernel='linear', C=1000)
clf.fit(X_train, y_train)

# 5.输出模型准确率
print("线性SVM训练集评分为: {0:.3f}, 测试集评分为: {1:.3f}".format(
    clf.score(X_train, y_train), clf.score(X_test, y_test)))

# 6.可视化分析
# c: 色彩或颜色序列; s: 散点尺寸; cmap: Colormap
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, s=30, cmap=plt.cm.Paired)

# 建立图像坐标
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# 生成两个等差数列
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# 绘制分类的决定边界
ax.contour(XX, YY, Z, colors='k',
           levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
# 加强绘制支持向量
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[
           :, 1], s=100, linewidth=1, facecolors='b')

plt.savefig(os.getcwd() + '/Codes/Ch07SVM/results/Ch0701intoLinearSVM.png', dpi=300)
plt.show()
