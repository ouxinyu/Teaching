# TODO: 1. 导入必须库 以及 定义必要的函数
import numpy as np
import matplotlib.pyplot as plt
# 导入 Wine酒 数据集
from sklearn import datasets
from sklearn.model_selection import train_test_split
# 导入支持向量机SVM
from sklearn import svm

# 定义一个绘图函数


def make_meshgrid(x, y, h=0.02):
    x_min, x_max = x.min() - 1, x.max() - 1
    y_min, y_max = y.min() - 1, y.max() - 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

# 第一个一个绘制等高线的函数


def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out


# TODO: 2. 创建/导入数据
wine = datasets.load_wine()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = wine.data[:, :2]  # 为便于可视化仍然仅使用前两个特征
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# TODO: 4. 构建模型，并进行模型训练（或称为拟合数据）
C = 1.0
models = (svm.SVC(kernel='rbf', gamma=0.1, C=C),
          svm.SVC(kernel='rbf', gamma=1, C=C),
          svm.SVC(kernel='rbf', gamma=10, C=C),
          svm.SVC(kernel='rbf', gamma=15, C=C),
          svm.SVC(kernel='rbf', gamma=20, C=C),
          svm.SVC(kernel='rbf', gamma=50, C=C))
# TODO:考虑输出变量models
models = (clf.fit(X_train, y_train) for clf in models)

titles = ('gamma=0.1',
          'gamma=1',
          'gamma=10',
          'gamma=15',
          'gamma=20',
          'gamma=50')


# TODO: 5. 输出模型准确率
# for model, title in zip(models, titles):
#     print("RBFSVM({0}): 训练集准确率: {1:.3f}, 测试集准确率: {2:.3f}".format(
#         title, clf.score(X_train, y_train), clf.score(X_test, y_test)))

# TODO: 6. 可视化分析
# 设定一个子图形的个数和排列方式
fig, sub = plt.subplots(3, 2, figsize=(10, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# 使用自定义的函数进行画图
X0, X1 = X_train[:, 0], X_train[:, 1]
xx, yy = make_meshgrid(X0, X1)

for clf, title, ax in zip(models, titles, sub.flatten()):
    plot_contours(ax, clf, xx, yy, cmap=plt.cm.plasma, alpha=0.8)
    ax.scatter(X0, X1, c=y_train, cmap=plt.cm.plasma, s=20, edgecolors='k')
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xlabel('Feature 0')
    ax.set_ylabel('Feature 1')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)

    # 输出准确率
    print("RBFSVM({0}): 训练集准确率: {1:.3f}, 测试集准确率: {2:.3f}".format(
        title, clf.score(X_train, y_train), clf.score(X_test, y_test)))

plt.show()
