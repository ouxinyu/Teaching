from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
# 从模型选择子库中导入数据集拆分工具
from sklearn.model_selection import train_test_split

# TODO: 1.创建数据集并进行分隔
X, y = datasets.make_blobs(n_samples=100, centers=2,
                           random_state=50, cluster_std=2)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=8, train_size=0.7)

# TODO: 2.输出原始数据集的数据统计信息, 给出样本两个特征的极值
print("原始数据，训练集特征一的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X_train[:, 0]), np.min(X_train[:, 0])))
print("原始数据，训练集特征二的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X_train[:, 1]), np.min(X_train[:, 1])))
print("原始数据，测试集特征一的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X_test[:, 0]), np.min(X_test[:, 0])))
print("原始数据，测试集特征二的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X_test[:, 1]), np.min(X_test[:, 1])))

# TODO: 3.使用StandardScaler对样本的特征X进行数据预处理
scaler1 = preprocessing.StandardScaler().fit(X_train)
X1_train = scaler1.transform(X_train)
X1_test = scaler1.transform(X_test)

# TODO: 4.输出StandardScaler处理后的数据统计信息, 给出样本两个特征的极值
print("StandardScaler, 训练集特征一的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X1_train[:, 0]), np.min(X1_train[:, 0])))
print("StandardScaler, 训练集特征二的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X1_train[:, 1]), np.min(X1_train[:, 1])))
print("StandardScaler, 测试集特征一的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X1_test[:, 0]), np.min(X1_test[:, 0])))
print("StandardScaler, 测试集特征二的最大值：{:.2f}， 最小值：{:.2f}。".format(
    np.max(X1_test[:, 1]), np.min(X1_test[:, 1])))

# TODO: 5.输出图形，并保存
plt.figure(figsize=(12, 4))
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

plt.subplot(121)
# 绘制样本的散点图
plt.scatter(X_train[:, 0], X_train[:, 1], c='c', cmap=plt.cm.cool, label='训练集')
plt.scatter(X_test[:, 0], X_test[:, 1], c='b', cmap=plt.cm.cool, label='测试集')
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']
plt.title('图1: 原始数据图')

plt.subplot(122)
# 绘制样本的散点图
plt.scatter(X1_train[:, 0], X1_train[:, 1],
            c='c', cmap=plt.cm.cool, label='训练集')
plt.scatter(X1_test[:, 0], X1_test[:, 1], c='b', cmap=plt.cm.cool, label='测试集')
plt.title('图2: StandardScaler')

plt.legend(loc='best')
plt.savefig('Codes//Ch09Preprocessing//results//Ch0901StandardScaler.png', dpi=150)
plt.show()