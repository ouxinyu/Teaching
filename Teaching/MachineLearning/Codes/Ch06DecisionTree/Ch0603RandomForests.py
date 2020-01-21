'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 随机森林
@LastEditorTime: 2020-01-18
'''
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# 导入随机森林模型
from sklearn.ensemble import RandomForestClassifier

# 1. 载入数据集
wine = datasets.load_wine()
X = wine.data[:, :2]  # 为便于可视化仍然仅使用前两个特征
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 2. 模型训练
# 设定随机森林中树的数量，此处 = 6
forest = RandomForestClassifier(n_estimators=6, random_state=3, n_jobs=-1)
forest.fit(X_train, y_train)

# 3. 模型评估
score_train = forest.score(X_train, y_train)
score_test = forest.score(X_test, y_test)

print("随机森林：\n 训练集准确率：{0:.3f}，测试集准确率：{1:.3f}".format(score_train, score_test))

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

Z = forest.predict(np.c_[xx.ravel(), yy.ravel()])

# 给每个分类中的样本分配不同的颜色
Z = Z.reshape(xx.shape)
plt.figure(dpi=100)
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# 用散点把样本表示出来
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("分类器：随机森林")

plt.show()
