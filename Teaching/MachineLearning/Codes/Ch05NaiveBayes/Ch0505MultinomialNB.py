'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 多项式朴素贝叶斯
@LastEditorTime:2020-01-17
'''
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

# 1. 载入数据及数据初始化
# 生成样本数为 50000， 分类数为 2的数据集，并按照 75%:25% 的比例进行拆分
X, y = make_blobs(n_samples=500, centers=5, random_state=8)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# 2. 模型评分
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 导入多项式贝叶斯
# 使用多项式贝叶斯拟合数据
mnb = MultinomialNB()
mnb.fit(X_train_scaled, y_train)
score = mnb.score(X_test_scaled, y_test)

print("模型评分：{:.3f}".format(score))

# 3. 可视化分析
# 设置坐标轴的范围
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

# 设置图的分辨率为150像素
plt.figure(dpi=100)
# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 用不同背景颜色表示不同的类别
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

z = mnb.predict(np.c_[(xx.ravel(), yy.ravel())]).reshape(xx.shape)
plt.pcolormesh(xx, yy, z, cmap=plt.cm.Pastel1)

# 将训练集和测试集用散点图表示出来
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
            cmap=plt.cm.cool, edgecolor="k")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.cool, marker="*")

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# 设置图标题
plt.title("分类器：多项式朴素贝叶斯 (MultinomialNB)")
plt.show()
