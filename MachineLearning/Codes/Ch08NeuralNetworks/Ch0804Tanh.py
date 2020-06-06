# TODO: 1. 导入必须库 以及 定义必要的函数
# 导入绘图工具集
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

# 导入数据集
from sklearn import datasets
from sklearn.model_selection import train_test_split
# 导入MLP神经网络
from sklearn.neural_network import MLPClassifier

# TODO: 2. 创建/导入数据
wine = datasets.load_wine()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = wine.data[:, :2]  # 为便于可视化仍然仅使用前两个特征
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16)

# TODO: 4. 构建模型，并进行模型训练（或称为拟合数据）---
mlp_tanh = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[
                         10, 10], activation='tanh', random_state=16)
mlp_tanh.fit(X_train, y_train)

# 使用不同色块显示不同分类
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))

# TODO: 5. 输出预测结果
score_train = mlp_tanh.score(X_train, y_train)
score_test = mlp_tanh.score(X_test, y_test)
print("训练集准确率: {0:.4f}, 测试集准确率: {1:.4f}.".format(score_train, score_test))

# TODO: 6. 可视化预测结果
Z4 = mlp_tanh.predict(np.c_[xx.ravel(), yy.ravel()])

Z4 = Z4.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z4, cmap=cmap_light)

# 将数据特征用散点图绘制出来
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# 设置图的标题，并显示图形
plt.title("MLPClassifier: solver=lbfgs, activation=tanh, nodes=[10, 10]")
plt.show()
