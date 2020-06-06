'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 基于KNN的多分类任务
@LastEditorTime: 2020-1-16
'''

# 1. 生成数据集
# 导入样数据集生成器
import time
from sklearn.datasets import make_blobs
# 从近邻算法子库中导入K近邻分类器KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
# 导入绘图工具箱 matplotlib
import matplotlib.pyplot as plt
# 从模型选择子库中导入数据集拆分工具
# from sklearn.model_selection import train_test_split
# 导入计算库
import numpy as np

# 生成数据集，样本数=1000, 类别数=2
n_samples = 1500
X2, y2 = make_blobs(n_samples=n_samples, centers=5, random_state=8)

# 将生成的数据集进行可视化
plt.scatter(X2[:, 0], X2[:, 1], c=y2, cmap=plt.cm.spring, edgecolor='k')
# plt.show()

# 2. 划分训练集和测试集
test_rate = 0.7
split_index = int(n_samples * test_rate)
X2_train = X2[0:split_index]
y2_train = y2[0:split_index]
X2_test = X2[split_index:]
y2_test = y2[split_index:]

# 分别可视化训练样本和测试样本， x: 训练集， o: 测试集
plt.scatter(X2_train[:, 0], X2_train[:, 1], c=y2_train, cmap=plt.cm.spring, edgecolor='k', marker='x')
plt.scatter(X2_test[:, 0], X2_test[:, 1], c=y2_test, cmap=plt.cm.spring, edgecolor='k', marker='o')
# plt.show()


# 3. 基于训练集数据训练KNN模型
# 使用生成的数据集(X, y)训练KNN分类器
clf2 = KNeighborsClassifier()
clf2.fit(X2_train, y2_train)

# 4. 预测及评分

t_start = time.perf_counter()  # 启动计时器
print("正在使用模型，对训练样本的 y 值进行预测...", end="")

# 将分类结果进行可视化
# 分别用样本的两个特征值创建图像和横轴和纵轴
x2_min, x2_max = X2_test[:, 0].min() - 1, X2_test[:, 1].max() + 1
y2_min, y2_max = X2_test[:, 1].min() - 1, X2_test[:, 1].max() + 1
xx2, yy2 = np.meshgrid(np.arange(x2_min, x2_max, 0.02), np.arange(y2_min, y2_max, 0.02))
Z2 = clf2.predict(np.c_[xx2.ravel(), yy2.ravel()])

print("执行时间为：{:.2f}".format(time.perf_counter() - t_start))  # 输出执行时间

# 给每个分类中的样本分配不同的颜色
Z2 = Z2.reshape(xx2.shape)
plt.pcolormesh(xx2, yy2, Z2, cmap=plt.cm.Pastel1)

# 用散点把样本表示出来
plt.scatter(X2_test[:, 0], X2_test[:, 1], c=y2_test, cmap=plt.cm.spring, edgecolor='k')
plt.xlim(xx2.min(), xx2.max())
plt.ylim(yy2.min(), yy2.max())
plt.title("Classifier: KNN")
plt.show()

# 输出模型评分结果
print("模型正确率为：{:.2f}".format(clf2.score(X2_test, y2_test)))
