'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 决策树的基本使用
@LastEditorTime: 2020-01-18
'''
# 导入numpy计算库
from sklearn.model_selection import train_test_split
import numpy as np

# 导入画图工具
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 导入tree树模型和数据集加载工具
from sklearn import tree
from sklearn import datasets

'''
设置超参数max_depth
'''
_max_depth = {1, 3, 5}


# 导入数据拆分工具
wine = datasets.load_wine()

# 1. 载入Wine数据集
# 设置X, y的值。此处为了便于可视化，仅选取前两个特征
X = wine.data[:, :2]
# X = wine.data
y = wine.target
# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y)


def Output(_max_depth):
    # 2. 配置决策树，并拟合训练集
    # 设置决策树的分类器的最大深度为 1
    clf = tree.DecisionTreeClassifier(max_depth=_max_depth)
    # 拟合训练数据集
    clf.fit(X_train, y_train)

    # 3. 输出预测准确率
    # 输出模型评分，即正确率
    score_train = clf.score(X_train, y_train)
    score_test = clf.score(X_test, y_test)

    print("树深 = {0}：训练集准确率：{1:.3f}，测试集准确率：{2:.3f}".format(
        _max_depth, score_train, score_test))

    # 4. 可视化分类结果
    # 定义图像中分区的颜色和散点的颜色
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    # 分别用样本的两个特征值创建图像的横轴和纵轴
    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
    # 设置特征轴的尺度的粒度
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 给每个分类中的样本分配不同的颜色
    Z = Z.reshape(xx.shape)
    plt.figure(dpi=100)
    plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # 用散点把样本表示出来
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("分类器: 决策树(max_depth = {})".format(_max_depth))

    plt.show()


for i in _max_depth:
    Output(i)
