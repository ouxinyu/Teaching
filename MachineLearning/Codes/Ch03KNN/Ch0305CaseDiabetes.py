'''
@Author: Xin-Yu Ou (欧新宇)
@Description: K最近邻算法案例 —— 酒的分类
@LastEditorTime: 2020-01-16
'''
# 加载 pandas库，并使用read_csv()函数读取糖尿病预测数据集diabetes
import pandas as pd
import numpy as np
# 导入绘图工具箱 matplotlib
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import learning_curve

# 1. 载入数据集
# 从sklearn的datasets模块中载入数据集
data = pd.read_csv('datasets/diabetes.csv')

# 2. 对数据集进行拆分（训练集+测试集）
# 将数据中的特征和标签进行分离，其中第0位为索引号，第1-8位为特征，第9位为标签
X = data.iloc[:, 0:8]
y = data.iloc[:, 8]
print("X的形状为{0}，Y的形状为{1}".format(X.shape, y.shape))

# 以 80%:20%的比例对训练集和测试集进行拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. 使用KNN构建模型
# 引入KNN分类模型, 并配置KNN分类器，设置近邻数 = 2
knn = KNeighborsClassifier(n_neighbors=4)

knn.fit(X_train, y_train)

# 4. 预测与评分
train_score = knn.score(X_train, y_train)
test_score = knn.score(X_test, y_test)

print("训练集评分:{0:.2f}；测试集评分:{1:.2f}".format(train_score, test_score))


# 定义一个函数用于绘制学习曲线
def plot_learning_curve(plt, estimator, title, X, y, ylim=None, cv=None, n_jobs=1, train_sizes=np.linspace(0.1, 1.0, 5)):
    """
    函数功能描述：生成训练集和测试集的简单学习曲线。

    参数：
    ----------
    estimator : 分类器或预测器对象。
    title: 字符串类型, 图的标题
    X : 矩阵类型, shape (n_samples, n_features)， 用于保存训练样本，其中行表示样本的数量，列表示特征的数量
    y : 矩阵类型, shape (n_samples) 或者 (n_samples, n_features), 该参数用于保存样本的标签值，为空时表示无监督学习。
    ylim : 元组类型, shape (ymin, ymax), 可选。定义图的y轴的取值范围。
    cv : 整型, cross-validation 交叉验证生成器或可迭代设置，可选。用于确定交叉验证的分割策略。
        cv有以下几种输入:
          - None, 默认状态下，使用 3-fold cross-validation,
          - integer, 指定倍数为整数 n.
          - 指定用作交叉验证生成器的对象.
          - 一个可迭代的产生序列/测试的分割对象.
          - 当标签"y"是二进制或者多类时，使用参数integer或None，此时会使用StratifsiedKFold用法类
          - 当标签"y"不是二进制值，或estimtor不是分类器时，此时会使用KFold用法类
    n_jobs : 整型, 可选。并行运算的数量，通常在使用GPU，或CPU并行的时候使用。
    """

    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("score")
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o--', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

    plt.legend(loc="best")
    plt.show()
    return plt


# 从模型选择子库中导入数据集拆分工具

knn = KNeighborsClassifier(n_neighbors=2)
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
plt.figure(figsize=(8, 6), dpi=100)
plot_learning_curve(plt, knn, 'Learning Curve for KNN Diabetes', X, y, ylim=(0, 1.01), cv=cv)
